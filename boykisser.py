import os
import sys
import time
import random
import base64
import json
import platform
import logging
from datetime import datetime

import discord
from discord.ext import commands
import requests
from colorama import Fore, init

# Initialize Colorama for colored output
init(autoreset=True)

# Suppress Discord API logging
logging.getLogger('discord').setLevel(logging.CRITICAL)

# Boykisser Logo (displayed in red)
LOGO = f"""{Fore.RED}
  _                 _    _                                          
 | |__   ___  _   _| | _(_)___ ___  ___ _ __                        
 | '_ \ / _ \| | | | |/ / / __/ __|/ _ \ '__|                       
 | |_) | (_) | |_| |   <| \__ \__ \  __/ |                          
 |_.__/ \___/ \__, |_|\_\_|___/___/\___|_|                          
             |___/                                                  
"""

# Global variables for simulated settings
debug_mode = False
current_prefix = "!"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ----- STARTUP -----
clear()
print(LOGO)
TOKEN = input(f"{Fore.YELLOW}[?] Enter your Discord bot token: ")

# ----- BOT SETUP -----
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=current_prefix, intents=intents)
bot.remove_command("help")  # Remove default help

# ========= 50 Bot-Related Features =========
# 1. Change Bot Username
async def change_username():
    new_username = input("Enter new username: ")
    try:
        await bot.user.edit(username=new_username)
        print(f"[✓] Username changed to: {new_username}")
    except Exception as e:
        print("Error changing username:", e)

# 2. Change Bot Bio (About Me)
async def change_bio():
    new_bio = input("Enter new bio: ")
    try:
        await bot.user.edit(about_me=new_bio)
        print("[✓] Bio updated!")
    except Exception as e:
        print("Error updating bio:", e)

# 3. Change Bot Avatar
async def change_avatar():
    file_path = input("Enter path to avatar image file: ")
    try:
        with open(file_path, "rb") as f:
            image = f.read()
        await bot.user.edit(avatar=image)
        print("[✓] Avatar changed successfully!")
    except Exception as e:
        print("Error changing avatar:", e)

# 4. Set Custom Status (Game)
async def set_custom_status():
    status = input("Enter custom status (game): ")
    try:
        await bot.change_presence(activity=discord.Game(name=status))
        print(f"[✓] Custom status set to: {status}")
    except Exception as e:
        print("Error setting custom status:", e)

# 5. Set Playing Activity
async def set_playing_activity():
    game = input("Enter game name: ")
    try:
        await bot.change_presence(activity=discord.Game(name=game))
        print(f"[✓] Playing activity set to: {game}")
    except Exception as e:
        print("Error setting playing activity:", e)

# 6. Set Streaming Activity
async def set_streaming_activity():
    title = input("Enter streaming title: ")
    url = input("Enter streaming URL: ")
    try:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=title, url=url))
        print("[✓] Streaming activity set.")
    except Exception as e:
        print("Error setting streaming activity:", e)

# 7. Set Listening Activity
async def set_listening_activity():
    listen_to = input("Enter what you're listening to: ")
    try:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listen_to))
        print("[✓] Listening activity set.")
    except Exception as e:
        print("Error setting listening activity:", e)

# 8. Set Watching Activity
async def set_watching_activity():
    watch = input("Enter what you're watching: ")
    try:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watch))
        print("[✓] Watching activity set.")
    except Exception as e:
        print("Error setting watching activity:", e)

# 9. Set Invisible Status
async def set_invisible_status():
    try:
        await bot.change_presence(status=discord.Status.invisible)
        print("[✓] Status set to invisible.")
    except Exception as e:
        print("Error setting invisible status:", e)

# 10. Set Online Status
async def set_online_status():
    try:
        await bot.change_presence(status=discord.Status.online)
        print("[✓] Status set to online.")
    except Exception as e:
        print("Error setting online status:", e)

# 11. Set Idle Status
async def set_idle_status():
    try:
        await bot.change_presence(status=discord.Status.idle)
        print("[✓] Status set to idle.")
    except Exception as e:
        print("Error setting idle status:", e)

# 12. Set Do Not Disturb Status
async def set_dnd_status():
    try:
        await bot.change_presence(status=discord.Status.do_not_disturb)
        print("[✓] Status set to Do Not Disturb.")
    except Exception as e:
        print("Error setting DND status:", e)

# 13. Get Bot Token Info
async def get_token_info():
    headers = {"Authorization": TOKEN}
    try:
        r = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        if r.status_code == 200:
            data = r.json()
            print(f"[✓] Logged in as: {data.get('username')}#{data.get('discriminator')}")
        else:
            print(f"Error: Unable to fetch token info (status code {r.status_code})")
    except Exception as e:
        print("Error fetching token info:", e)

# 14. List Guilds Bot Is In
async def list_guilds():
    if bot.guilds:
        print("[✓] Guilds:")
        for guild in bot.guilds:
            print(f" - {guild.name} (ID: {guild.id})")
    else:
        print("Bot is not in any guilds.")

# 15. List Channels of a Guild
async def list_channels():
    try:
        guild_id = int(input("Enter guild ID: "))
        guild = bot.get_guild(guild_id)
        if guild:
            print(f"[✓] Channels in {guild.name}:")
            for ch in guild.channels:
                print(f" - {ch.name} (ID: {ch.id}, Type: {ch.type})")
        else:
            print("Guild not found.")
    except Exception as e:
        print("Error listing channels:", e)

# 16. List Roles of a Guild
async def list_roles():
    try:
        guild_id = int(input("Enter guild ID: "))
        guild = bot.get_guild(guild_id)
        if guild:
            print(f"[✓] Roles in {guild.name}:")
            for role in guild.roles:
                print(f" - {role.name} (ID: {role.id})")
        else:
            print("Guild not found.")
    except Exception as e:
        print("Error listing roles:", e)

# 17. Get Bot Ping (Latency)
async def get_ping():
    latency = bot.latency
    print(f"[✓] Bot latency: {int(latency * 1000)} ms")

# 18. Clear Bot Activity (Remove Activity)
async def clear_activity():
    try:
        await bot.change_presence(activity=None)
        print("[✓] Activity cleared.")
    except Exception as e:
        print("Error clearing activity:", e)

# 19. Set Custom Activity (General)
async def set_custom_activity():
    print("Choose activity type:")
    print("1. Playing  2. Streaming  3. Listening  4. Watching")
    choice = input("Enter choice (1-4): ")
    name = input("Enter activity name: ")
    try:
        if choice == "1":
            act = discord.Game(name=name)
        elif choice == "2":
            url = input("Enter streaming URL: ")
            act = discord.Activity(type=discord.ActivityType.streaming, name=name, url=url)
        elif choice == "3":
            act = discord.Activity(type=discord.ActivityType.listening, name=name)
        elif choice == "4":
            act = discord.Activity(type=discord.ActivityType.watching, name=name)
        else:
            print("Invalid choice.")
            return
        await bot.change_presence(activity=act)
        print("[✓] Custom activity set.")
    except Exception as e:
        print("Error setting custom activity:", e)

# 20. Get Bot User Info
async def get_user_info():
    try:
        user = bot.user
        print(f"[✓] User ID: {user.id}")
        print(f"Username: {user.name}#{user.discriminator}")
        print(f"Created at: {user.created_at}")
    except Exception as e:
        print("Error fetching user info:", e)

# 21. Get Bot's Current Avatar URL
async def get_avatar_url():
    try:
        if bot.user.avatar:
            url = bot.user.avatar.url if hasattr(bot.user.avatar, "url") else "No URL available"
            print(f"[✓] Current Avatar URL: {url}")
        else:
            print("No avatar set.")
    except Exception as e:
        print("Error getting avatar URL:", e)

# 22. Save Bot Settings to File
async def save_settings():
    settings = {
        "username": bot.user.name,
        "status": str(bot.user.status),
        "activity": str(bot.user.activity) if bot.user.activity else "None"
    }
    try:
        with open("bot_settings.json", "w") as f:
            json.dump(settings, f, default=str)
        print("[✓] Settings saved to bot_settings.json")
    except Exception as e:
        print("Error saving settings:", e)

# 23. Load Bot Settings from File
async def load_settings():
    try:
        with open("bot_settings.json", "r") as f:
            settings = json.load(f)
        print("[✓] Loaded settings:")
        for key, value in settings.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print("Error loading settings:", e)

# 24. Update Bot's Game Activity
async def update_game_activity():
    game = input("Enter new game name: ")
    try:
        await bot.change_presence(activity=discord.Game(name=game))
        print(f"[✓] Game activity updated to: {game}")
    except Exception as e:
        print("Error updating game activity:", e)

# 25. Simulate Bot Restart
async def simulate_restart():
    print("[✓] Simulating bot restart... (This is only a simulation)")
    # Note: Actual restart would require stopping and re-running the script.

# 26. Display System Info (Bot Environment)
async def display_system_info():
    print("[✓] System Information:")
    print("OS:", os.name)
    print("Platform:", sys.platform)
    print("Processor:", platform.processor())
    print("Python Version:", platform.python_version())

# 27. Show Current Time
async def show_current_time():
    print("[✓] Current time:", datetime.now())

# 28. Get Discord Library Version
async def discord_library_version():
    print("[✓] discord.py version:", discord.__version__)

# 29. Toggle Debug Mode (Simulation)
async def toggle_debug_mode():
    global debug_mode
    debug_mode = not debug_mode
    state = "ON" if debug_mode else "OFF"
    print(f"[✓] Debug mode toggled {state}")

# 30. Get Bot's Creation Date
async def get_bot_creation_date():
    try:
        print("[✓] Bot account created on:", bot.user.created_at)
    except Exception as e:
        print("Error getting creation date:", e)

# 31. Show Bot's Current Status (Presence)
async def show_bot_status():
    try:
        print("[✓] Current status:", bot.user.status)
    except Exception as e:
        print("Error fetching status:", e)

# 32. Simulate Sending a Test Message
async def simulate_send_message():
    channel_id = input("Enter channel ID (simulation): ")
    message = input("Enter message content (simulation): ")
    print(f"[SIMULATION] Would send message to channel {channel_id}: {message}")

# 33. Simulate Editing a Message
async def simulate_edit_message():
    message_id = input("Enter message ID to edit (simulation): ")
    new_content = input("Enter new content (simulation): ")
    print(f"[SIMULATION] Would edit message {message_id} to: {new_content}")

# 34. Simulate Deleting a Message
async def simulate_delete_message():
    message_id = input("Enter message ID to delete (simulation): ")
    print(f"[SIMULATION] Would delete message {message_id}")

# 35. Simulate Bulk Deleting Messages
async def simulate_bulk_delete():
    channel_id = input("Enter channel ID for bulk delete (simulation): ")
    count = input("Enter number of messages to delete (simulation): ")
    print(f"[SIMULATION] Would bulk delete {count} messages in channel {channel_id}")

# 36. Generate Fake Nitro Code
async def generate_fake_nitro():
    code = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=16))
    print("[✓] Fake Nitro Code:", "https://discord.gift/" + code)

# 37. Generate Fake Invite Code
async def generate_fake_invite():
    code = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6))
    print("[✓] Fake Invite Code:", "https://discord.gg/" + code)

# 38. Get Current Timestamp (Unix)
async def get_current_timestamp():
    print("[✓] Current Unix Timestamp:", int(datetime.now().timestamp()))

# 39. Display Bot's Shard Count (Simulation)
async def display_shard_count():
    # If bot is not sharded, this will be 1.
    count = getattr(bot, "shard_count", 1)
    print("[✓] Bot Shard Count:", count)

# 40. Display Bot's Enabled Intents
async def display_intents():
    enabled = []
    intents_obj = bot.intents
    for intent, value in intents_obj.__dict__.items():
        if isinstance(value, bool) and value:
            enabled.append(intent)
    print("[✓] Enabled Intents:")
    for intent in enabled:
        print(" -", intent)

# 41. Get Current Activity Type
async def current_activity_type():
    act = bot.user.activity
    if act:
        print("[✓] Current activity type:", act.type.name, "with name:", act.name)
    else:
        print("No activity set.")

# 42. Simulate Changing Command Prefix
async def change_command_prefix():
    global current_prefix
    new_prefix = input("Enter new command prefix (simulation): ")
    current_prefix = new_prefix
    print(f"[SIMULATION] Command prefix changed to: {current_prefix} (Note: This does not affect runtime commands)")

# 43. List Available Commands
async def list_available_commands():
    print("[✓] Available Commands:")
    for num, desc in enumerate(menu_options, start=1):
        print(f"{num}. {desc}")

# 44. Simulate Logging Out
async def simulate_logout():
    print("[SIMULATION] Logging out... (simulation only, not actually logging out)")

# 45. Simulate Logging In Again
async def simulate_login():
    print("[SIMULATION] Logging in... (simulation only, not actually re-logging in)")

# 46. Simulate Reconnecting
async def simulate_reconnect():
    print("[SIMULATION] Reconnecting to Discord... (simulation only)")

# 47. Display a Random Bot Fact
async def random_bot_fact():
    facts = [
        "Discord bots can perform a wide range of tasks.",
        "Bots are an integral part of many Discord communities.",
        "discord.py is one of the most popular libraries for building bots."
    ]
    print("[✓] Bot Fact:", random.choice(facts))

# 48. Simulate Updating Bot
async def simulate_update():
    print("[SIMULATION] Checking for updates... No updates available.")

# 49. Display Help/Info About the Tool
async def display_help():
    print("[✓] Boykisser Multi-Tool Help:")
    print("This tool provides 50 bot-related functions for managing and inspecting your Discord bot.")
    print("Use the menu to select a feature by entering its corresponding number.")

# 50. Exit the Tool
async def exit_tool():
    print("Exiting Boykisser Multi-Tool.")
    sys.exit()

# ========= End of 50 Features =========

# Mapping of option numbers to functions
tools = {
    1: change_username,
    2: change_bio,
    3: change_avatar,
    4: set_custom_status,
    5: set_playing_activity,
    6: set_streaming_activity,
    7: set_listening_activity,
    8: set_watching_activity,
    9: set_invisible_status,
    10: set_online_status,
    11: set_idle_status,
    12: set_dnd_status,
    13: get_token_info,
    14: list_guilds,
    15: list_channels,
    16: list_roles,
    17: get_ping,
    18: clear_activity,
    19: set_custom_activity,
    20: get_user_info,
    21: get_avatar_url,
    22: save_settings,
    23: load_settings,
    24: update_game_activity,
    25: simulate_restart,
    26: display_system_info,
    27: show_current_time,
    28: discord_library_version,
    29: toggle_debug_mode,
    30: get_bot_creation_date,
    31: show_bot_status,
    32: simulate_send_message,
    33: simulate_edit_message,
    34: simulate_delete_message,
    35: simulate_bulk_delete,
    36: generate_fake_nitro,
    37: generate_fake_invite,
    38: get_current_timestamp,
    39: display_shard_count,
    40: display_intents,
    41: current_activity_type,
    42: change_command_prefix,
    43: list_available_commands,
    44: simulate_logout,
    45: simulate_login,
    46: simulate_reconnect,
    47: random_bot_fact,
    48: simulate_update,
    49: display_help,
    50: exit_tool
}

# Descriptions for the menu (in order)
menu_options = [
    "Change Bot Username",
    "Change Bot Bio",
    "Change Bot Avatar",
    "Set Custom Status (Game)",
    "Set Playing Activity",
    "Set Streaming Activity",
    "Set Listening Activity",
    "Set Watching Activity",
    "Set Invisible Status",
    "Set Online Status",
    "Set Idle Status",
    "Set Do Not Disturb Status",
    "Get Bot Token Info",
    "List Guilds Bot Is In",
    "List Channels of a Guild",
    "List Roles of a Guild",
    "Get Bot Ping (Latency)",
    "Clear Bot Activity",
    "Set Custom Activity (General)",
    "Get Bot User Info",
    "Get Bot's Current Avatar URL",
    "Save Bot Settings to File",
    "Load Bot Settings from File",
    "Update Bot's Game Activity",
    "Simulate Bot Restart",
    "Display System Info",
    "Show Current Time",
    "Get Discord Library Version",
    "Toggle Debug Mode",
    "Get Bot's Creation Date",
    "Show Bot's Current Status",
    "Simulate Sending a Test Message",
    "Simulate Editing a Message",
    "Simulate Deleting a Message",
    "Simulate Bulk Deleting Messages",
    "Generate Fake Nitro Code",
    "Generate Fake Invite Code",
    "Get Current Unix Timestamp",
    "Display Bot's Shard Count",
    "Display Bot's Enabled Intents",
    "Get Current Activity Type",
    "Simulate Changing Command Prefix",
    "List Available Commands",
    "Simulate Logging Out",
    "Simulate Logging In Again",
    "Simulate Reconnecting",
    "Display a Random Bot Fact",
    "Simulate Updating Bot",
    "Display Help/Info About the Tool",
    "Exit the Tool"
]

# Display menu centered in terminal
def display_menu():
    clear()
    print(LOGO)
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80
    title = "🎭 Boykisser Multi-Tool 🎭"
    print(title.center(terminal_width))
    print("\n")
    for i, option in enumerate(menu_options, start=1):
        print(f"{Fore.CYAN}[{i}] {option}".center(terminal_width))
    print(f"{Fore.YELLOW}[0] Exit".center(terminal_width))

# Main menu loop
async def main_menu():
    while True:
        display_menu()
        try:
            choice = int(input(f"{Fore.YELLOW}[?] Select an option: "))
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1)
            continue
        if choice == 0:
            await exit_tool()
        elif choice in tools:
            await tools[choice]()
        else:
            print("Invalid option selected.")
        input("\nPress Enter to continue...")

# ----- BOT EVENT -----
@bot.event
async def on_ready():
    print(f"{Fore.GREEN}[✓] Logged in as {bot.user}!")
    await main_menu()

# ----- RUN BOT -----
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure:
    print(f"{Fore.RED}[!] Invalid token provided!")
except Exception as e:
    print("An error occurred:", e)
