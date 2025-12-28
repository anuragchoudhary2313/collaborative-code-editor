# Docker Hub Deployment Complete! 🎉

## Published Images

Your collaborative code editor is now available on Docker Hub:

- **Repository**: https://hub.docker.com/r/anurag2313/collaborative-code-editor
- **Latest tag**: `anurag2313/collaborative-code-editor:latest`
- **Version tag**: `anurag2313/collaborative-code-editor:v1`
- **Digest**: `sha256:3d0f3dee87c3220329e9d20faf8b693b2e8b130ce9a0cbb469852b025d71cdda`

## Pull & Run Anywhere

Anyone can now run your app with a single command:

```bash
# Pull and run the latest version
docker pull anurag2313/collaborative-code-editor:latest
docker run -d -p 5001:5001 \
  -e GROQ_API_KEY="your-groq-api-key-here" \
  --name code-editor \
  anurag2313/collaborative-code-editor:latest

# Or run specific version
docker run -d -p 5001:5001 \
  -e GROQ_API_KEY="your-groq-api-key-here" \
  --name code-editor \
  anurag2313/collaborative-code-editor:v1
```

## Automated Builds from GitHub

Set up automated builds so Docker Hub rebuilds your image whenever you push to GitHub:

### Step 1: Link GitHub Account

1. Go to https://hub.docker.com
2. Click your username → Account Settings → Linked Accounts
3. Click "Link GitHub"
4. Authorize Docker Hub to access your GitHub

### Step 2: Configure Automated Build

1. Go to https://hub.docker.com/r/anurag2313/collaborative-code-editor
2. Click "Builds" tab
3. Click "Configure Automated Builds"
4. Select your GitHub repository: `anuragchoudhary2313/collaborative-code-editor`
5. Configure build rules:

   - **Source**: `main` branch
   - **Docker Tag**: `latest`
   - **Dockerfile location**: `/Dockerfile`
   - **Build Context**: `/`

6. Add version tag rule:

   - **Source Type**: Tag
   - **Source**: `/^v[0-9.]+$/` (regex for version tags)
   - **Docker Tag**: `{sourceref}`
   - **Dockerfile location**: `/Dockerfile`

7. Click "Save and Build"

### Step 3: Test Automated Build

```bash
# Push a new tag to GitHub
git tag v1.0.1
git push origin v1.0.1
```

Docker Hub will automatically:

- Detect the push
- Build the image
- Tag it as `anurag2313/collaborative-code-editor:v1.0.1`
- Update `latest` tag

## Cloud Deployment Options

Now that your image is on Docker Hub, deploy anywhere:

### AWS EC2

```bash
# SSH into EC2 instance
docker pull anurag2313/collaborative-code-editor:latest
docker run -d -p 80:5001 \
  -e GROQ_API_KEY="your-key" \
  --restart unless-stopped \
  anurag2313/collaborative-code-editor:latest
```

### Railway

1. Go to https://railway.app
2. New Project → Deploy Docker Image
3. Enter: `anurag2313/collaborative-code-editor:latest`
4. Add environment variable: `GROQ_API_KEY`
5. Deploy! (Railway generates public URL automatically)

### Render

1. Go to https://render.com
2. New → Web Service → Docker
3. Image URL: `docker.io/anurag2313/collaborative-code-editor:latest`
4. Add environment variable: `GROQ_API_KEY`
5. Deploy! (Free tier with auto-sleep)

### DigitalOcean App Platform

1. Go to https://cloud.digitalocean.com/apps
2. Create App → Docker Hub
3. Repository: `anurag2313/collaborative-code-editor:latest`
4. Add environment variable: `GROQ_API_KEY`
5. Deploy! ($5/month)

### Azure Container Instances

```bash
az container create \
  --resource-group myResourceGroup \
  --name code-editor \
  --image anurag2313/collaborative-code-editor:latest \
  --dns-name-label code-editor-app \
  --ports 5001 \
  --environment-variables GROQ_API_KEY="your-key"
```

### Google Cloud Run

```bash
gcloud run deploy code-editor \
  --image docker.io/anurag2313/collaborative-code-editor:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GROQ_API_KEY="your-key"
```

## Update Workflow

When you make changes to your code:

```bash
# 1. Update code locally
# 2. Rebuild Docker image
docker build -t anurag2313/collaborative-code-editor:latest .

# 3. Tag new version
docker tag anurag2313/collaborative-code-editor:latest anurag2313/collaborative-code-editor:v1.0.1

# 4. Push both tags
docker push anurag2313/collaborative-code-editor:latest
docker push anurag2313/collaborative-code-editor:v1.0.1

# 5. Or use automated builds (push to GitHub and Docker Hub builds automatically)
git add .
git commit -m "Update feature"
git tag v1.0.1
git push origin main --tags
```

## Share Your App

Anyone can now use your collaborative code editor:

**Docker Hub**: https://hub.docker.com/r/anurag2313/collaborative-code-editor
**GitHub**: https://github.com/anuragchoudhary2313/collaborative-code-editor
**One-line install**:

```bash
docker run -d -p 5001:5001 -e GROQ_API_KEY="key" anurag2313/collaborative-code-editor:latest
```

## Next Steps

1. ✅ Image pushed to Docker Hub (latest & v1)
2. ⏳ Set up automated builds (optional, recommended)
3. ⏳ Deploy to cloud platform (Railway, Render, AWS, etc.)
4. ⏳ Add CI/CD pipeline with GitHub Actions
5. ⏳ Monitor usage on Docker Hub

Congratulations! Your app is now globally accessible via Docker Hub! 🚀
