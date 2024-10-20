import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Embed
import json
import os

# กำหนดชื่อไฟล์ JSON
KEY_FILE = 'keys.json'
MY_GUILD_ID = 123456789101112  # แทนที่ด้วย Guild ID ของคุณ

# ฟังก์ชันเพื่อโหลดคีย์จากไฟล์ JSON
def load_keys():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'r') as file:
            return json.load(file)
    return []

# ฟังก์ชันเพื่อบันทึกคีย์ไปยังไฟล์ JSON
def save_keys(keys):
    with open(KEY_FILE, 'w') as file:
        json.dump(keys, file)

# สร้างบอทและคำสั่ง slash
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True  # เปิดใช้งาน Server Members Intent
bot = commands.Bot(command_prefix="!", intents=intents)

# โหลดคีย์จากไฟล์ JSON
keys = load_keys()

# ตรวจสอบบทบาท
async def is_admin(interaction: Interaction):
    return any(role.name == "Owner" for role in interaction.user.roles)

# ตรวจสอบว่าอยู่ในเซิร์ฟเวอร์ที่ถูกต้อง
async def is_in_correct_guild(interaction: Interaction):
    return interaction.guild and interaction.guild.id == MY_GUILD_ID

# คำสั่ง slash เพื่อให้คีย์
@bot.slash_command(name="get_key", description="รับคีย์จากบอท")
async def get_key(interaction: Interaction):
    if not await is_in_correct_guild(interaction):
        await interaction.response.send_message("คุณไม่สามารถใช้คำสั่งนี้ในเซิร์ฟเวอร์นี้ได้", ephemeral=True)
        return

    if keys:
        key = keys.pop(0)
        save_keys(keys)  # บันทึกคีย์ที่อัปเดตแล้ว
        thiskeys = Embed(title="🔑 นี่คือคีย์ของคุณ",description=f"```json\n{key}\n```", color=0x00ff00)
        await interaction.response.send_message(embed=thiskeys, ephemeral=True)
    else:
        await interaction.response.send_message("ไม่มีคีย์ให้บริการในขณะนี้", ephemeral=True)

# คำสั่ง slash เพื่อเพิ่มคีย์
@bot.slash_command(name="add_key", description="เพิ่มคีย์ใหม่")
async def add_keys(interaction: Interaction, keys_input: str):
    if not await is_in_correct_guild(interaction):
        await interaction.response.send_message("คุณไม่สามารถใช้คำสั่งนี้ในเซิร์ฟเวอร์นี้ได้", ephemeral=True)
        return

    if await is_admin(interaction):
        new_keys = keys_input.split()
        keys.extend(new_keys)
        save_keys(keys)  # บันทึกคีย์ที่อัปเดตแล้ว
        newskeys =Embed(title="🔑 คีย์ถูกเพิ่มแล้ว", description=f"```json\n{', '.join(new_keys)}\n```", color=0x00ff00)
        await interaction.response.send_message(embed=newskeys, ephemeral=True) 

    else:
        await interaction.response.send_message("คุณไม่มีสิทธิ์ในการใช้คำสั่งนี้", ephemeral=True)

# คำสั่ง slash เพื่อดูคีย์ทั้งหมด (เฉพาะผู้ดูแล)
@bot.slash_command(name="list_keys", description="ดูคีย์ทั้งหมด")
async def list_keys(interaction: Interaction):
    if not await is_in_correct_guild(interaction):
        await interaction.response.send_message("คุณไม่สามารถใช้คำสั่งนี้ในเซิร์ฟเวอร์นี้ได้", ephemeral=True)
        return

    if await is_admin(interaction):
        keys_json = json.dumps(keys, indent=4)
        allkeys = Embed(title="🔑 คีย์ทั้งหมด", description=f"```json\n{keys_json}\n```", color=0x00ff00)
        await interaction.response.send_message(embed=allkeys, ephemeral=True)
    else:
        await interaction.response.send_message("คุณไม่มีสิทธิ์ในการใช้คำสั่งนี้", ephemeral=True)

# เริ่มต้นบอท
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

# รันบอท
bot.run('ใส่tokenตรงนี้')