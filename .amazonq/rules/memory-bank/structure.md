# Ryzen Music Bot - Project Structure

## Directory Organization

### Root Level Structure
```
RyzenMusic/
├── assets/          # Static resources (fonts, images)
├── cookies/         # Platform authentication cookies
├── core/            # Core bot functionality
├── platforms/       # Platform-specific integrations
├── plugins/         # Bot command handlers
├── scripts/         # Utility and deployment scripts
├── strings/         # Localization files
├── Tune/            # Core framework components
├── utils/           # Utility functions and helpers
└── config.py        # Main configuration file
```

## Core Components

### `/core/` - Bot Core Functionality
- **call.py**: Voice call management and audio streaming logic
- Handles Telegram voice chat integration
- Manages audio/video streaming sessions

### `/platforms/` - External Service Integration
- **youtube.py**: YouTube platform integration and video/audio extraction
- **spotify.py**: Spotify API integration for track metadata and streaming
- Abstracted platform interfaces for extensibility

### `/plugins/` - Command Handlers
- **start.py**: Bot initialization and welcome commands
- **play.py**: Music playback commands and queue management
- **admins.py**: Administrative commands and user management
- **broadcast.py**: Message broadcasting functionality
- **lyrics.py**: Lyrics fetching and display

### `/Tune/` - Framework Core
- **core/bot.py**: Main bot instance and Pyrogram client setup
- **core/mongo.py**: MongoDB database connection and operations
- **core/git.py**: Git integration for updates and version control
- **core/dir.py**: Directory and file management utilities
- **logging.py**: Centralized logging system
- **misc.py**: Miscellaneous utility functions

### `/utils/` - Utility Layer
- **database.py**: Database abstraction and query helpers
- **cookies.py**: Cookie management for platform authentication
- **decorators.py**: Custom decorators for command handling
- **inline/play.py**: Inline keyboard handlers for music controls
- **stream/stream.py**: Audio/video streaming utilities

## Architectural Patterns

### Modular Plugin Architecture
- Command handlers separated into individual plugin files
- Each plugin handles specific functionality domains
- Centralized registration and management system

### Platform Abstraction Layer
- Unified interface for different music platforms
- Extensible design for adding new streaming services
- Consistent API across all platform integrations

### Database Abstraction
- MongoDB integration with connection pooling
- Centralized database operations in utils/database.py
- Async/await pattern for non-blocking database operations

### Configuration Management
- Environment-based configuration with fallback defaults
- Centralized config.py for all bot settings
- Support for multiple deployment environments

## Key Relationships

### Bot Initialization Flow
1. **__main__.py** → Entry point and bot startup
2. **Tune/core/bot.py** → Pyrogram client initialization
3. **config.py** → Configuration loading
4. **Tune/core/mongo.py** → Database connection establishment
5. **plugins/** → Command handler registration

### Music Playback Flow
1. **plugins/play.py** → Command processing
2. **platforms/youtube.py** → Content extraction
3. **core/call.py** → Voice chat integration
4. **utils/stream/stream.py** → Audio streaming
5. **utils/database.py** → Queue and state management

### Administrative Flow
1. **plugins/admins.py** → Admin command processing
2. **utils/decorators.py** → Permission validation
3. **utils/database.py** → User management operations
4. **plugins/broadcast.py** → Message distribution

## Asset Management
- **assets/fonts/**: Custom fonts for image generation
- **assets/images/**: Bot logos, thumbnails, and graphics
- **cookies/**: Platform authentication tokens and cookies
- **strings/**: Multi-language support files (YAML format)

## Deployment Structure
- **Dockerfile**: Container deployment configuration
- **heroku.yml**: Heroku-specific deployment settings
- **Procfile**: Process definition for cloud platforms
- **requirements.txt**: Python dependency specifications
- **scripts/**: Deployment automation and utility scripts