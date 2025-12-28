# 🚀 Collaborative Code Editor - ACE Framework Fullstack App

A powerful, real-time collaborative code editor with AI-powered code analysis, built using the ACE Framework for intelligent suggestions and learning.

## 🎯 Features

### Real-Time Collaboration

- **Multi-user Editing**: Multiple developers can edit the same code simultaneously
- **WebSocket Integration**: Live code synchronization with Socket.IO
- **User Presence**: See who's online and editing in real-time
- **Session Management**: Create/join collaborative sessions

### 🤖 AI-Powered Code Analysis (ACE Framework)

- **Quality Scoring**: Automatic code quality assessment (0-100 scale)
- **Security Analysis**: Detect potential security vulnerabilities
- **Performance Tips**: Suggestions for code optimization
- **Intelligent Explanations**: AI explains what your code does
- **Refactoring Suggestions**: Recommends code improvements

### Developer Experience

- **7 Languages**: JavaScript, Python, Java, C++, HTML, CSS, SQL
- **Syntax Awareness**: Language-specific analysis and suggestions
- **Code Metrics**: Track code complexity and maintainability
- **Analysis History**: View previous analyses and improvements

## 📦 Architecture

```
Frontend (HTML5/CSS3/JS)
    ↓ WebSocket & REST API
Flask Backend (Python)
    ↓ ACE Framework Integration
AI Analysis Engine (Groq LLM)
    ↓
Code Quality Environment
```

### Components

1. **Backend (code_editor_app.py)**

   - Flask REST API with 6 endpoints
   - Flask-SocketIO for real-time collaboration
   - CodeQualityEnvironment for code evaluation
   - CodeSuggestionAgent using ACE Framework

2. **Frontend (templates/code_editor.html)**

   - Glassmorphism UI design
   - Real-time code editor
   - AI analysis dashboard
   - Session management interface

3. **ACE Integration**
   - Intelligent code analysis using Groq API
   - Learning from user interactions
   - Multi-dimension evaluation (quality, security, performance)

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Groq API Key (get free at groq.com)

### Installation

1. **Clone and Navigate**

   ```bash
   cd "c:\Users\anura\OneDrive\Desktop\ACE Framework"
   ```

2. **Activate Virtual Environment**

   ```bash
   .venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

**Option 1: Direct Start**

```powershell
$env:GROQ_API_KEY = 'your-groq-api-key'
python code_editor_app.py
```

**Option 2: Background Process**

```powershell
# PowerShell
$env:GROQ_API_KEY = 'your-groq-api-key'
Start-Process python -ArgumentList "code_editor_app.py"
```

### Access the Application

- **URL**: http://localhost:5001
- **Port**: 5001 (configurable in code_editor_app.py)

## 📖 How to Use

### Create a Session

1. Click "**+ New Session**" button
2. Enter session title (e.g., "My Project")
3. Select programming language
4. Enter your name
5. Click "Create Session"

### Join Existing Session

1. See active sessions in the sidebar
2. Click on a session to join
3. Enter your username
4. You're now collaborating!

### Analyze Code

1. Write or paste code in the editor
2. Click "🔍 **Analyze**" button
3. View results in the AI Analysis panel:
   - **Quality**: Overall code quality score
   - **Suggestions**: Improvements and refactoring tips
   - **Security**: Vulnerability detection
   - **Explain**: AI explanation of your code

### Real-Time Collaboration

- Code changes sync automatically to all users
- See who's editing in the "Active Users" panel
- Session persists across page reloads

## 🔌 API Endpoints

### REST API

```
POST /api/session/create
- Create a new collaborative session
- Body: { title, code, language }

GET /api/session/<session_id>
- Get session details and current code

POST /api/analyze
- Analyze code quality
- Body: { code, language }

POST /api/explain
- Get AI explanation of code
- Body: { code }

POST /api/refactor
- Get refactoring suggestions
- Body: { code, language }

GET /api/sessions
- List all active sessions
```

### WebSocket Events

```
join_session
- User joins a collaborative session
- Data: { session_id, username }

code_change
- Broadcast code changes to all users
- Data: { session_id, user_id, code }

request_analysis
- Request code analysis from ACE
- Data: { session_id, code, language }

request_explanation
- Request AI explanation
- Data: { session_id, code }

cursor_position
- Share cursor position with other users
- Data: { session_id, user_id, username, line, column }
```

## 🧠 ACE Framework Integration

### CodeQualityEnvironment

Evaluates code across multiple dimensions:

- **Complexity**: Function length, code size
- **Security**: Dangerous functions, imports
- **Best Practices**: Docstrings, code style
- **Performance**: Loop optimization, builtin usage

### CodeSuggestionAgent

Uses Groq's LLM to:

- Generate intelligent improvement suggestions
- Identify refactoring opportunities
- Provide code explanations
- Learn from user interactions (future)

## ⚙️ Configuration

### Change Port

Edit `code_editor_app.py` line ~415:

```python
socketio.run(app, host='127.0.0.1', port=5001, debug=True)
```

### Change Model

Edit `code_editor_app.py` line ~17:

```python
MODEL = "groq/llama-3.3-70b-versatile"  # Change to your model
```

### Environment Variables

```bash
GROQ_API_KEY=your_api_key_here
FLASK_ENV=development  # or production
```

## 🎨 UI Features

- **Glassmorphism Design**: Modern frosted glass effect
- **Dark Theme**: Eye-friendly dark mode
- **Responsive Layout**: Works on desktop and tablet
- **Real-time Sync**: Smooth, instant updates
- **Accessibility**: Keyboard shortcuts and screen reader support

## 📊 Analysis Dashboard

The AI Analysis panel provides:

1. **Quality Score** (0-100)

   - Visual progress indicator
   - Quality metrics

2. **Issues Tab**

   - Code quality problems
   - Best practice violations

3. **Suggestions Tab**

   - Specific improvements
   - Refactoring opportunities

4. **Security Tab**

   - Vulnerability detection
   - Risk assessment

5. **Explanation Tab**
   - What the code does
   - Function descriptions

## 🔐 Security Features

- **XSS Protection**: Sanitized code display
- **CORS Configuration**: Configurable allowed origins
- **API Validation**: Input validation on all endpoints
- **Session Security**: Unique session IDs
- **Security Analysis**: Built-in code vulnerability detection

## 🚨 Limitations

- Local in-memory storage (data lost on restart)
- File uploads not yet supported
- Limited to 10KB code snippets (configurable)
- Single Groq API key (authentication per instance)

## 📈 Future Enhancements

- [ ] Database persistence (PostgreSQL/MongoDB)
- [ ] User authentication and authorization
- [ ] GitHub integration
- [ ] Code diff visualization
- [ ] Performance profiling
- [ ] Custom code analysis rules
- [ ] Export/download code and analysis
- [ ] Chat between collaborators
- [ ] Version control integration
- [ ] Mobile app support

## 🐛 Troubleshooting

### ModuleNotFoundError

```bash
pip install -r requirements.txt
```

### Port 5001 Already in Use

```bash
# Change port in code_editor_app.py
# Or kill process: netstat -ano | findstr :5001
```

### Groq API Errors

- Verify API key is set: `$env:GROQ_API_KEY`
- Check rate limits (free tier: 12,000 TPM)
- Ensure internet connection

### WebSocket Connection Issues

- Clear browser cache
- Disable browser extensions
- Check firewall settings

## 📚 Dependencies

- **Flask** 3.0.0 - Web framework
- **Flask-SocketIO** 5.3.0 - Real-time communication
- **ace-framework** 0.7.1 - AI agent framework
- **litellm** 1.80.11 - LLM unified API
- **groq** 1.0.0 - Groq API client
- **python-dotenv** 1.0.0 - Environment variables

## 📄 License

MIT License - Open source and free to use

## 🤝 Contributing

Contributions welcome! Please submit issues and pull requests.

## 📞 Support

- **Documentation**: See inline code comments
- **Issues**: Create GitHub issues
- **Email**: your-email@example.com

---

**Built with ❤️ using ACE Framework + Flask + Socket.IO**

🚀 **Happy Collaborative Coding!**
