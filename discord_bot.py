import os
import discord
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

bot = commands.Bot(command_prefix = ";", description = "bot en test de dev")

@bot.event
async def on_ready():
    print("le bot est en ligne!!!!!!")

@bot.command()
async def coucou(ctx):
    await ctx.send(f"cc! {get(ctx.guild.roles)}")

@bot.command()
async def help_fondateur(ctx):
    fondateur = get(ctx.guild.roles, name="fondateur")
    co_fondateur = get(ctx.guild.roles, name="co fondateur ❤")
    droit = get(ctx.guild.roles, name="bras droits")
    await ctx.send(f"{fondateur.mention} {co_fondateur.mention} {droit.mention}")

@bot.command()
async def help_modo(ctx):
    Administrateur = get(ctx.guild.roles, name="Administrateur")
    modo = get(ctx.guild.roles, name="modo")
    await ctx.send(f"cette personne a besoin d'aide{Administrateur.mention} {modo.mention}")

@bot.command()
async def serveur_info(ctx):
    serveur = ctx.guild
    number_of_text_channels = len(serveur.text_channels)
    number_of_voice_channels = len(serveur.voice_channels)
    serveur_descrition = serveur.description
    number_of_people = serveur.member_count
    serveur_name = serveur.name
    message = f"le serveur **{serveur_name}** contient **{number_of_people}** personnes \nla description du serveur est **{serveur_descrition}** \nce serveur possède **{number_of_text_channels}** sallon textuelle et **{number_of_voice_channels}** sallon vocalle"
    await ctx.send(message)

@bot.command()
async def bot_aide(ctx):
    aide = f"**-------- publique --------**\n\nje peux répéter apès vous avec la commende \n**;repeat** \nje peux vous donné les info du serveur avec la commende \n**;serveur_info** \nje peux donné les information d un message avec la commende \n**;message_info**\n si vous avez besoin d'aide il est possible d'utiliser la commende **;help_modo**\nsi la réson de votre demande d'aide est plus importent il y a la commende **;help_fondateur**\n**c'est deux commende(;help_modo et help_fondateur) ne son a utuliser que en quas de besoin sinon vour risquerez un ban perm,les même condition si vous spammé**\n\n**-------- admin --------**\n\nje peux bannir un bersonne avec la commende \n**;ban @lepseudo réson du ban obligatoir **ex ;ban @mermoud comportement inaproprier** \nje peux unban avec la commende **;unban Ball#9564 la réson obligajtoir** \nje peux supprimer des message avec le commende **;clear le nombre de message a sup**\net enfin je peux kick avec la commende** **;kick le pseudo et la réson du kick**\n\n**-------- esteur_egg --------**\n\nj'ai une commende cachez avous de la retrouvé(si vous la trouvé merci de ne pas spam ou risque de ban perm)\n\n**-------- copyright --------**\n\n©lasere"
    await ctx.send(aide)

@bot.command()
async def cc(ctx):
    await ctx.send(f"salut,comment ça vas {ctx.author.mention}")

@bot.command()
async def repeat(ctx, *text):
    await ctx.send(" ".join(text))

@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nombre : int):
        messages = await ctx.channel.history(limit=nombre + 1).flatten()
        for message in messages:
            await message.delete()

@bot.command()
async def message_info(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre).flatten()
    for message in messages:
        await ctx.send(message)
        print(message)

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *reason):
        reason = " ".join(reason)
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f"{user} a été banni définitivement pour la réson suivent: {reason}")

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    user_name, user_id = user.split("#")
    banne_list = await ctx.guild.bans()
    for i in banne_list:
        if i.user.name == user_name and i.user.discriminator == user_id:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"{user} a été unban")
            return
    #on sait que l utulisateur na pas été trouvé
    await ctx.send(f"le pseudo {user} na pas été trouvé dans la liste de banni")

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} a été kick ")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("la command n'a pas été trouvé...")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("il manque un argumant a ta command!")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("vous n'avez pas les perme pour utuliser cette command...")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("je suis n'avré mais il s'emble que je n est pas le permition pour pouvoir executer cette command :/")

#démarer le bot
bot.run(os.getenv("TOKEN"))