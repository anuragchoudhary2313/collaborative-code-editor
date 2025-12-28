"""
Collaborative Code Editor with ACE Framework
Features: Real-time collaboration, AI code analysis, suggestions, security checks
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms
from ace import ACELiteLLM
import json
import uuid
import os
from datetime import datetime
from threading import Lock
import re

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
MODEL = "groq/llama-3.3-70b-versatile"

# In-memory storage for sessions
sessions = {}
session_lock = Lock()

# Connected users tracking
connected_users = {}
user_lock = Lock()

# ==================== ACE Framework Components ====================


class CodeQualityEnvironment:
    """
    Evaluates code quality, security, performance, and best practices
    """

    def evaluate(self, code_snippet: str, language: str = "python") -> dict:
        """
        Evaluates code on multiple dimensions
        Returns: {'quality_score': 0-100, 'issues': [...], 'suggestions': [...]}
        """
        evaluation = {
            "quality_score": 85,
            "issues": [],
            "suggestions": [],
            "security_checks": [],
            "performance_tips": [],
        }

        # Check for security issues
        security_keywords = ["eval", "exec", "pickle", "os.system", "subprocess"]
        for keyword in security_keywords:
            if keyword in code_snippet.lower():
                evaluation["issues"].append(f"⚠️ Security: Avoid using '{keyword}'")
                evaluation["security_checks"].append(
                    {
                        "type": "security_risk",
                        "keyword": keyword,
                        "severity": "high",
                        "message": f"'{keyword}' can be a security vulnerability",
                    }
                )
                evaluation["quality_score"] -= 15

        # Check for code complexity
        if len(code_snippet.split("\n")) > 50:
            evaluation["suggestions"].append(
                "Consider breaking this code into smaller functions"
            )
            evaluation["quality_score"] -= 5

        # Check for missing docstrings
        if "def " in code_snippet and '"""' not in code_snippet:
            evaluation["issues"].append("Missing docstrings for functions")
            evaluation["quality_score"] -= 10

        # Performance tips
        if "for" in code_snippet and "append" in code_snippet:
            evaluation["performance_tips"].append(
                "Consider using list comprehension instead of append in loops"
            )

        if "import *" in code_snippet:
            evaluation["issues"].append(
                "Avoid 'import *' - explicitly import needed modules"
            )
            evaluation["quality_score"] -= 10

        # Ensure score is in range
        evaluation["quality_score"] = max(0, min(100, evaluation["quality_score"]))

        return evaluation


class CodeSuggestionAgent:
    """
    Uses ACE Framework to generate intelligent code suggestions
    """

    def __init__(self):
        self.agent = None  # Lazy initialization
        self.evaluation_env = CodeQualityEnvironment()

    def _ensure_agent(self):
        """Lazy load the LLM agent on first use"""
        if self.agent is None:
            self.agent = ACELiteLLM(model=MODEL, api_key=GROQ_API_KEY)

    def analyze_code(self, code: str, language: str = "python") -> dict:
        """Analyze code and return suggestions"""
        try:
            self._ensure_agent()  # Initialize on first use
            evaluation = self.evaluation_env.evaluate(code, language)

            # Generate smart suggestions using LLM
            prompt = f"""Analyze this {language} code and provide 3-5 specific improvements:

CODE:
```{language}
{code[:500]}
```

Provide JSON response with this structure:
{{
    "improvements": [
        {{"suggestion": "...", "reason": "...", "priority": "high|medium|low"}}
    ],
    "refactoring_opportunities": [...]
}}"""

            try:
                response = self.agent.ask(prompt)

                # Try to parse JSON from response
                json_match = re.search(r"\{.*\}", response, re.DOTALL)
                if json_match:
                    suggestions_data = json.loads(json_match.group())
                else:
                    suggestions_data = {
                        "improvements": [],
                        "refactoring_opportunities": [],
                    }
            except:
                suggestions_data = {"improvements": [], "refactoring_opportunities": []}

            return {
                "evaluation": evaluation,
                "suggestions": suggestions_data.get("improvements", []),
                "refactoring": suggestions_data.get("refactoring_opportunities", []),
            }
        except Exception as e:
            return {
                "evaluation": self.evaluation_env.evaluate(code, language),
                "suggestions": [],
                "refactoring": [],
                "error": str(e),
            }

    def generate_explanation(self, code: str, context: str = "") -> str:
        """Generate explanation of what code does"""
        try:
            self._ensure_agent()  # Initialize on first use
            prompt = f"Explain what this code does in 2-3 sentences:\n```\n{code}\n```"
            return self.agent.ask(prompt)
        except:
            return "Unable to generate explanation"


# Initialize the code analysis agent
code_agent = CodeSuggestionAgent()

# ==================== Flask Routes ====================


@app.route("/")
def index():
    """Serve the collaborative code editor UI"""
    return render_template("code_editor.html")


@app.route("/api/session/create", methods=["POST"])
def create_session():
    """Create a new collaborative session"""
    data = request.json
    session_id = str(uuid.uuid4())[:8]

    with session_lock:
        sessions[session_id] = {
            "id": session_id,
            "title": data.get("title", "Untitled"),
            "code": data.get("code", "// Start coding here..."),
            "language": data.get("language", "javascript"),
            "created_at": datetime.now().isoformat(),
            "users": [],
            "analysis": {},
            "history": [],
        }

    return jsonify({"session_id": session_id, "message": "Session created"})


@app.route("/api/session/<session_id>", methods=["GET"])
def get_session(session_id):
    """Get session details"""
    with session_lock:
        if session_id not in sessions:
            return jsonify({"error": "Session not found"}), 404
        session = sessions[session_id]

    return jsonify(
        {
            "id": session["id"],
            "title": session["title"],
            "code": session["code"],
            "language": session["language"],
            "users": session["users"],
            "analysis": session.get("analysis", {}),
            "created_at": session["created_at"],
        }
    )


@app.route("/api/analyze", methods=["POST"])
def analyze_code():
    """Analyze code using ACE Framework"""
    data = request.json
    code = data.get("code", "")
    language = data.get("language", "python")

    analysis = code_agent.analyze_code(code, language)

    return jsonify(analysis)


@app.route("/api/explain", methods=["POST"])
def explain_code():
    """Generate explanation for code snippet"""
    data = request.json
    code = data.get("code", "")

    explanation = code_agent.generate_explanation(code)

    return jsonify({"explanation": explanation})


@app.route("/api/refactor", methods=["POST"])
def refactor_suggestion():
    """Get refactoring suggestions"""
    data = request.json
    code = data.get("code", "")

    analysis = code_agent.analyze_code(code, data.get("language", "python"))

    return jsonify(
        {
            "refactoring_opportunities": analysis.get("refactoring", []),
            "suggestions": analysis.get("suggestions", []),
        }
    )


@app.route("/api/sessions", methods=["GET"])
def list_sessions():
    """List all active sessions"""
    with session_lock:
        session_list = [
            {
                "id": s["id"],
                "title": s["title"],
                "language": s["language"],
                "users_count": len(s["users"]),
                "created_at": s["created_at"],
            }
            for s in sessions.values()
        ]

    return jsonify({"sessions": session_list})


# ==================== WebSocket Events ====================


@socketio.on("join_session")
def on_join(data):
    """User joins a collaborative session"""
    session_id = data.get("session_id")
    username = data.get("username", "Anonymous")
    user_id = str(uuid.uuid4())[:8]

    join_room(session_id)

    with user_lock:
        connected_users[user_id] = {
            "id": user_id,
            "username": username,
            "session_id": session_id,
            "joined_at": datetime.now().isoformat(),
        }

    with session_lock:
        if session_id in sessions:
            sessions[session_id]["users"].append({"id": user_id, "username": username})

    emit(
        "user_joined",
        {
            "user_id": user_id,
            "username": username,
            "message": f"{username} joined the session",
        },
        to=session_id,
    )


@socketio.on("code_change")
def on_code_change(data):
    """Broadcast code changes to all users in session"""
    session_id = data.get("session_id")
    code = data.get("code")
    user_id = data.get("user_id")

    with session_lock:
        if session_id in sessions:
            sessions[session_id]["code"] = code
            sessions[session_id]["history"].append(
                {
                    "timestamp": datetime.now().isoformat(),
                    "user_id": user_id,
                    "code_length": len(code),
                }
            )

    emit(
        "code_updated",
        {"code": code, "user_id": user_id, "timestamp": datetime.now().isoformat()},
        to=session_id,
    )


@socketio.on("request_analysis")
def on_request_analysis(data):
    """User requests code analysis"""
    session_id = data.get("session_id")
    code = data.get("code")
    language = data.get("language", "python")

    analysis = code_agent.analyze_code(code, language)

    with session_lock:
        if session_id in sessions:
            sessions[session_id]["analysis"] = analysis

    emit("analysis_complete", analysis, to=session_id)


@socketio.on("request_explanation")
def on_request_explanation(data):
    """User requests code explanation"""
    session_id = data.get("session_id")
    code = data.get("code")

    explanation = code_agent.generate_explanation(code)

    emit(
        "explanation_ready",
        {"explanation": explanation, "timestamp": datetime.now().isoformat()},
        to=session_id,
    )


@socketio.on("cursor_position")
def on_cursor_position(data):
    """Share cursor position with other users"""
    session_id = data.get("session_id")

    emit(
        "cursor_updated",
        {
            "user_id": data.get("user_id"),
            "username": data.get("username"),
            "line": data.get("line"),
            "column": data.get("column"),
        },
        to=session_id,
        skip_sid=request.sid,
    )


@socketio.on("leave_session")
def on_leave(data):
    """User leaves session"""
    session_id = data.get("session_id")
    user_id = data.get("user_id")

    with user_lock:
        if user_id in connected_users:
            username = connected_users[user_id]["username"]
            del connected_users[user_id]

    with session_lock:
        if session_id in sessions:
            sessions[session_id]["users"] = [
                u for u in sessions[session_id]["users"] if u["id"] != user_id
            ]

    emit(
        "user_left",
        {
            "user_id": user_id,
            "username": username,
            "message": f"{username} left the session",
        },
        to=session_id,
    )

    leave_room(session_id)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5001))
    host = os.getenv("HOST", "0.0.0.0")
    debug = os.getenv("FLASK_ENV", "development") == "development"

    print(f"🚀 Collaborative Code Editor running at http://{host}:{port}")
    print("📝 Features: Real-time collaboration, AI code analysis, suggestions")
    socketio.run(app, host=host, port=port, debug=debug)
