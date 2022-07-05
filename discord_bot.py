import os
import discord
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv
from random import *

load_dotenv(dotenv_path="config")

bot = commands.Bot(command_prefix = ";", description = "official bot from the discord server: 𝐸𝓍𝓅𝑒́𝓇𝒾𝑒𝓃𝒸𝑒")

@bot.event
async def on_ready():
    print("le bot est en ligne!!!!!!")
    channel = bot.get_channel(832379873753956397)
    await channel.send("salut,je suis en ligne si besoin😉")

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
@commands.has_permissions(manage_messages = True)
async def code(ctx):
    await ctx.send("je suis open souce si vous soiter voir comment je sui fait rendévous ici: https://github.com/lasere77/bot_discord")

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
    aide = f"**-------- publique --------**\n\nje peux répéter après vous avec la commande : \n**;repeat** (ne pas lui faire dire des choses imoral sous risque de kick et ban si récidive)\nje peux vous donné les info du serveur avec la commande \n**;serveur_info** \nje peux donné les informations d'un message avec la commande  \n**;message_info**\n si vous avez besoin d'aide il est possible d'utiliser la commande \n**;help_modo**\nsi la raison de votre demande d'aide est plus importente il y a la commande \n**;help_fondateur**\n**ces deux commande (;help_modo et help_fondateur) ne son a utiliser que en cas de besoin sinon vous risquerez un ban perm.A ne pas spam non plus sous risque de la même sanctionla commande ** \nla commande \n**;meme** permet de regardé le même du serveur \ntu peux aussi joué avec la command **;game** \nle but est de donné un nombre entre 0 a 6 et si la chance est avec toi tu gagneras peut être\nsi tu a besois de générer un nombre aléatoir entre 0 a 6tu peux utuliser la command **;dé** \navec la command **;vidéo**\ntu pourra regardé des vidéo qui son dans la list choisir aléatoirement\n\n**-------- admin --------**\n\nje peux bannir une personne avec la commende \n;ban @lepseudo la raison du ban est obligatoire **ex ;ban @mermoud comportement insulant**\nje peux unban avec la commende:\n**;unban Ball#9564 la raison obligatoire** \nje peux supprimer des messages avec le commande \n**;clear [nombre de message à supprimé]**\net enfin je peux kick avec la commande\n**;kick [Pseudo + la raison]** \nj'ai aussi la commande \n**;code pour voir mon code source**\n\n**-------- easteur_egg --------**\n\nj'ai une commande caché a vous de la retrouvé (si vous la trouvé merci de ne pas spam, sinon ça sera un ban)\n\n**-------- copyright --------**\n\n©lasere"
    await ctx.send(aide)

@bot.command()
async def cc(ctx):
    await ctx.send(f"salut,comment ça vas {ctx.author.mention}")

@bot.command()
async def repeat(ctx, *,text):
    await ctx.send(text)

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
async def fun_fact(ctx):
    list = ["https://vm.tiktok.com/ZMR92tPUp/" , "https://www.youtube.com/watch?v=8W4oKiEQph0" , "https://vm.tiktok.com/ZMRbr1wfk/" , "https://vm.tiktok.com/ZMRbMnYXa/" , "https://vm.tiktok.com/ZMRbMcBcn/" , "https://vm.tiktok.com/ZMRbMGNxg/" , "https://vm.tiktok.com/ZMRbr8rW1/ \nvoila comment je vois jouer @Matt" , "https://vm.tiktok.com/ZMRbreT4f/" , "https://vm.tiktok.com/ZMRbMELYC/" , "https://vm.tiktok.com/ZMRbrderh/ \nquand ta encore l'ADSL" , "https://vm.tiktok.com/ZMRbrJYL7/ \n@Matt" , "https://vm.tiktok.com/ZMRbMsnTF/" , "https://vm.tiktok.com/ZMRbMvhwV/ \nPOV:ton pote viend de ta dire sa te dit on joue se soire" , "https://vm.tiktok.com/ZMRbrNPgo/" , "https://vm.tiktok.com/ZMRbM3PcF/ \nquand tu sais que tu vas passé une journé de merde" , "https://vm.tiktok.com/ZMRbrFLDn/"]
    await ctx.send(list[randint(0,len(list)-1)])

@bot.command()
async def dé(ctx):
    await ctx.send(randint(0,6))

@bot.command()
async def game(ctx, nombre : int):
    messages = nombre
    random = randint(0,6)
    if messages == random:
        await ctx.send("bien joué,ta gagné 😉")
    elif messages > 7:
        await ctx.send("le nombre doit être compris entre 0 et 6 ")
    else:
        await ctx.send("perdu tu peux retenter ta chance")
        await ctx.send(f"le nombre étais {random} et vous avez mis le nombre {messages}")

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

@bot.command()
async def meme(ctx):
    await ctx.send("voici le meme du serveur 𝐸𝓍𝓅𝑒́𝓇𝒾𝑒𝓃𝒸𝑒: \ntiktok: https://vm.tiktok.com/ZMR92tPUp/ \nyoutub: https://www.youtube.com/watch?v=8W4oKiEQph0 ")

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
