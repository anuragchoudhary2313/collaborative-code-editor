"""
Content Generator Web App
Flask API + HTML Frontend - Production Ready
"""

from flask import Flask, render_template, request, jsonify
from ace import ACELiteLLM
import os
import json
from datetime import datetime
import threading

# Initialize Flask app
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max request size

# Initialize ACE Agent
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
generator = ACELiteLLM(model="groq/llama-3.3-70b-versatile")

# Store generation history
generation_history = []
generation_lock = threading.Lock()

# Configuration
CONTENT_TYPES = {
    "blog": {
        "name": "Blog Post",
        "template": "Generate a well-structured blog post about: {prompt}\n\nRequirements:\n- Engaging introduction\n- 3-4 main sections\n- Conclusion\n- 400-600 words",
    },
    "social": {
        "name": "Social Media Post",
        "template": "Create an engaging social media post about: {prompt}\n\nRequirements:\n- Catchy headline\n- Call-to-action\n- Emoji usage\n- 50-100 words",
    },
    "product": {
        "name": "Product Description",
        "template": "Write a compelling product description for: {prompt}\n\nInclude:\n- Key features\n- Benefits\n- Target audience\n- 150-200 words",
    },
    "email": {
        "name": "Email Campaign",
        "template": "Create an email for: {prompt}\n\nInclude:\n- Compelling subject line\n- Engaging body\n- Clear CTA\n- 150-250 words",
    },
    "script": {
        "name": "Video Script",
        "template": "Write a video script for: {prompt}\n\nInclude:\n- Hook (first 10 seconds)\n- Body\n- Call-to-action\n- ~200-300 words",
    },
}


@app.route("/")
def index():
    """Serve the main page"""
    return render_template("index.html", content_types=CONTENT_TYPES)


@app.route("/api/generate", methods=["POST"])
def generate_content():
    """Generate content based on user request"""
    try:
        data = request.json
        prompt = data.get("prompt", "").strip()
        content_type = data.get("content_type", "blog")

        # Validation
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        if content_type not in CONTENT_TYPES:
            return jsonify({"error": "Invalid content type"}), 400

        if len(prompt) > 500:
            return jsonify({"error": "Prompt too long (max 500 characters)"}), 400

        # Generate content
        template = CONTENT_TYPES[content_type]["template"]
        full_prompt = template.format(prompt=prompt)

        try:
            generated_content = generator.ask(full_prompt)
        except Exception as e:
            return jsonify({"error": f"Generation failed: {str(e)[:100]}"}), 503

        # Store in history
        with generation_lock:
            entry = {
                "id": len(generation_history) + 1,
                "prompt": prompt,
                "content_type": content_type,
                "generated_content": generated_content,
                "timestamp": datetime.now().isoformat(),
                "rating": None,
                "feedback": None,
            }
            generation_history.append(entry)

        return (
            jsonify(
                {"success": True, "content": generated_content, "entry_id": entry["id"]}
            ),
            200,
        )

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)[:100]}"}), 500


@app.route("/api/feedback", methods=["POST"])
def submit_feedback():
    """Submit feedback on generated content"""
    try:
        data = request.json
        entry_id = data.get("entry_id")
        rating = data.get("rating")
        feedback_text = data.get("feedback", "")

        # Validation
        if not entry_id or not rating:
            return jsonify({"error": "Entry ID and rating required"}), 400

        if not isinstance(rating, (int, float)) or rating < 1 or rating > 10:
            return jsonify({"error": "Rating must be between 1-10"}), 400

        # Update history
        with generation_lock:
            for entry in generation_history:
                if entry["id"] == entry_id:
                    entry["rating"] = rating
                    entry["feedback"] = feedback_text
                    break

        # Let agent learn from feedback
        if feedback_text:
            learning_prompt = f"Content rated {rating}/10. Feedback: {feedback_text}. Learn to improve future content."
            try:
                generator.ask(learning_prompt)
            except:
                pass  # Learning is best-effort

        return (
            jsonify(
                {"success": True, "message": "Feedback recorded and agent is learning!"}
            ),
            200,
        )

    except Exception as e:
        return jsonify({"error": f"Error: {str(e)[:100]}"}), 500


@app.route("/api/history", methods=["GET"])
def get_history():
    """Get generation history"""
    with generation_lock:
        return jsonify({"history": generation_history[-20:]}), 200  # Last 20 entries


@app.route("/api/save-model", methods=["POST"])
def save_model():
    """Save the trained model"""
    try:
        generator.save_skillbook("content_generator_production.json")
        return (
            jsonify(
                {
                    "success": True,
                    "message": "Model saved to content_generator_production.json",
                }
            ),
            200,
        )
    except Exception as e:
        return jsonify({"error": f"Save failed: {str(e)[:100]}"}), 500


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Get usage statistics"""
    with generation_lock:
        total = len(generation_history)
        rated = sum(1 for e in generation_history if e["rating"] is not None)
        avg_rating = (
            sum(e["rating"] for e in generation_history if e["rating"]) / rated
            if rated > 0
            else 0
        )

        by_type = {}
        for entry in generation_history:
            ct = entry["content_type"]
            by_type[ct] = by_type.get(ct, 0) + 1

        return (
            jsonify(
                {
                    "total_generated": total,
                    "total_rated": rated,
                    "average_rating": round(avg_rating, 1),
                    "by_content_type": by_type,
                }
            ),
            200,
        )


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Server error"}), 500


if __name__ == "__main__":
    print("=" * 70)
    print("🚀 Content Generator Web App")
    print("=" * 70)
    print("\n✅ Starting Flask server...")
    print("📍 Open http://localhost:5000 in your browser")
    print("\n🎨 Features:")
    print("   ✓ Generate multiple content types")
    print("   ✓ Rate and provide feedback")
    print("   ✓ Agent learns continuously")
    print("   ✓ Save trained models")
    print("   ✓ View generation history")
    print("\n" + "=" * 70)

    app.run(debug=True, host="0.0.0.0", port=5000)
