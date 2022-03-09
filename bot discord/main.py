import discord
from discord.ext import commands
from sty import fg, bg, ef, rs



#créeation de Kyla
Kyla=commands.Bot(command_prefix='Kyla.')

Condanation={}

#quand Kyla se reveil
@Kyla.event
async def on_ready():
    print("Kyla est reveillé, Bonsoir :>")
    await Kyla.change_presence(status=discord.Status.do_not_disturb,
                               activity=discord.Game("la Creation"))
    return

#les commandes
@Kyla.command()
async def Magie(ctx):
    print("lol")
    await ctx.send(f"Dans ce monde 12 Magies régne sur le monde:\n"
                   f"•Le Feu\n"
                   f"•L'Eau\n"
                   f"•La Foudre\n"
                   f"•Le Vent\n"
                   f"•La Roche\n"
                   f"•Le Chao\n"
                   f"•La Lumiere\n"
                   f"•L'Ombre\n"
                   f"•La Galaxie\n"
                   f"•Les Illusions\n"
                   f"•Les Bêtes\n"
                   f"•Les Réves/Cauchemars\n")
    return

@Kyla.event
async def on_member_join(member):
    print("oui")
    salon : discord.TextChannel = Kyla.get_channel(885250133414002718)
    await salon.send(f"Nous faitons aujourd'hui la Naissance de {member.display_name}, Un jours ta magie se révélera aussi, voix sa dans le salon dédier")
    await salon.send(f"Bienvenu très cher/s hésite pas a jeté un oeuil a tes magie et autre :>")
    return

#Ajouter un role, par contre pas reussi le enlever
@Kyla.event
async def on_raw_reaction_add(payload):
    emoji=payload.emoji.name
    Salon=payload.channel_id
    Message=payload.message_id
    Member=payload.member
    roles= Kyla.get_guild(payload.guild_id).roles

    if Salon == 865705929391865887 and Message ==866106717493526528 :
        if emoji == "Fire":
            Fire = roles[12]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Water":
            Fire = roles[11]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Thunder":
            Fire = roles[10]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Wind":
            Fire = roles[9]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Chao":
            Fire = roles[8]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Rock":
            Fire = roles[7]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Life":
            Fire = roles[6]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Death":
            Fire = roles[5]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Galaxy":
            Fire = roles[4]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Illusion":
            Fire = roles[3]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Beast":
            Fire = roles[2]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
        elif emoji == "Dream":
            Fire = roles[1]
            await Member.add_roles(Fire)
            await Member.send("Obtien La Bennediction du dieux du feu, très Cher")
    return

#BOOM SANCTION
@Kyla.command()
@commands.has_role("Moi Teddy")
async def Jugement(ctx, oui: discord.Member):
    pseud= oui.mention
    Id= oui.id

    if Id not in Condanation:
        Condanation[Id] = 0
        print("remier enrengistrement de sanction")

    Condanation[Id] +=1

    if Condanation[Id] == 1:
        await ctx.send(f"{pseud} Vous avez été reconnu couplable de votre actes, le conceil vous averti de me pas recommencer, sinon votre ame serra purger a jamais, on vous laisse encore 2chance")
    elif Condanation[Id] == 2:
        await ctx.send(f"Très Cher {pseud}, c'est la deuxieme fois que nous nous retrouvons pour parler de votre comportement, je tien a vous prévenir que la prochaine fois, vous vous en sortirais pas avec un simple message, au revoir!")
    else:
        await ctx.send(f"entendez vous le bruit de ses Cloche? IL EST HEURE POUR UNE EXECUTION")
        await oui.send("La prochaine fois que vous voudrez troubler l'équilibre de quelque chose, vous y réfléchirait avant :>")
        await oui.kick()
        await ctx.send(f"{pseud} a été executé au nom de l'équilibre :>")
    return

@Jugement.error
async  def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Je ne peux juger qui que se soit sans savoir qui sais et ce qu'il a fait, un jugement doit respecter des rêgle")
    return

@Jugement.error
async  def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Seul le conceil des 12 peuvent Juger du jugement d'une peine")
    return



#Connection de Kyla sur le Server
CléServer= "ODY1NjcxOTg3NjE5Mjk5Mzkw.YPHZ3Q.2FiaKR5u7596SMgDt14qVJbE4Os"
print("Veuillez accueillir le Créateur du monde")
Kyla.run(CléServer)
