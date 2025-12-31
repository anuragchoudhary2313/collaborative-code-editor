# 🚀 Collaborative Code Editor with ACE Framework

A real-time collaborative code editor powered by AI, built with Flask, Socket.IO, and the ACE Framework.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1.2-green.svg)

## ✨ Features

- 🤝 **Real-time Collaboration** - Multiple users can edit code simultaneously
- 🤖 **AI Code Analysis** - Powered by ACE Framework and Groq LLM
- 🔍 **Quality Scoring** - Automatic code quality assessment (0-100 scale)
- 🛡️ **Security Scanner** - Detects vulnerabilities and dangerous functions
- ⚡ **Performance Tips** - AI-powered optimization suggestions
- 📚 **Code Explanations** - Understands and explains your code
- 🎨 **Beautiful UI** - Modern glassmorphism design with dark theme
- 🌐 **7 Languages** - JavaScript, Python, Java, C++, HTML, CSS, SQL

## 🌐 Live Deployment

- **App (Render):** https://collaborative-code-editor-jklj.onrender.com/
- **Repository:** https://github.com/anuragchoudhary2313/collaborative-code-editor

> Render free tier sleeps after inactivity; first hit may take 30–60 seconds to wake.

![Collaborative Code Editor Demo](https://via.placeholder.com/800x400?text=Collaborative+Code+Editor)

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Groq API Key (free at [groq.com](https://groq.com))

### Installation

```bash
# Clone the repository
git clone https://github.com/anuragchoudhary2313/collaborative-code-editor.git
cd collaborative-code-editor
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate      # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Set API key
$env:GROQ_API_KEY = 'your-groq-api-key'  # Windows
export GROQ_API_KEY='your-groq-api-key'  # Linux/Mac

# Run the application
python code_editor_app.py
```

Open **http://localhost:5001** in your browser!

## 🐳 Docker Deployment

```bash
# Build image
docker build -t collaborative-code-editor .

# Run container
docker run -d -p 5001:5001 \
  -e GROQ_API_KEY='your-api-key' \
  --name code-editor \
  collaborative-code-editor

# Access at http://localhost:5001
```

## ☁️ Cloud Deployment (Render)

Already deployed for you:

- 🌐 Live: https://collaborative-code-editor-jklj.onrender.com/

Redeploy on your own Render account (free tier):

1. Go to [render.com](https://render.com) → New → Web Service
2. Connect GitHub repo `anuragchoudhary2313/collaborative-code-editor`
3. Runtime: **Python 3** (or Docker auto-detected)
4. Build: `pip install -r requirements.txt`
5. Start: `gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:$PORT code_editor_app:app`
6. Env var: `GROQ_API_KEY=your-groq-api-key`
7. Deploy (first boot may take ~3-5 minutes)

Note: Free tier sleeps after 15 minutes idle; first hit wakes the app (30–60 seconds).

Or use Docker Compose:

```bash
docker-compose up -d
```

## ☁️ Cloud Deployment

Deploy to Railway (FREE):

1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "Deploy from GitHub"
4. Add environment variable: `GROQ_API_KEY`
5. Your app is live! 🎉

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for more platforms (Heroku, AWS, etc.)

## 📖 How to Use

1. **Create Session** - Click "+ New Session"
2. **Write Code** - Start coding in your favorite language
3. **Analyze** - Click "🔍 Analyze" for AI insights
4. **Collaborate** - Share session with team members
5. **Learn** - Implement AI suggestions to improve code

## 🏗️ Architecture

```
Frontend (HTML/CSS/JS)
    ↓ WebSocket & REST API
Flask Backend
    ↓ ACE Framework
Groq LLM (AI Analysis)
```

## 🛠️ Technologies

- **Backend**: Flask 3.1.2, Flask-SocketIO 5.6.0
- **Frontend**: HTML5, CSS3 (Glassmorphism), Vanilla JavaScript
- **AI**: ACE Framework 0.7.1, Groq LLM (llama-3.3-70b-versatile)
- **Real-time**: Socket.IO 4.5.4
- **Production**: Gunicorn, Eventlet

## 📁 Project Structure

```
collaborative-code-editor/
├── code_editor_app.py          # Main Flask application
├── templates/
│   └── code_editor.html        # Frontend UI
├── Dockerfile                   # Docker configuration
├── docker-compose.yml          # Docker Compose setup
├── requirements.txt            # Python dependencies
├── Procfile                    # Heroku/Railway config
├── railway.json                # Railway configuration
└── README.md                   # This file
```

## 🤖 AI Analysis Features

### Quality Scoring

- Code complexity analysis
- Best practices evaluation
- Documentation completeness
- Style compliance

### Security Scanning

- Dangerous function detection (eval, exec, etc.)
- SQL injection risks
- Code injection vulnerabilities
- Import statement validation

### Performance Optimization

- Loop optimization suggestions
- Algorithm efficiency tips
- Resource usage recommendations
- Built-in function suggestions

## 🌟 Screenshots

### Main Editor

![Main Editor](https://via.placeholder.com/600x400?text=Main+Editor)

### AI Analysis Dashboard

![Analysis Dashboard](https://via.placeholder.com/600x400?text=AI+Analysis)

### Real-time Collaboration

![Collaboration](https://via.placeholder.com/600x400?text=Real-time+Sync)

## 🚧 Roadmap

- [ ] File upload/download
- [ ] GitHub integration
- [ ] Database persistence (PostgreSQL)
- [ ] User authentication
- [ ] Code diff visualization
- [ ] Custom analysis rules
- [ ] Mobile app support
- [ ] VS Code extension

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [ACE Framework](https://github.com/ace-framework) - AI agent framework
- [Groq](https://groq.com) - Lightning-fast AI inference
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Socket.IO](https://socket.io/) - Real-time communication

## 📞 Support

- 🐛 Issues: [GitHub Issues](https://github.com/anuragchoudhary2313/collaborative-code-editor/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/anuragchoudhary2313/collaborative-code-editor/discussions)

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=anuragchoudhary2313/collaborative-code-editor&type=Date)](https://star-history.com/#anuragchoudhary2313/collaborative-code-editor&Date)

---

**Built with ❤️ using ACE Framework + Flask + Socket.IO**

🚀 **Happy Collaborative Coding!**
