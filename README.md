# 🎵 Ryzen Music Bot

<p align="center">
  <img src="https://te.legra.ph/file/c0e014ff34f34d1056627.png" alt="Ryzen Music" width="200"/>
</p>

<h1 align="center">
  <b>⚡ Ultra-Fast Telegram Music Bot ⚡</b>
</h1>

<p align="center">
  <b>🚀 Nanosecond Response Time | 🎵 High-Quality Streaming | 🔥 Advanced Features</b>
</p>

---

## 🌟 Features

- ⚡ **Ultra-Fast Performance** - Nanosecond response time
- 🎵 **High-Quality Audio/Video** - Crystal clear streaming
- 🔍 **Multi-Platform Support** - YouTube, Spotify, SoundCloud
- 📱 **Advanced Queue Management** - Smart playlist handling
- 🎛️ **Admin Controls** - Complete music control
- 🌐 **Multi-Language Support** - Available in multiple languages
- 🔒 **Secure & Reliable** - Built with security in mind

## 🚀 Quick Deploy

### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/RyzenMusic/RyzenMusic)

### Deploy on Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/ryzen-music)

## 📋 Requirements

- Python 3.11+
- MongoDB Database
- Telegram API ID & Hash
- Bot Token from @BotFather

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/RyzenMusic/RyzenMusic
cd RyzenMusic
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables:**
```bash
cp .env.example .env
# Edit .env with your credentials
```

4. **Run the bot:**
```bash
python main.py
```

## ⚙️ Configuration

Edit `.env` file with your credentials:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_DB_URI=your_mongodb_uri
OWNER_ID=your_user_id
STRING_SESSION=your_pyrogram_session
```

## 📝 Commands

### 🎵 Music Commands
- `/play` - Play a song
- `/vplay` - Play video
- `/pause` - Pause current track
- `/resume` - Resume paused track
- `/skip` - Skip current song
- `/stop` - Stop music and clear queue
- `/queue` - Show current queue

### 👮♂️ Admin Commands
- `/settings` - Bot settings
- `/broadcast` - Send broadcast message
- `/stats` - Bot statistics

## 🏗️ Project Structure

```
RyzenMusic/
├── Tune/                 # Main package
│   ├── core/            # Core functionality
│   ├── plugins/         # Command handlers
│   ├── platforms/       # Platform integrations
│   └── utils/           # Utility functions
├── assets/              # Static resources
├── scripts/             # Deployment scripts
├── main.py             # Entry point
└── config.py           # Configuration
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the GNU AGPL v3.0 License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Telegram:** [@RyzenMusicSupport](https://t.me/RyzenMusicSupport)
- **Channel:** [@RyzenMusicChannel](https://t.me/RyzenMusicChannel)

---

<p align="center">
  <b>Made with ❤️ by Ryzen Music Team</b>
</p>