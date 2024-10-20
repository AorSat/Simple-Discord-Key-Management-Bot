# Discord Key Management Bot

บอทนี้ถูกพัฒนาเพื่อใช้ในการจัดการคีย์ในเซิร์ฟเวอร์ Discord โดยอนุญาตให้ผู้ใช้ขอรับคีย์ และผู้ดูแลสามารถเพิ่มคีย์หรือดูคีย์ทั้งหมดได้
---
## Features
- สามารถรับคีย์ได้ด้วยคำสั่ง `/get_key`
- สามารถเพิ่มคีย์ได้ด้วยคำสั่ง `/add_key` (Admin only)
- สามารถดูคีย์ทั้งหมดได้ด้วยคำสั่ง `/list_keys` (Admin only)
---
## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/AorSat/Simple-Discord-Key-Management-Bot.git
   cd Simple-Discord-Key-Management-Bot
1. Install dependencies
   ```bash
   pip install -r requirements.txt

1. Add your bot token
   - นำtokenไปวางที่ `bot.run('ใส่tokenตรงนี้')`
1. Run bot
   ```bash
   python discordbot.py
---
## Requirements
- Python 3.10+
- Nextcord
---
