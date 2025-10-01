# 🍪 YouTube Cookies Setup Guide

## 🚀 Two Methods Available

### Method 1: Pastebin URL (Recommended - Fastest)
### Method 2: Local File (cookies/youtube.txt)

---

## 🌐 Method 1: Pastebin URL (Ultra-Fast)

### Step 1: Extract Cookies from Browser
1. Install browser extension: **"Get cookies.txt LOCALLY"**
2. Go to **YouTube.com** and login
3. Click extension icon → Export cookies for **youtube.com**
4. Copy the cookies content

### Step 2: Upload to Pastebin
1. Go to [pastebin.com](https://pastebin.com)
2. Paste your cookies content
3. Set **Expiration**: Never
4. Set **Exposure**: Unlisted (for security)
5. Click **Create New Paste**
6. Copy the **raw URL**: `https://pastebin.com/raw/abc123xyz`

### Step 3: Add to Environment
```env
YOUTUBE_COOKIES_URL=https://pastebin.com/raw/your_paste_id_here
```

---

## 📁 Method 2: Local File

### Step 1: Extract Cookies
Same as Method 1, steps 1-4

### Step 2: Save to Local File
1. Open `cookies/youtube.txt`
2. Paste your cookies content
3. Save the file

---

## 🍪 Cookie Format Example

```
# Netscape HTTP Cookie File
.youtube.com	TRUE	/	FALSE	1735689600	VISITOR_INFO1_LIVE	abc123def456ghi789
.youtube.com	TRUE	/	FALSE	1735689600	YSC	xyz789abc123
.youtube.com	TRUE	/	FALSE	1735689600	PREF	f4=4000000&tz=UTC
.youtube.com	TRUE	/	FALSE	1735689600	CONSENT	YES+cb.20210328-17-p0.en+FX+667
.youtube.com	TRUE	/	FALSE	1735689600	GPS	1
```

## ⚡ Performance Benefits

### With Cookies:
- 🔓 **Access age-restricted content**
- 🌍 **Bypass geo-restrictions**
- ⚡ **5x faster video processing**
- 🎥 **HD quality streams**
- 📱 **Mobile-optimized streams**
- 🚫 **Avoid rate limiting**

## 🔄 Auto-Update System

The bot automatically:
1. **Checks pastebin URL first** (if provided)
2. **Falls back to local file** if pastebin fails
3. **Caches cookies** for performance
4. **Updates local file** from pastebin

## 🛠️ Testing Your Setup

```bash
# Test cookie loading
python3 -c "
import asyncio
from utils.cookies import cookie_manager

async def test():
    cookies = await cookie_manager.get_cookies('your_pastebin_url')
    print(f'Loaded {len(cookies)} cookies')

asyncio.run(test())
"
```

## 🔒 Security Tips

1. **Use unlisted pastes** (not public)
2. **Update cookies monthly**
3. **Don't share pastebin URLs**
4. **Use different accounts** for bot cookies
5. **Monitor for unusual activity**

## 🆘 Troubleshooting

**Cookies not working:**
```bash
# Check cookie format
cat cookies/youtube.txt | head -5

# Test pastebin URL
curl https://pastebin.com/raw/your_id

# Verify bot can access
tail -f logs.txt | grep -i cookie
```

**Common Issues:**
- ❌ **Wrong format**: Ensure Netscape format
- ❌ **Expired cookies**: Refresh from browser
- ❌ **Wrong domain**: Must be `.youtube.com`
- ❌ **Missing headers**: Include all required fields

## 🎯 Priority System

1. **Pastebin URL** (if `YOUTUBE_COOKIES_URL` set)
2. **Local file** (`cookies/youtube.txt`)
3. **Cached cookies** (in memory)
4. **No cookies** (fallback mode)

## 💡 Pro Tips

1. **Multiple accounts**: Use different YouTube accounts
2. **Regular updates**: Refresh cookies weekly
3. **Backup method**: Keep both pastebin and local file
4. **Monitor logs**: Check for cookie-related errors
5. **Test regularly**: Verify cookies still work

## 🎵 Ready to Stream!

With proper cookies setup, your bot will have:
- **Unlimited access** to YouTube content
- **Premium streaming quality**
- **Bypass all restrictions**
- **Lightning-fast performance**