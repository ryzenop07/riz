# 🚀 VPS Deployment Guide - Ryzen Music Bot

## 📋 Prerequisites

- Ubuntu 20.04+ VPS
- Root access
- 1GB+ RAM
- Python 3.11+

## ⚡ Quick Start (Recommended)

```bash
# Clone repository
git clone https://github.com/RyzenMusic/RyzenMusic
cd RyzenMusic

# Configure bot
cp .env.example .env
nano .env

# Start bot
bash start
```

## 🛠️ Manual Installation

### 1. Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install Dependencies
```bash
sudo apt install -y python3.11 python3.11-pip python3.11-venv git ffmpeg
```

### 3. Clone Repository
```bash
git clone https://github.com/RyzenMusic/RyzenMusic
cd RyzenMusic
```

### 4. Configure Bot
```bash
cp .env.example .env
nano .env
```

Add your credentials:
```env
API_ID=12345678
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_DB_URI=your_mongodb_uri
STRING1=your_session_string
OWNER_ID=your_user_id
```

### 5. Start Bot
```bash
bash start
```

## 🔄 Systemd Service (Auto-restart)

### Create Service
```bash
sudo nano /etc/systemd/system/ryzenmusic.service
```

```ini
[Unit]
Description=Ryzen Music Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/RyzenMusic
ExecStart=/bin/bash /root/RyzenMusic/start
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

### Enable Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable ryzenmusic
sudo systemctl start ryzenmusic
```

## 📊 Management Commands

```bash
# Start bot manually
bash start

# Check service status
sudo systemctl status ryzenmusic

# View logs
sudo journalctl -u ryzenmusic -f

# Restart service
sudo systemctl restart ryzenmusic

# Stop service
sudo systemctl stop ryzenmusic

# Update bot
git pull && sudo systemctl restart ryzenmusic
```

## 🔧 Performance Optimization

### 1. Increase File Limits
```bash
echo "* soft nofile 65536" >> /etc/security/limits.conf
echo "* hard nofile 65536" >> /etc/security/limits.conf
```

### 2. Optimize Network
```bash
echo "net.core.rmem_max = 134217728" >> /etc/sysctl.conf
echo "net.core.wmem_max = 134217728" >> /etc/sysctl.conf
sysctl -p
```

## 🐳 Docker Deployment

```bash
# Build image
docker build -t ryzenmusic .

# Run container
docker run -d --name ryzenmusic --restart unless-stopped ryzenmusic
```

## 🔒 Security Setup

### 1. Setup Firewall
```bash
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
```

### 2. Fail2Ban
```bash
sudo apt install fail2ban -y
sudo systemctl enable fail2ban
```

## 🆘 Troubleshooting

### Common Issues:

**Virtual environment not found:**
```bash
cd RyzenMusic
python3 -m venv venv
bash start
```

**Permission denied:**
```bash
chmod +x start
sudo chown -R $USER:$USER /path/to/RyzenMusic
```

**Python not found:**
```bash
sudo apt install python3.11 python3.11-pip python3.11-venv
```

**Dependencies error:**
```bash
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 📈 Monitoring

### Check bot process
```bash
ps aux | grep python
```

### Monitor logs
```bash
tail -f logs.txt
```

### System resources
```bash
htop
free -h
df -h
```

## 🔄 Auto-Update Script

Create `/root/update-bot.sh`:
```bash
#!/bin/bash
cd /root/RyzenMusic
git pull
sudo systemctl restart ryzenmusic
echo "Bot updated successfully!"
```

Make executable:
```bash
chmod +x /root/update-bot.sh
```

Add to crontab for daily updates:
```bash
crontab -e
# Add: 0 2 * * * /root/update-bot.sh
```

## 💡 Tips

- Use `screen` or `tmux` for manual runs
- Monitor RAM usage regularly
- Keep system updated
- Backup configuration files
- Use SSD for better performance

## 🎵 Expected Output

When you run `bash start`, you should see:
```
🎵 Starting Ryzen Music Bot...
==============================
📦 Creating virtual environment...
📥 Installing dependencies...
🚀 Starting Ryzen Music Bot...
[01-Oct-25 04:03:26 - INFO] - Tune.core.mongo - Connecting to your Mongo Database...
[01-Oct-25 04:03:26 - INFO] - Tune.core.mongo - Connected to your Mongo Database.
[01-Oct-25 04:03:26 - INFO] - Tune.core.dir - Directories Updated.
[01-Oct-25 04:03:26 - INFO] - Tune.core.git - Git Client Found [VPS DEPLOYER]
[01-Oct-25 04:03:26 - INFO] - Tune.misc - ᴅᴀᴛᴀʙᴀsᴇ ʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ💗
[01-Oct-25 04:03:26 - INFO] - Tune.core.bot - Bot client initialized.
[01-Oct-25 04:03:26 - INFO] - Tune - 🎵 Ryzen Music Bot Started Successfully! 🎵
```

## 🎯 Ready!

Your Ryzen Music bot is now running with `bash start` command!