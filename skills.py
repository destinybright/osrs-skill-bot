import discord
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.message_content = True


# command to use ! to get bot responses
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def skills(ctx, *, username: str):
    """
    Lists the levels of all of a user's skills

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data:
        embed = create_skills_embed(username, data, ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def overall(ctx, *, username: str):
    """
    Lists the overall level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Overall" in data:
        embed = create_skill_embed(username, "Overall", data["Overall"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def attack(ctx, *, username: str):
    """
    Lists the Attack level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Attack" in data:
        embed = create_skill_embed(username, "Attack", data["Attack"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def defence(ctx, *, username: str):
    """
    Lists the Defence level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Defence" in data:
        embed = create_skill_embed(username, "Defence", data["Defence"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def strength(ctx, *, username: str):
    """
    Lists the Strength level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Strength" in data:
        embed = create_skill_embed(username, "Strength", data["Strength"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def hitpoints(ctx, *, username: str):
    """
    Lists the Hitpoints level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Hitpoints" in data:
        embed = create_skill_embed(username, "Hitpoints", data["Hitpoints"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def ranged(ctx, *, username: str):
    """
    Lists the Ranged level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Ranged" in data:
        embed = create_skill_embed(username, "Ranged", data["Ranged"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def prayer(ctx, *, username: str):
    """
    Lists the Prayer level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Prayer" in data:
        embed = create_skill_embed(username, "Prayer", data["Prayer"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def magic(ctx, *, username: str):
    """
    Lists the Magic level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Magic" in data:
        embed = create_skill_embed(username, "Magic", data["Magic"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def cooking(ctx, *, username: str):
    """
    Lists the Cooking level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Cooking" in data:
        embed = create_skill_embed(username, "Cooking", data["Cooking"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def woodcutting(ctx, *, username: str):
    """
    Lists the Woodcutting level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Woodcutting" in data:
        embed = create_skill_embed(username, "Woodcutting", data["Woodcutting"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def fletching(ctx, *, username: str):
    """
    Lists the Fletching level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Fletching" in data:
        embed = create_skill_embed(username, "Fletching", data["Fletching"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def fishing(ctx, *, username: str):
    """
    Lists the Fishing level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Fishing" in data:
        embed = create_skill_embed(username, "Fishing", data["Fishing"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def firemaking(ctx, *, username: str):
    """
    Lists the Firemaking level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Firemaking" in data:
        embed = create_skill_embed(username, "Firemaking", data["Firemaking"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def crafting(ctx, *, username: str):
    """
    Lists the Crafting level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Crafting" in data:
        embed = create_skill_embed(username, "Crafting", data["Crafting"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def smithing(ctx, *, username: str):
    """
    Lists the Smithing level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Smithing" in data:
        embed = create_skill_embed(username, "Smithing", data["Smithing"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def mining(ctx, *, username: str):
    """
    Lists the Mining level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Mining" in data:
        embed = create_skill_embed(username, "Mining", data["Mining"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def herblore(ctx, *, username: str):
    """
    Lists the herblore level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Herblore" in data:
        embed = create_skill_embed(username, "Herblore", data["Herblore"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def agility(ctx, *, username: str):
    """
    Lists the Agility level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Agility" in data:
        embed = create_skill_embed(username, "Agility", data["Agility"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def thieving(ctx, *, username: str):
    """
    Lists the Thieving level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Thieving" in data:
        embed = create_skill_embed(username, "Thieving", data["Thieving"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def slayer(ctx, *, username: str):
    """
    Lists the Slayer level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Slayer" in data:
        embed = create_skill_embed(username, "Slayer", data["Slayer"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def farming(ctx, *, username: str):
    """
    Lists the Farming level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Farming" in data:
        embed = create_skill_embed(username, "Farming", data["Farming"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def runecraft(ctx, *, username: str):
    """
    Lists the Runecraft level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Runecraft" in data:
        embed = create_skill_embed(username, "Runecraft", data["Runecraft"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def hunter(ctx, *, username: str):
    """
    Lists the Hunter level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Hunter" in data:
        embed = create_skill_embed(username, "Hunter", data["Hunter"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

@bot.command()
async def construction(ctx, *, username: str):
    """
    Lists the Construction level and XP of a user

    """
    await ctx.trigger_typing()
    data = get_osrs_skills(username)
    if data and "Construction" in data:
        embed = create_skill_embed(username, "Construction", data["Construction"], ctx)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ **Error:** There is no player with the username **{username}**.")

skill_names = [
        "Overall",
        "Attack",
        "Defence",
        "Strength",
        "Hitpoints",
        "Ranged",
        "Prayer",
        "Magic",
        "Cooking",
        "Woodcutting",
        "Fletching",
        "Fishing",
        "Firemaking",
        "Crafting",
        "Smithing",
        "Mining",
        "Herblore",
        "Agility",
        "Thieving",
        "Slayer",
        "Farming",
        "Runecraft",
        "Hunter",
        "Construction"
    ]

def get_osrs_skills(username):
    # OSRS api
    url = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={username}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    lines = response.text.splitlines()
    skills = {}
    for i, skill in enumerate(skill_names):
        try:
            skill_data = lines[i].split(",")
            level = skill_data[1]
            experience = skill_data[2]
            skills[skill] = {
                "level": level,
                "experience": experience
            }
        except IndexError:
            skills[skill] = {
                "level": "N/A",
                "experience": "N/A"
            }
    return skills

def create_skills_embed(username, skills, ctx):
    embed = discord.Embed(
        title=f"Skill Levels for {username}",
        url= "https://discord.com/oauth2/authorize?client_id=1317430179022376971",
        color=discord.Color.green()
    )

    embed.set_author(name=ctx.author.display_name, url="http://google.com", icon_url=ctx.author.display_avatar.url)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/2007scape/images/c/ce/Gnome_child_chathead.png/revision/latest?cb=20150729051514")

    for skill, data in skills.items():
        embed.add_field(
            name=f"{skill} Level",
            value=f"{data['level']}",
            inline=True
        )

    embed.set_footer(text="To see XP amount for a certain skill, use the command ![input desired skill here]")
    return embed

def create_skill_embed(username, skill_name, skill_data, ctx):
    embed = discord.Embed(
        title=f"{skill_name} level for {username}",
        url= "https://discord.com/oauth2/authorize?client_id=1317430179022376971",
        color=discord.Color.green()
    )

    embed.set_author(name=ctx.author.display_name, url="http://google.com", icon_url=ctx.author.display_avatar.url)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/2007scape/images/c/ce/Gnome_child_chathead.png/revision/latest?cb=20150729051514")


    embed.add_field(
        name="Level",
        value=skill_data.get('level', 'N/A'),
        inline=True
    )
    embed.add_field(
        name="Experience",
        value=skill_data.get('experience', 'N/A'),
        inline=True
    )
    embed.set_footer(text="To see the levels of all skills, use the command !skills")
    return embed


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        command_name = ctx.command.name if ctx.command else 'Unknown Command'
        await ctx.send(f"❌ **Error:** Missing required argument.\nUsage: `!{command_name} <username>`")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ **Error:** Unknown command. Use !list to see all valid commands.")
    else:
        print(f"Unhandled error: {error}")
        await ctx.send("❌ **Error:** An unexpected error occurred. Please try again later.")

@bot.command(name='list')
async def list_commands(ctx):
    """
    Lists all valid commands

    """
    embed = discord.Embed(
        title="Valid Commands",
        url= "https://discord.com/oauth2/authorize?client_id=1317430179022376971",
        description="These are all the valid commands:",
        color=discord.Color.green()
    )

    commands_per_embed = 15
    command_list = list(bot.commands)
    command_batches = [command_list[i:i + commands_per_embed] for i in range(0, len(command_list), commands_per_embed)]

    for batch in command_batches:
        for command in batch:
            if not command.hidden and command.name != 'list':
                description = command.help if command.help else "No description provided."
                embed.add_field(
                    name=f"!{command.name}",
                    value=description,
                    inline=False
                )
        await ctx.send(embed=embed)
        embed.clear_fields()


bot.run('')
