#!/usr/bin/env pwsh
# Quick Deploy Script for Collaborative Code Editor

Write-Host "🚀 COLLABORATIVE CODE EDITOR - QUICK DEPLOY" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

# Check if .venv exists
if (-not (Test-Path ".venv")) {
  Write-Host "❌ Virtual environment not found. Creating..." -ForegroundColor Yellow
  python -m venv .venv
}

# Activate virtual environment
Write-Host "✅ Activating virtual environment..." -ForegroundColor Green
. .\.venv\Scripts\Activate.ps1

# Install/Update dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Green
pip install -r requirements.txt

# Check if GROQ_API_KEY is set
if (-not $env:GROQ_API_KEY) {
  Write-Host "⚠️  GROQ_API_KEY not set!" -ForegroundColor Yellow
  Write-Host "   Please set it with: `$env:GROQ_API_KEY = 'your-key'" -ForegroundColor Yellow
  $apiKey = Read-Host "Enter your Groq API key (or press Enter to skip)"
  if ($apiKey) {
    $env:GROQ_API_KEY = $apiKey
  }
}

Write-Host ""
Write-Host "🎯 Choose deployment option:" -ForegroundColor Cyan
Write-Host "1. Local Development (localhost:5001)" -ForegroundColor White
Write-Host "2. Local Production (with Gunicorn)" -ForegroundColor White
Write-Host "3. Docker Build" -ForegroundColor White
Write-Host "4. Docker Compose" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Enter choice (1-4)"

switch ($choice) {
  "1" {
    Write-Host ""
    Write-Host "🚀 Starting LOCAL DEVELOPMENT server..." -ForegroundColor Green
    Write-Host "   URL: http://localhost:5001" -ForegroundColor Cyan
    Write-Host "   Press Ctrl+C to stop" -ForegroundColor Yellow
    Write-Host ""
    python code_editor_app.py
  }
  "2" {
    Write-Host ""
    Write-Host "🚀 Starting LOCAL PRODUCTION server..." -ForegroundColor Green
    $env:FLASK_ENV = "production"
    Write-Host "   URL: http://0.0.0.0:5001" -ForegroundColor Cyan
    Write-Host "   Press Ctrl+C to stop" -ForegroundColor Yellow
    Write-Host ""
    gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:5001 code_editor_app:app
  }
  "3" {
    Write-Host ""
    Write-Host "🐳 Building Docker image..." -ForegroundColor Green
    docker build -t collaborative-code-editor .
    Write-Host ""
    Write-Host "✅ Docker image built successfully!" -ForegroundColor Green
    Write-Host "   Run with: docker run -p 5001:5001 -e GROQ_API_KEY='your-key' collaborative-code-editor" -ForegroundColor Cyan
  }
  "4" {
    Write-Host ""
    Write-Host "🐳 Starting with Docker Compose..." -ForegroundColor Green
    docker-compose up -d
    Write-Host ""
    Write-Host "✅ Application started!" -ForegroundColor Green
    Write-Host "   URL: http://localhost:5001" -ForegroundColor Cyan
    Write-Host "   Logs: docker-compose logs -f" -ForegroundColor Yellow
    Write-Host "   Stop: docker-compose down" -ForegroundColor Yellow
  }
  default {
    Write-Host "❌ Invalid choice. Exiting." -ForegroundColor Red
    exit 1
  }
}

Write-Host ""
Write-Host "✨ Deployment script complete!" -ForegroundColor Green
