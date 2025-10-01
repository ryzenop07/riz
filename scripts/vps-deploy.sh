#!/bin/bash

# Ryzen Music Bot - Auto VPS Deploy Script
set -e

echo "🎵 Ryzen Music Bot - VPS Auto Deploy"
echo "======================================"

# Update system
echo "📦 Updating system..."
apt update && apt upgrade -y

# Install dependencies
echo "🔧 Installing dependencies..."
apt install -y python3.11 python3.11-pip python3.11-venv git ffmpeg curl wget

# Clone repository
echo "📥 Cloning repository..."
cd /root
git clone https://github.com/RyzenMusic/RyzenMusic
cd RyzenMusic

# Setup virtual environment
echo "🐍 Setting up Python environment..."
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create environment file
echo "⚙️ Creating configuration..."
cp .env.example .env

# Create systemd service
echo "🚀 Creating system service..."
cat > /etc/systemd/system/ryzenmusic.service << EOF
[Unit]
Description=Ryzen Music Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/RyzenMusic
ExecStart=/root/RyzenMusic/venv/bin/python -m Tune
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

# Enable service
systemctl daemon-reload
systemctl enable ryzenmusic

# Performance optimization
echo "⚡ Optimizing performance..."
echo "* soft nofile 65536" >> /etc/security/limits.conf
echo "* hard nofile 65536" >> /etc/security/limits.conf

# Setup firewall
echo "🔒 Configuring firewall..."
ufw --force enable
ufw allow ssh

echo ""
echo "✅ Installation Complete!"
echo ""
echo "📝 Next Steps:"
echo "1. Edit /root/RyzenMusic/.env with your bot credentials"
echo "2. Run: systemctl start ryzenmusic"
echo "3. Check status: systemctl status ryzenmusic"
echo ""
echo "🎵 Your Ryzen Music Bot is ready!"