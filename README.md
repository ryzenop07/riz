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
- 🔍 **Multi-Platform Support** - YouTube, Spotify, SoundCloud, and more
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
python -m Tune
```

## ⚙️ Configuration

Edit `config.py` with your credentials:

```python
API_ID = 12345678
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
MONGO_DB_URI = "your_mongodb_uri"
OWNER_ID = [your_user_id]
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

### 👮‍♂️ Admin Commands
- `/settings` - Bot settings
- `/auth` - Authorize users
- `/unauth` - Unauthorize users
- `/reload` - Reload bot

## 🎨 Customization

### Adding Custom Fonts
Place your fonts in `assets/fonts/` directory.

### Adding Custom Images
Place your images in `assets/images/` directory.

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

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=RyzenMusic/RyzenMusic&type=Date)](https://star-history.com/#RyzenMusic/RyzenMusic&Date)

---

<p align="center">
  <b>Made with ❤️ by Ryzen Music Team</b>
</p>