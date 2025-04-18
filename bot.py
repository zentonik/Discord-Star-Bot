import discord
from discord.ext import commands
from discord.ext.commands import CooldownMapping, BucketType
import time

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.reactions = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

ALLOWED = 827918768906174504  # Allowed user ID
free_use_enabled = False

cooldowns = CooldownMapping.from_cooldown(1, 60, commands.BucketType.user)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# !star
@bot.command()
async def star(ctx, message_id: str = None):
    global free_use_enabled

    if not free_use_enabled and ctx.author.id != ALLOWED:
        await ctx.send("You are not authorized to use this command.")
        return

    if message_id is None:
        await ctx.send("Please provide a valid message ID.")
        return
    
    try:
        message_id = int(message_id)
    except ValueError:
        await ctx.send("The provided message ID is not a valid number.")
        return

    bucket = cooldowns.get_bucket(ctx.message)
    current_time = time.time()

    if bucket.update_rate_limit(current_time):
        await ctx.send("You can use this command once every minute.")
        return

    try:
        channel = ctx.channel
        msg = await channel.fetch_message(message_id)

        embed = discord.Embed(
            description=msg.content or "📷",
            color=discord.Color.gold()
        )
        embed.set_author(name=msg.author.display_name, icon_url=msg.author.display_avatar.url)
        embed.timestamp = msg.created_at

        if msg.attachments:
            for attachment in msg.attachments:
                if attachment.content_type and "image" in attachment.content_type:
                    embed.set_image(url=attachment.url)
                    break

        star_msg = await ctx.send(embed=embed)
        await star_msg.add_reaction("⭐")

    except discord.NotFound:
        await ctx.send("Message not found.")
    except discord.Forbidden:
        await ctx.send("I don’t have permission to fetch that.")
    except Exception as e:
        await ctx.send(f"Error: {e}")

# allows everyone on the server to use !star
@bot.command()
async def freeuse(ctx):
    global free_use_enabled

    if ctx.author.id != ALLOWED:
        await ctx.send("You are not authorized to use this command.")
        return

    free_use_enabled = not free_use_enabled 

    if free_use_enabled:
        await ctx.send("The `!star` command can now be used by everyone.")
    else:
        await ctx.send("The `!star` command can no longer be used by everyone.")

bot.run("TOKEN")  # Change Token.
