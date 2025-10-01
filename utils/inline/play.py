from pyrogram.types import InlineKeyboardButton

def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▶️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="⏹", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="🔀", callback_data=f"ADMIN Shuffle|{chat_id}"),
            InlineKeyboardButton(text="🔁", callback_data=f"ADMIN Loop|{chat_id}"),
            InlineKeyboardButton(text="📋", callback_data=f"queue|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="🗑 Close", callback_data="close"),
        ],
    ]
    return buttons

def telegram_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text="📥 Download", callback_data="download"),
            InlineKeyboardButton(text="🔗 Share", callback_data="share"),
        ],
        [
            InlineKeyboardButton(text="🗑 Close", callback_data="close"),
        ],
    ]
    return buttons