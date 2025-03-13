import os
import logging
import httpx
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from config import GROQ_API_KEY, GROQ_API_URL, TEXT_MODEL

# Initialize logging
logger = logging.getLogger(__name__)

def setup_groq_handler(app: Client):
    @app.on_message(filters.command(["dep"], prefixes=["/", "."]) & (filters.private | filters.group))
    def dep_command(client: Client, message: Message):
        # Extract user text from the command
        user_text = " ".join(message.command[1:])  # Extract text after /dep
        if not user_text:
            message.reply_text("**⚠️ Please provide some text after the `/dep` command.**", parse_mode=ParseMode.MARKDOWN)
            return

        # Send a temporary message
        temp_message = message.reply_text("**⚡️Generating Dep Response....⌛️**", parse_mode=ParseMode.MARKDOWN)

        try:
            # Call the Groq API
            response = requests.post(
                GROQ_API_URL,
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": TEXT_MODEL,
                    "messages": [
                        {"role": "system", "content": "Reply in the same language as the user's message."},
                        {"role": "user", "content": user_text},
                    ],
                },
            )
            response.raise_for_status()
            data = response.json()
            bot_response = data.get("choices", [{}])[0].get("message", {}).get("content", "⚠️ Error: Unexpected AI response.")

            # Edit the temporary message with the final response
            temp_message.edit_text(bot_response, parse_mode=ParseMode.MARKDOWN)

        except requests.exceptions.RequestException as e:
            logger.error(f"HTTP error while calling Groq API: {e}")
            temp_message.edit_text("**⚠️ Sorry, I encountered a network error. Please try again later.**", parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            temp_message.edit_text("**⚠️ Sorry, I encountered an error processing your request.**", parse_mode=ParseMode.MARKDOWN)

# Run bot
if __name__ == "__main__":
    setup_groq_handler(app)
    app.run()
