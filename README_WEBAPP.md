# 🎨 Content Generator Web App - ACE Framework

A production-ready web application for self-learning content generation powered by the ACE Framework.

## 🚀 Quick Start

### 1. Install Flask

```bash
pip install flask flask-cors
```

### 2. Set Your API Key

```powershell
$env:GROQ_API_KEY = "your-groq-api-key-here"
```

### 3. Run the App

```bash
python app.py
```

### 4. Open in Browser

```
http://localhost:5000
```

## ✨ Features

### 📝 Content Generation

- **Blog Posts** - Long-form, well-structured articles
- **Social Media** - Engaging posts with CTAs
- **Product Descriptions** - Feature/benefit focused
- **Email Campaigns** - Compelling marketing emails
- **Video Scripts** - Engaging video content

### 🧠 Self-Learning

- Rate generated content (1-10 stars)
- Provide feedback for AI improvement
- Agent learns from every interaction
- Save trained models for production

### 📊 Analytics

- Track total generations
- Monitor average quality ratings
- View usage by content type
- Complete generation history

### 💾 Model Management

- Save trained skillbooks
- Load previous models
- Export for production deployment

## 🎯 How to Use

### Generate Content

1. Select **Content Type** (Blog, Social, etc.)
2. Enter your **Prompt/Topic**
3. Click **Generate**
4. Review the generated content

### Train the AI

1. **Rate** the content (1-10 stars)
2. Provide **Feedback** (optional)
3. Click **Submit Feedback**
4. Agent learns and improves!

### Save Your Model

- Click **Save Model** to save trained strategies
- Use `content_generator_production.json` for deployment

## 🛠️ Architecture

```
Content Generator Web App
├── Backend (Flask)
│   ├── /api/generate - Create content
│   ├── /api/feedback - Rate & learn
│   ├── /api/history - View past generations
│   ├── /api/stats - Get analytics
│   └── /api/save-model - Save trained model
│
├── Frontend (HTML/CSS/JS)
│   ├── Content generation interface
│   ├── Rating system
│   ├── Statistics dashboard
│   └── Generation history
│
└── ACE Engine
    ├── Agent - Generates content
    ├── Reflector - Analyzes quality
    └── SkillManager - Updates strategies
```

## 📊 API Endpoints

### POST `/api/generate`

Generate new content

```json
{
  "prompt": "Write a blog about AI",
  "content_type": "blog"
}
```

### POST `/api/feedback`

Submit quality feedback

```json
{
  "entry_id": 1,
  "rating": 8,
  "feedback": "Great! Add more examples"
}
```

### GET `/api/history`

Get generation history

### GET `/api/stats`

Get usage statistics

### POST `/api/save-model`

Save trained model

## 🔧 Configuration

### Modify Content Types

Edit `CONTENT_TYPES` in `app.py`:

```python
CONTENT_TYPES = {
    "custom": {
        "name": "Custom Type",
        "template": "Your custom prompt template..."
    }
}
```

### Change Model

Modify the model in `app.py`:

```python
generator = ACELiteLLM(model="groq/llama-3.3-70b-versatile")
```

### Adjust Settings

- `MAX_CONTENT_LENGTH` - Max request size
- `DEBUG` - Enable/disable debug mode
- `HOST/PORT` - Server configuration

## 📈 Performance Tips

1. **Use Groq Dev Tier** for higher rate limits
2. **Batch feedback** to improve learning efficiency
3. **Save models regularly** for backup
4. **Monitor stats** to track improvement

## 🐛 Troubleshooting

### Rate Limit Errors

- Upgrade to Groq Dev Tier: https://console.groq.com/settings/billing

### API Key Not Working

- Verify key: `$env:GROQ_API_KEY`
- Check Groq console for usage

### Port Already in Use

```powershell
python app.py # Uses port 5000
# Or change port in app.py: app.run(port=5001)
```

## 🚀 Deployment

### Local Network Access

```python
app.run(host='0.0.0.0', port=5000)
```

### Production Deployment

Use a production WSGI server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker (Optional)

```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV GROQ_API_KEY=your_key
CMD ["python", "app.py"]
```

## 📚 Learning Resources

- [ACE Framework Documentation](https://github.com/your-repo)
- [Groq API Docs](https://console.groq.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com)

## 🤝 Support

- Check logs for detailed error messages
- Verify API key and rate limits
- Test with simple prompts first
- Monitor generation stats

## 📝 Example Workflows

### Blog Writing Workflow

```
1. Select "Blog Post" type
2. Enter topic: "Sustainable Living in 2025"
3. Generate content
4. Rate quality (8/10)
5. Feedback: "Add climate statistics"
6. Submit - AI learns!
7. Generate again - content improves
```

### Product Launch Workflow

```
1. Select "Email Campaign"
2. Prompt: "New fitness app launch"
3. Generate marketing email
4. Rate and provide feedback
5. Generate for social media variant
6. Collect all feedback
7. Save final model for launch
```

## 🎊 You're Ready!

Your Content Generator is production-ready. Start generating amazing content with AI that learns and improves over time!

Happy Creating! 🚀
