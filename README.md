
# 🤖 DeepSeek: R1- AI Chatbot for Telegram  

DeepSeek: R1 is a fast and inefficient AI-powered chatbot for Telegram, built using Pyrogram and OpenRouter AI API. This bot can handle multiple user queries simultaneously with high responsiveness.  

## ✨ Features  
- 🚀 AI-powered responses via OpenRouter API  
- ⚡ Handles multiple users efficiently with 1000 workers  
- 🔥 Fast API requests using `httpx` 
- 🛠️ Error handling for timeouts and failed API responses  

## 📂 Project Structure  
```
DeepSeekBot/
│── main.py           # Main bot script
│── config.py         # Configuration file (API keys, bot token, etc.)
│── requirements.txt  # Required Python dependencies
```

## Official Api Call With `OpenAi` Library
```
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<OPENROUTER_API_KEY>",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="deepseek/deepseek-r1:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)
```
## Official Api Call With python
```
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "deepseek/deepseek-r1:free",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ],
    
  })
)
```

## 🛠️ Setup & Installation  

### ✅ Prerequisites  
- 🐍 Python 3.8+  
- 🤖 Telegram Bot Token from [@BotFather](https://t.me/BotFather)  
- 🔑 API credentials from [OpenRouter](https://openrouter.ai/)  

### 📥 Installation Steps  

1. **Clone the Repository**  
   ```sh
   git clone https://github.com/abirxdhack/DeepSeekBot.git
   cd DeepSeekBot
   ```

2. **(Optional) Create a Virtual Environment**  
   ```sh
   python3 -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```

3. **Install Dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure the Bot**  
   - Open `config.py` and add the following details:  
     ```python
     API_ID = "your_api_id"
     API_HASH = "your_api_hash"
     BOT_TOKEN = "your_bot_token"
     ```
   - Replace `your_api_id`, `your_api_hash`, and `your_bot_token` with actual values.  

5. **Run the Bot**  
   ```sh
   python3 main.py
   ```

## 📝 Usage  
- Start the bot and send a command:  
  ```
  /dep your_question_here
  ```
- The bot will process your request and reply with an AI-generated response.  

## 📜 License  
This project is open-source and available under the MIT License.  

## 👤 Credits  
Developed by [@abirxdhack](https://github.com/abirxdhack).  

Developed by [@nkka404](https://t.me/nkka404).  
