import logging
import asyncio
import httpx
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from config import API_ID, API_HASH, BOT_TOKEN

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# OpenRouter API details
OPENROUTER_API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://your-site.com",
    "X-Title": "YourSiteName",
}

# Create Pyrogram bot instance with 1000 workers
app = Client("dep_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, workers=1000)

async def fetch_response(user_input):
    """ Fetch response from OpenRouter API using persistent httpx session for speed """
    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [{"role": "user", "content": user_input}]
    }

    async with httpx.AsyncClient(timeout=5) as client:  # Reduced timeout for faster response
        try:
            response = await client.post(API_URL, headers=HEADERS, json=payload)
            response.raise_for_status()
            data = response.json()

            if "choices" in data and data["choices"]:
                response_text = data["choices"][0]["message"]["content"]
                return response_text.replace("<think>", "").replace("</think>", "").strip()

        except httpx.HTTPStatusError as e:
            logger.error(f"API request failed: {e}")
            return "**🚨 API error. Try again later.**"

        except httpx.TimeoutException:
            return "**⚠️ Request timed out. Try again.**"

@app.on_message(filters.command("dep"))
async def dep_command(client, message):
    user_input = message.text[len("/dep "):].strip()

    if not user_input:
        await message.reply("**⚠️ Missing text input. Provide a valid query.**", parse_mode=ParseMode.MARKDOWN)
        return

    # Send loading message
    loading_message = await message.reply("**⚡️ Thinking And Generating Response...**", parse_mode=ParseMode.MARKDOWN)

    # Fetch API response concurrently
    api_task = asyncio.create_task(fetch_response(user_input))

    # Wait for the API response
    api_message = await api_task

    # Edit message with final response
    await loading_message.edit(f"**{api_message}**", parse_mode=ParseMode.MARKDOWN)

# Run bot
app.run()
