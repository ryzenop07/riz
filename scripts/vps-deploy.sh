#!/bin/bash

# Ryzen Music Bot - VPS Deployment Script

echo "🎵 Ryzen Music Bot - VPS Deployment"
echo "=================================="

# Update system
echo "📦 Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install Python and pip
echo "🐍 Installing Python 3.11..."
sudo apt install python3.11 python3.11-pip python3.11-venv -y

# Install FFmpeg
echo "🎬 Installing FFmpeg..."
sudo apt install ffmpeg -y

# Create virtual environment
echo "📁 Creating virtual environment..."
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Create systemd service
echo "⚙️ Creating systemd service..."
sudo tee /etc/systemd/system/ryzenmusic.service > /dev/null <<EOF
[Unit]
Description=Ryzen Music Bot
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$(pwd)
ExecStart=$(pwd)/venv/bin/python main.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable ryzenmusic
sudo systemctl start ryzenmusic

echo "✅ Deployment completed!"
echo "🔍 Check status: sudo systemctl status ryzenmusic"
echo "📋 View logs: sudo journalctl -u ryzenmusic -f"