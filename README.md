# Church Live Streaming System

A WebRTC-based live streaming system for church services with broadcaster and viewer interfaces.

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python app.py
   ```

3. Open in browser:
   - **Broadcaster**: `http://127.0.0.1:5000/media-panel/go-live`
   - **Viewer**: `http://127.0.0.1:5000/live`
   - **Dashboard**: `http://127.0.0.1:5000/`

## Production Deployment Options

### Option 1: Heroku (Recommended)
1. Create a Heroku account
2. Install Heroku CLI
3. Create a new app:
   ```bash
   heroku create your-church-live-stream
   ```
4. Deploy:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a your-church-live-stream
   git push heroku main
   ```

### Option 2: Railway
1. Go to [Railway.app](https://railway.app)
2. Connect your GitHub repository
3. Deploy automatically

### Option 3: DigitalOcean App Platform
1. Create a DigitalOcean account
2. Use App Platform to deploy from GitHub

### Option 4: VPS (Advanced)
Deploy to a VPS with Nginx reverse proxy and SSL certificate.

## Features

- **WebRTC Streaming**: Real-time video streaming between broadcaster and viewers
- **Live Chat**: Interactive chat system
- **Status Monitoring**: Live viewer count and stream duration
- **Mobile Responsive**: Works on all devices
- **HTTPS Ready**: Secure streaming for production

## CORS Issues

If you encounter CORS errors when accessing from different domains:
- For local development: Use `http://127.0.0.1:5000` URLs
- For production: Deploy to a proper hosting service with HTTPS

## Browser Support

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support
- Mobile browsers: Full support

## Security Notes

- Camera/microphone permissions required for broadcasting
- HTTPS recommended for production
- Consider authentication for broadcaster access in production