from code_editor_app import app
import os


# Vercel serverless function entry point
def handler(request, response):
    return app(request, response)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
