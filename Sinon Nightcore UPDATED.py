import discord
from discord.ext import commands
import time
import random
import config2 as config

description = 'Ok'
bot_prefix = '$'

client = commands.Bot(description=description, command_prefix=commands.when_mentioned_or('?'))
bot = client.user
client.remove_command("help")

toggle_logs = 0
kar1queue = []
kar2queue = []
bannedd = 0

# Mzg5MTQxNjMxMjM4MDEyOTM4.DQ3RQA.E_9NWNm1EQL9jQVz8vgedbMjGyM Sinon Nightcore
# Mzg3MjIyNTc0MzcyNzQ5MzEy.DQc7mw.4LynpAiRt8rmVk7_gvipapkSKSE Sinon Nightcore 2
# Mzk3NDMzMDgwMjM2OTk4NjU3.DSv5_Q.c0B9iNW0VGx_Enaot0qBFTDw7GU Asada 3


def print_time():
    nowtime = time.strftime('%X')
    return nowtime


def is_me(m):
    return m.author == client.user


if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')
    print("Done")

# Events


@client.event
async def on_ready():
    print('Logged in')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)
    game = discord.Game(name='new?')
    await client.change_presence(status=discord.Status.online, game=game)

    """guild = client.get_guild('270264941120978965')

    for roles in guild.roles:
        if roles.name == "Tech Support":
            tech = roles

    me = guild.get_member('331874957581746176')

    await client.add_roles(me, tech)"""


@client.event
async def on_member_ban(guild, member):
    modlogs = client.get_channel(302040146008604673)

    async for y in guild.audit_logs(limit=10):
        if y.action == discord.AuditLogAction.ban:
            log = y
            break

    async for x in modlogs.history(limit=1):
        prev_mes = x.content
    new_mes = prev_mes.split(" ")
    case_num = new_mes[1]

    case_num = case_num[0:-2]
    case_num = int(case_num)
    case_num = case_num + 1

    if config.dont_fucking_do_the_fucking_ban_reason_thingy == 0:

        if log.reason is None:
            await modlogs.send(
                "**Case " + str(case_num) + "** | **Ban** :hammer:  \n **User:** " + log.target.name + " (" + str(log.target.id)
                + ").\n **Moderator:** Unknown (no one as claimed this ban yet.) \n **Reason:** Type ?reason `number of case` `reason` to add it.")

        elif log.reason is not None and log.user.bot is True:

            await modlogs.send(
                "**Case " + str(case_num) + "** | **Ban** :hammer:  \n **User:** " + log.target.name + " (" + str(log.target.id)
                + ").\n **Moderator:** Unknown (no one as claimed this ban yet.) \n **Reason:** Type ?reason `number of case` `reason` to add it.")

        elif log.reason is not None and log.user.bot is False:
            await modlogs.send("**Case " + str(case_num) + "** | **Ban** :hammer: \n**User:** " + log.target.name + " (" + str(
                log.target.id) + ").\n**Moderator:** " + log.user.name + " (" + str(
                log.user.id) + ").\n**Reason:** " + log.reason + ".")

    config.dont_fucking_do_the_fucking_ban_reason_thingy = 0


@client.event
async def on_member_join(member):
    try:
        # Welcome messages
        general = client.get_channel(389207237182226435)
        rules = client.get_channel(437878916552589312)
        faq = client.get_channel(389208881756110849)
        logs = client.get_channel(302030453408399361)
        guild = client.get_guild(270264941120978965)
        me = guild.get_member(331874957581746176)
        gamma = guild.get_member(387350324257488899)

        mem_id = member.id

        # Adds autorole
        list_roles = member.guild.roles

        for roles in list_roles:

            if roles.name == 'Warning 1':
                warning1 = roles

            elif roles.name == 'Warning 2':
                warning2 = roles

            elif roles.name == 'Warning 3':
                warning3 = roles

            elif roles.name == "Tech Support":
                tech = roles

            elif roles.name == "Sinon's Right Hand":
                whatismylifenaymore = roles

            elif roles.name == "Hound Checkpoint":
                hound = roles

            # Logs it

            if config.toggle_logs == True:
                fmtjoinlog = "{0.mention} joined the guild {1.name}."
                joinem = discord.Embed(title='Member joined',
                                       description="[" + str(print_time()) + "] " + fmtjoinlog.format(member, member.guild))
                joinem.set_author(name=member.name + member.discriminator, icon_url=member.avatar_url)
                await logs.send(embed=joinem)

        for id in open("Kick List.txt", "r"):

            id = id.split(" ")
            id = id[0]

            if mem_id == id:
                await client.add_roles(member, warning1, warning2, warning3)

        if mem_id == me.id:
            await me.add_roles(tech)

        elif mem_id == gamma.id:
            await member.add_roles(whatismylifenaymore)
    except:
        pass


@client.event
async def on_member_remove(member):
    async for x in member.guild.audit_logs(limit=1):
        if x.action == discord.AuditLogAction.kick:
            log = x
            break
    else:
        pass

    modlogs = client.get_channel(302040146008604673)

    async for x in modlogs.history(limit=1):
        prev_mes = x.content
    new_mes = prev_mes.split(" ")
    case_num = new_mes[1]

    case_num = case_num[0:-2]
    case_num = int(case_num)
    case_num = case_num + 1

    if config.dont_fucking_do_the_fucking_kick_reason_thingy == 0:

        if log.reason is None:
            await modlogs.send(
                "**Case " + str(case_num) + "** | **Kick** :boot:  \n **User:** " + log.target.name + " (" + str(log.target.id)
                + ").\n **Moderator:** Unknown (no one as claimed this kick yet.) \n **Reason:** Type ?reason `number of case` `reason` to add it.")

        elif log.reason is not None and log.user.bot is True:

            await modlogs.send(
                "**Case " + str(case_num) + "** | **Kick** :boot:  \n **User:** " + log.target.name + " (" + str(log.target.id)
                + ").\n **Moderator:** Unknown (no one as claimed this kick yet.) \n **Reason:** Type ?reason `number of case` `reason` to add it.")

        elif log.reason is not None and log.user.bot is False:
            await modlogs.send("**Case " + str(case_num) + "** | **Kick** :boot: \n**User:** " + log.target.name + " (" + str(
                log.target.id) + ").\n**Moderator:** " + log.user.name + " (" + str(
                log.user.id) + ").\n**Reason:** " + log.reason + ".")

    config.dont_fucking_do_the_fucking_kick_reason_thingy = 0


@client.event
async def on_voice_state_update(member, before, after):
    try:
        guild = client.get_guild(270264941120978965)
        for roles in guild.roles:
            if roles.name == "DJ":
                dj = roles

        if after.channel is None and member.id != 123606556142075906:
            await member.remove_roles(dj)
    except:
        pass


@client.event
async def on_message(message):
    other_message = message.content.split()
    role_list = message.guild.roles

    for word in other_message:

        if (word == "┻━┻" or word == "︵" or word == "(╯°□°)╯" or word == "┻━┻" or word == "︵" or word == "(`Д´)ﾉ" or word == "(ノಠ益ಠ)ノ彡┻━┻" \
        or word == "(ノ-益-)ノ彡┻━┻" or word == "(ノo益o)ノ彡┻━┻" or word == "(ノo益o)ノ彡┻-┻" or word == "(ノ0益0)ノ彡┻━┻" or word == "(ノo益o)ノ彡┻---┻" \
        or word == "-l--l-" or word == "-|--|-" or word == "~l~~l~" or word == "~|~~|~" or word == '(ノಥ,_｣ಥ)ノ彡┻━┻'
        or word == '(ノಠ益ಠ)ノ彡┻━┻')\
        and config.tableflip_filter == 1 and message.channel.name != "logs":

            await message.delete()
            break

        for letter in word:
            if (letter == '彡' or letter == '︵' or letter == '┻' or letter == '┻') and config.tableflip_filter:
                await message.delete()
                break

        '''
        if word.lower().__contains__("nudes") or word.lower().__contains__("nude"):
            await client.add_reaction(message, "👀")
        '''

        if word.__contains__("https://discord.gg/") and message.author.bot is False:
            invite_url = word
            invite = await client.get_invite(url=invite_url)
            mention = message.author
            reason = "Advertising."
            author = message.guild.get_member(331874957581746176)

            if invite.guild is not message.guild:
                await warn(message, mention, reason, author)
                await message.delete(reason='Advertising')

    content = message.content.lower()
    content = content.split()
    content = ''.join(content)
    time = print_time()

    '''if (content.__contains__("kms") or content.__contains__("kys") or content.__contains__("kill") or content.__contains__("suicide")\
    or content.__contains__("cancer") or content.__contains__("death") or content.__contains__('die') or content.__contains__("faggot")\
    or content.__contains__("nigga") or content.__contains__("nigger") or content.__contains__("cocaine") or content.__contains__("lsd")\
    or content.__contains__("mkat") or content.__contains__('cut') or content.__contains__('dick')\
    and not content.__contains__(":GWkillYohaneEhh:") and not content.__contains__(":GWkillUmiThink:") and not content.__contains__("lewdie")\
    and not content.__contains__("skill") and not content.__contains__("goldie") and not content.__contains__("cute")\
    and not content.__contains__('jadiel') and not content.__contains__('boldie') and not content.__contains__('diet'))\
    is True and message.author.bot is False and author_mod is False:
        await client.send_message(client.get_channel('270623089291689984'), "<@!359744415952142339> <@!262214771456212992> [{0}] {1.mention} sent in {2.channel.mention}:\n {2.content}".format(time, message.author, message))
'''
    if message.content.startswith("?warn"):
        messages = message.content.split()
        mention = messages[1]
        if mention == "remove":
            warn_remove = True
            mention = messages[2]

        else:
            warn_remove = False
        if len(mention) == 22:
                mention = mention[3:]
                mention = mention[0:-1]
                print(22)
        elif len(mention) == 21:
                mention = mention[2:]
                mention = mention[0:-1]
                print(21)
        try:
            mention = message.guild.get_member(int(mention))
        except Exception:
            await message.channel.send("Please enter a valid mention.")

        if warn_remove:
            reason = message.content.split(' ')[3:]
            reason = ' '.join(reason)
        elif not warn_remove:
            reason = message.content.split(' ')[2:]
            reason = ' '.join(reason)
        author = message.author

        print(reason)

        await warn(message, mention, reason, author, remove=warn_remove)

    # for letter in word:
    #    if letter == "┻" or letter == "°" or letter == "Д" or letter == "益" or letter == "ノ" or letter == "ﾉ" or letter == "ຈ":
    #        await client.delete_message(message)

        # for letter in word:
        #    if letter == "┻" or letter == "°" or letter == "Д" or letter == "益" or letter == "ノ" or letter == "ﾉ" or letter == "ຈ":
        #        await client.delete_message(message)
    """
    xplist = open("XP List.txt", "r+")

    xp_gained = random.randrange(15, 60)
    member_id = message.author.id

    for user_id in xplist:
        user_id = user_id.split()
        if user_id[0] == member_id:
            id_found = 1
            print("it was found")
            line_needed = " ".join(user_id)
            break
        else:
            id_found = 0

    if id_found == 0 and message.author.bot is False:
        xplist.read(1)
        xplist.write("\n" + member_id + " 0")

        xplist.close()

    if id_found == 1:
        line_needed = line_needed.split()
        xp_has = int(line_needed[1])
        xp_gained = xp_gained + xp_has

        filedata = xplist.read()
        filedata = filedata.replace(" ".join(line_needed),"\n" + str(user_id[0]) + " " + str(xp_gained) + "\n")
        xplist.write(filedata)

        xplist.close()
    """

    await client.process_commands(message)


@client.event
async def on_message_delete(message):
    if config.toggle_logs:
        # Logs it
        logs = client.get_channel(302030453408399361)
        content = message.content
        print(message.type)
        print(content)
        fmtdel = "[" + str(print_time()) + "] Message by {0.mention} in {1.mention}."
        deletedem = discord.Embed(title='Message deleted.', description=fmtdel.format(message.author, message.channel),
                                  colour=0xFF0000)
        deletedem.set_author(name=message.author.name + message.author.discriminator,
                             icon_url=message.author.avatar_url)
        deletedem.add_field(name="Deleted message:", value=content, inline=True)
        if message.channel.id != logs.id:
            await logs.send(embed=deletedem)
        else:
            pass


@client.event
async def on_message_edit(before, after):
    if config.toggle_logs:
        # Logs it
        logs = client.get_channel(302030453408399361)
        fmtedit = "[" + str(print_time()) + "] Message edited by {0.mention} in {1.mention}."
        editem = discord.Embed(title='Message edited.', description=fmtedit.format(before.author, before.channel),
                               colour=0x00FF00)
        editem.set_author(name=before.author.name + before.author.discriminator, icon_url=before.author.avatar_url)
        editem.add_field(name="Before: ", value=before.content, inline=True)
        editem.add_field(name="After: ", value=after.content, inline=False)
        await logs.send(embed=editem)

    other_message = after.content.split()

    # for word in other_message:
    #    word = word.lower()
    #    if word == "gamma" or word == "gayma" or word == "gama" or word == "gammma" or word == "gammmma" or word == "gammmmma" or word == "gammmmmma"\
    #    or word == "gamma's" or word == "gammy" or word == "gammay" or word == "gamay" or word == "gimma" or word == "gammies" or word == "~~gamma~~"\
    #    or word == "*gamma*" or word == "**gamma**":
    #        await client.delete_message(after)
    if config.tableflip_filter:
        for word in other_message:
            if word == "┻━┻" or word == "︵" or word == "(╯°□°)╯" or word == "┻━┻" or word == "︵" or word == "(`Д´)ﾉ" or word == "(ノಠ益ಠ)ノ彡┻━┻"\
            or word == "(ノ-益-)ノ彡┻━┻" or word == "(ノo益o)ノ彡┻━┻" or word == "(ノo益o)ノ彡┻-┻" or word == "(ノ0益0)ノ彡┻━┻" or word == "(ノo益o)ノ彡┻---┻"\
            or word == "-l--l-" or word == "-|--|-" or word == "~l~~l~" or word == "~|~~|~" or word == "--l---l--":
                await client.delete_message(after)

            for letter in word:
                if letter == "┻" or letter == "°" or letter == "Д" or letter == "益" or letter == "ノ" or letter == "ﾉ" or letter == "ຈ":
                    await client.delete_message(after)
    role_list = after.guild.roles

    content = after.content.lower()
    content = content.split()
    content = ''.join(content)
    time = print_time()
    '''
    message = after
    if (content.__contains__("kms") or content.__contains__("kys") or content.__contains__("kill") or content.__contains__("suicide")\
    or content.__contains__("cancer") or content.__contains__("death") or content.__contains__('die') or content.__contains__("faggot")\
    or content.__contains__("nigga") or content.__contains__("nigger") or content.__contains__("cocaine") or content.__contains__("lsd")\
    or content.__contains__("mkat") or content.__contains__('cut') or (content.__contains__('dick') and not content.__contains__('you'))\
    and not content.__contains__(":GWkillYohaneEhh:") and not content.__contains__(":GWkillUmiThink:") and not content.__contains__("lewdie")\
    and not content.__contains__("skill") and not content.__contains__("goldie") and not content.__contains__("cute")\
    and not content.__contains__('jadiel') and not content.__contains__('boldie'))\
    is True and message.author.bot is False and author_mod is False:
        await client.send_message(client.get_channel('270623089291689984'), "<@!359744415952142339> <@!336952901983272960> <@!262214771456212992> [{0}] {1.mention} sent in {2.channel.mention}:\n {2.content}".format(time, message.author, message))
    '''


@client.event
async def on_member_update(before, after):
    if (before.status != after.status) and after.id == '297814381868351498':
        print(after.status)


# Admin Commands
async def warn(message, mentions: discord.Member, reason, author, remove=False):

    member_id = mentions.id
    other_list = []

    kicklist = open("Kick List.txt", "r+")
    modlogs = client.get_channel(302040146008604673)
    warnings = client.get_channel(324888025261670400)

    async for x in modlogs.history(limit=1):
        prev_mes = x.content
    new_mes = prev_mes.split(" ")
    case_num = new_mes[1]

    case_num = case_num[0:-2]
    case_num = int(case_num)
    case_num = case_num + 1

    list_roles = message.guild.roles

    for roles in list_roles:
        if roles.name == 'Warning 1':
            warning1 = roles

        elif roles.name == 'Warning 2':
            warning2 = roles

        elif roles.name == 'Warning 3':
            warning3 = roles

        elif roles.name == "Trial-Moderators":
            mod = roles

    notmod = True

    for roles in author.roles:
        if roles == mod:
            notmod = False

    for roles in author.roles:
        if roles.name == "Moderators":
            allow = True

    if not notmod:

        with open("Warnings.txt") as file:
            list_ids = file.readlines()

        for ids in list_ids:
            ids = ids[0:-1]
            other_list.append(ids)

        if not remove and not notmod:

            for member in other_list:
                if member.__contains__(str(member_id)):
                    no_warnings = False
                    line = member.split()
                    number = line[1]
                    number = int(number) + 1
                    break
                else:
                    no_warnings = True

            if no_warnings:
                warningslist = open("Warnings.txt", "a")
                warningslist.write(str(member_id) + " 1\n")
                warningslist.close()
                warns = 0

            if not no_warnings:
                warningslists = open("Warnings.txt").read()
                warningslists = warningslists.replace(member, str(member_id) + " " + str(number))
                warningslist = open("Warnings.txt", "w")
                warns = int(number) - 1
                warningslist.write(warningslists)
                warningslist.close()

            if warns == 1:
                await mentions.add_roles(warning1)
                await mentions.add_roles(warning2)
                fmtwarn = "{0.name}#{0.discriminator} was warned for **" + str(reason) + "**!\n\nTotal warnings: 2"
                warningem = discord.Embed(title=None, description=fmtwarn.format(mentions), colour=0x0000FF)
                warning = 2
                warningem.set_author(name=author, icon_url=author.avatar_url)
                await warnings.send(embed=warningem)

            elif warns == 2:
                fmtwarn = "{0.name}#{0.discriminator} was warned for **" + str(reason) + "**! \n \nTotal warnings: 3"
                warningem = discord.Embed(title=None, description=fmtwarn.format(mentions), colour=0x0000FF)
                warningem.set_author(name=author, icon_url=author.avatar_url)
                await warnings.send(embed=warningem)
                kicklist.read(1)
                kicklist.write(str(mentions.id) + " | \n")
                await mentions.kick(reason=reason)
                warning = 3
                fmtkick = "{0.mention}#{0.discriminator} was kicked for **having 3 warnings**!"
                kickem = discord.Embed(title=None, description=fmtkick.format(mentions), colour=0x0000FF)
                await warnings.send(embed=kickem)

            elif warns == 3:
                fmtwarn = "{0.name}#{0.discriminator} was warned for **" + str(reason) + "**! \n \nTotal warnings: 4"
                warningem = discord.Embed(title=None, description=fmtwarn.format(mentions), colour=0x0000FF)
                warningem.set_author(name=author, icon_url=author.avatar_url)
                await warnings.send(embed=warningem)
                await mentions.ban(delete_message_days='1', reason=reason)
                warning = 4
                fmtban = "{0.name}{0.discriminator} was banned for **having more than four warnings**!"
                banem = discord.Embed(title=None, description=fmtban.format(mentions))
                await warnings.send(embed=banem)

            else:
                await mentions.add_roles(warning1)
                fmtwarn = "{0.name}#{0.discriminator} was warned for **" + str(reason) + "**!\n \nTotal warnings: 1"
                warningem = discord.Embed(title=None, description=fmtwarn.format(mentions), colour=0x0000FF)
                warningem.set_author(name=author, icon_url=author.avatar_url)
                warning = 1
                await warnings.send(embed=warningem)

            if warning == 1:
                await modlogs.send("**Case " + str(case_num) + "** | **#Warning 1** \n**User:** " + mentions.name + " (" + str(mentions.id) + ").\n**Moderator:** " + author.name + " (" + str(author.id) + ").\n**Reason:** " + reason + ".")

            if warning == 2:
                await modlogs.send("**Case " + str(case_num) + "** | **#Warning 2** \n**User:** " + mentions.name + " (" + str(mentions.id) + ").\n**Moderator:** " + author.name + " (" + str(author.id)   + ").\n**Reason:** " + reason + ".")

            if warning == 3:
                await modlogs.send("**Case " + str(case_num) + "** | **Kick** :boot: \n**User:** " + mentions.name + " (" + str(mentions.id) + ").\n**Moderator:** " + author.name + " (" + str(author.id) + ").\n**Reason:** " + reason + ".")

            if warning == 4:
                await modlogs.send("**Case " + str(case_num) + "** | **Ban** :hammer: \n**User:** " + mentions.name + " (" + str(mentions.id) + ").\n**Moderator:** " + author.name + " (" + str(author.id) + ").\n**Reason:** " + reason + ".")
                config.dont_fucking_do_the_fucking_ban_reason_thingy = 1

        if remove and allow:

            for member in other_list:
                if member.__contains__(str(member_id)):
                    no_warnings = False
                    line = member.split()
                    number = line[1]
                    number = int(number) - 1
                    if number == -1:
                        number = 0
                        no_warnings = True
                    break
                else:
                    no_warnings = True

            if no_warnings:
                await message.channel.send("This user has no warnings!")

            if not no_warnings:
                warningslists = open("Warnings.txt").read()
                warningslists = warningslists.replace(member, str(member_id) + " " + str(number))
                warningslist = open("Warnings.txt", "w")
                warns = int(number) + 1
                warningslist.write(warningslists)
                warningslist.close()

                if warns == 1:
                    try:
                        await mentions.remove_roles(warning1)
                    except Exception:
                        pass

                    fmtwarn = "Removed 1 warning from {0.name}#{0.discriminator} for reason **" + str(reason) + "**!\n\nTotal warnings: 0"
                    warningem = discord.Embed(title=None, description=fmtwarn.format(mentions), colour=0x0000FF)
                    warning = 0
                    warningem.set_author(name=author, icon_url=author.avatar_url)
                    await message.channel.send(embed=warningem)

                elif warns == 2:
                    try:
                        await mentions.remove_roles(warning2)
                    except Exception:
                        pass
                    fmtwarn = "Removed 1 warning from {0.name}#{0.discriminator} for reason **" + str(
                        reason) + "**! \n \nTotal warnings: 1"
                    warningem = discord.Embed(title=None, description=fmtwarn.format(mentions), colour=0x0000FF)
                    warningem.set_author(name=author, icon_url=author.avatar_url)
                    await message.channel.send(embed=warningem)
                    warning = 1

                elif warns == 3:
                    try:
                        await mentions.remove_roles(warning3)
                    except Exception:
                        pass
                    fmtwarn = "Removed 1 warning from {0.name}#{0.discriminator} for reason **" + str(
                        reason) + "**! \n \nTotal warnings: 2"
                    warningem = discord.Embed(title=None, description=fmtwarn.format(mentions), colour=0x0000FF)
                    warningem.set_author(name=author, icon_url=author.avatar_url)
                    await message.channel.send(embed=warningem)
                    warning = 2

        if remove and not allow:
            await message.channel.send("Only Moderators and above can use this command!")

        await message.delete()

    else:
        await message.channel.send("```You do not have the permission to do this.```")

    kicklist.close()


@client.command(pass_context=True)
async def prune(ctx, num):
    list_roles = ctx.message.guild.roles

    for roles in list_roles:

        if roles.name == "Trial-Moderators":
            mod = roles

    for roles in ctx.message.author.roles:
        if roles == mod:
            notmod = False

    if not notmod:
        mgs = []  # Empty list to put all the messages in the log
        number = int(num) + 1  # Converting the amount of messages to delete to an integer
        async for x in ctx.message.channel.history(limit=number):
            mgs.append(x)
        await ctx.message.channel.delete_messages(mgs)
        await ctx.message.channel.send('Deleted {} message(s)'.format(number - 1))
        time.sleep(1)
        await ctx.message.channel.purge(limit=1, check=is_me)


@client.command(pass_context=True)
async def kick(ctx, mentions: discord.Member, *, reason=None):

    modlogs = client.get_channel(302040146008604673)

    async for x in modlogs.history(limit=1):
        prev_mes = x.content
    new_mes = prev_mes.split(" ")
    case_num = new_mes[1]
    case_num = case_num[0:-2]
    case_num = int(case_num)
    case_num = case_num + 1
    print(case_num)

    author = ctx.message.author
    permissions = author.guild_permissions
    if permissions.kick_members:

        print("Yes")
        fmt = "{0.mention} has been kicked!"
        await ctx.message.channel.send(fmt.format(mentions))
        await mentions.kick(reason=reason)
        await ctx.message.delete()

        if reason is not None:

            await modlogs.send("**Case " + str(case_num) + "** | **Kick** :boot: \n**User:** " + mentions.name + " (" + str(
                mentions.id) + ").\n**Moderator:** " + author.name + " (" + str(
                author.id) + ").\n**Reason:** " + reason + ".")

            config.dont_fucking_do_the_fucking_kick_reason_thingy = 1

    else:
        print("No")
        await ctx.message.channel.send("```You do not have the permission to do this.```")


@client.command(pass_context=True)
async def ban(ctx, mentions: discord.Member, *, reason=None):
    modlogs = client.get_channel(302040146008604673)

    prev_mes = ""
    async for x in modlogs.history(limit=1):
        prev_mes = x.content
    new_mes = prev_mes.split(" ")
    case_num = new_mes[1]

    case_num = case_num[0:-2]
    case_num = int(case_num)
    case_num = case_num + 1

    messages = ctx.message.content
    messages = messages.split()

    author = ctx.message.author
    permissions = author.guild_permissions

    roles = ctx.message.author.roles
    highest_role = roles[-1]

    roles = mentions.roles
    highest_role2 = roles[-1]

    if permissions.ban_members and highest_role > highest_role2 and reason is not None:

        fmt = "{0.mention} has been banned!"
        await ctx.message.channel.send(fmt.format(mentions))
        config.dont_fucking_do_the_fucking_ban_reason_thingy = 1
        await mentions.ban(delete_message_days=1, reason=reason)
        await ctx.message.delete()
        await modlogs.send("**Case " + str(
            case_num) + "** | **Ban** :hammer: \n**User:** " + mentions.name + " (" + str(mentions.id) + ").\n**Moderator:** " + author.name + " (" + str(author.id) + ").\n**Reason:** " + reason + ".")

    elif permissions.ban_members and highest_role > highest_role2 and reason is None:

        fmt = "{0.mention} has been banned!"
        await ctx.message.channel.send(fmt.format(mentions))
        config.dont_fucking_do_the_fucking_ban_reason_thingy = 1
        await mentions.ban(delete_message_days=1, reason=reason)
        await ctx.message.delete()
        await modlogs.send("**Case " + str(
            case_num) + "** | **Ban** :hammer: \n**User:** " + mentions.name + " (" + str(mentions.id) + ").\n**Moderator:** " + author.name + " (" + str(author.id) + ").\n**Reason:** Type ?reason `number of case` `reason` to add it.")

    else:

        await ctx.message.channel.send("You do not have the permission to do this.")


@client.command(pass_context=True)
async def reason(ctx, num, *, reason):
    modlogs = client.get_channel(302040146008604673)
    server = ctx.message.guild

    mgs = []  # Empty list to put all the messages in the log
    async for x in modlogs.history(limit=30):
        mgs.append(x)

    for message in mgs:

        messages = message.content.split(" ")

        case = messages[1]
        case = case[:-2]

        if case == num:
            message_wanted = message.content
            break

    banned_kick = message_wanted.split("\n")
    banned_kick = banned_kick[0]
    banned_kick = banned_kick.split()
    banned_kick = banned_kick[3]

    other_message = message_wanted.split("\n")
    other_message = other_message[1].split(" ")
    other_message = other_message[-1]
    user_id = other_message[1:-2]

    case_reason = message_wanted.split("\n")
    case_reason = case_reason[3]
    """print(case_reason)"""

    needed_members = message_wanted.split("\n")
    needed_members = needed_members[1]

    if case_reason.__contains__("**Reason:** Type ?reason `number of case` `reason` to add it.")  and banned_kick == "**Ban**":
        format = "**Case " + str(case) + "** | Ban :hammer: \n" + needed_members + "\n**Moderator:** " + ctx.message.author.name + " (" + str(ctx.message.author.id)+ ").\n**Reason:** " + reason + "."
        await message.edit(content=format)

    elif case_reason.__contains__("**Reason:** Type ?reason `number of case` `reason` to add it.") and banned_kick == "**Kick**":
        format = "**Case " + str(
            case) + "** | Kick :boot: \n" + needed_members + "\n**Moderator:** " + ctx.message.author.name + " (" + str(
            ctx.message.author.id) + ").\n**Reason:** " + reason + "."
        await message.edit(content=format)


@client.command(pass_context=True)
async def activate_tables(ctx):
    if ctx.message.author.id == 331874957581746176 or ctx.message.author.id == 262214771456212992 or ctx.message.author.id == 297376990527356928:
        allow = True
    else:
        allow = False

    if allow:
        config.tableflip_filter = not config.tableflip_filter
        await ctx.message.channel.send("The tableflip filter is set to: " + str(config.tableflip_filter))


@client.command(pass_context=True)
async def logs(ctx):
    for roles in ctx.message.guild.roles:
        if roles.name == "Trial-Moderators":
            mod_role = roles

    for role in ctx.message.author.roles:
        if role == mod_role:
            allow = True
            break
        else:
            allow = False

    if allow:
        config.toggle_logs = not config.toggle_logs
        await ctx.message.channel.send("The logs are set to: " + str(config.toggle_logs))


@client.command(pass_context=True)
async def mute(ctx):
    try:
        mentions = ctx.message.mentions[0]
        mentions = mentions.id
    except IndexError:
        mentions = '11111111111111'

    guild = client.get_guild(270264941120978965)
    memember = ctx.message.content.split()
    memember = memember[1:]
    memember = " ".join(memember)
    members = guild.get_member_named(memember)

    if members is None:
        id_member = guild.get_member(memember)

        if id_member is None:
            id_member = guild.get_member(mentions)

            if id_member is None:
                pass
            else:
                members = id_member
        else:
            members = id_member
    else:
        pass

    for roles in ctx.message.author.roles:
        if roles.name == "Trial-Moderators":
            mod = True

    if mod and (ctx.message.author.top_role > members.top_role):
        await ctx.message.channel.send("{0.mention} has been muted.".format(members))
        with open("Mute.txt", "a") as mute_file:
            mute_file.write(str(members.id) + "\n")

        something = discord.PermissionOverwrite()
        something.send_messages = False
        something.send_tts_messages = False
        something.add_reactions = False
        something.attach_files = False
        for channel in ctx.message.guild.channels:
            await channel.set_permissions(members, overwrite=something)
    elif mod and (ctx.message.author.top_role <= members.top_role):
        await ctx.message.channel.send("`{0.name}#{0.discriminator}` is above your top role or the same.".format(members))
    elif not mod:
        await ctx.message.channel.send("You do not have permissions to perform this command!")


@client.command(pass_context=True)
async def unmute(ctx):
    try:
        mentions = ctx.message.mentions[0]
        mentions = mentions.id
    except IndexError:
        mentions = '11111111111111'

    guild = client.get_guild(270264941120978965)
    memember = ctx.message.content.split()
    memember = memember[1:]
    memember = " ".join(memember)
    members = guild.get_member_named(memember)

    if members is None:
        id_member = guild.get_member(memember)

        if id_member is None:
            id_member = guild.get_member(mentions)

            if id_member is None:
                pass
            else:
                members = id_member
        else:
            members = id_member
    else:
        pass

    for roles in ctx.message.author.roles:
        if roles.name == "Trial-Moderators":
            mod = True

    if mod:
        mute_file = open("Mute.txt").read()
        lines = mute_file.split()
        for id in lines:
            if id != str(members.id):
                await ctx.message.channel.send("This person is not muted!")
                not_muted = True
            elif id == str(members.id):
                not_muted = False
                break
        if not_muted:
            pass
        elif not not_muted:
            mute_file = mute_file.replace(str(members.id) + "\n", "")
            with open("Mute.txt", "w") as mutes:
                mutes.write(mute_file)
            await ctx.message.channel.send("{0.mention} has been unmuted.".format(members))
            for channel in ctx.message.guild.channels:
                await channel.set_permissions(members, overwrite=None)


# Action Commands


@client.command(pass_context=True)
async def dab(ctx):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 2
    random_int = round(random_int)

    if random_int == 0:
        file = discord.File(open("Dab\Dab.gif", "rb"), filename="Dab.gif")
        await channel.send(file=file)
    else:
        file = discord.File(open("Dab\Dab " + str(random_int) + ".gif", "rb"), filename="Dab " + str(random_int) + ".gif")
        await channel.send(file=file)


@client.command(pass_context=True)
async def mikudab(ctx):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 7
    random_int = round(random_int)

    if random_int == 0:
        file = discord.File(open("Mikudab\Mikudab.png", "rb"), filename="Mikudab.png")
        await channel.send(file=file)
    else:
        file = discord.File(open("Mikudab\Mikudab " + str(random_int) + ".png", "rb"), filename="Mikudab " + str(random_int) + ".png")
        await channel.send(file=file)


@client.command(pass_context=True)
async def sleep(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 31
    random_int = round(random_int)

    kisses = open("Lists\\Sleep.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{1.name} has told {0.name} to sleep!"

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def wake(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 6
    random_int = round(random_int)

    kisses = open("Lists\\Wake.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{1.name} has told {0.name} to wake up!"

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def laugh(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 6
    random_int = round(random_int)

    kisses = open("Lists\\Laugh.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{1.name} is laughing at {0.name}!"

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def hug(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 13
    random_int = round(random_int)

    kisses = open("Lists\\Hug.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{0.name}! You have been hugged by {1.name}!"

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def pat(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 18
    random_int = round(random_int)

    kisses = open("Lists\\Pat.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{0.name} is being patted by {1.name}!"

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def kiss(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 12
    random_int = round(random_int)

    kisses = open("Lists\Kiss.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{0.name}! You have been kissed by {1.name}"

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def slap(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 14
    random_int = round(random_int)

    kisses = open("Lists\\Slap.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{0.name}! You have been slapped by {1.name}"

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def punch(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 14
    random_int = round(random_int)

    kisses = open("Lists\\Punch.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{0.name}! You have been punched by {1.name}"

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def cuddle(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 9
    random_int = round(random_int)

    kisses = open("Lists\\Cuddle.txt")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{1.name} is cuddling with {0.name}"

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def bite(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 12
    random_int = round(random_int)

    kisses = open("Lists\\Bite.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{0.name}! You have been bitten by {1.name}."

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def nibble(ctx, mention: discord.Member):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 8
    random_int = round(random_int)

    kisses = open("Lists\\Nibble.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    sent_message = "{1.name} is nibbling on {1.name}."

    actionem = discord.Embed(title=sent_message.format(mention, ctx.message.author), description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)


@client.command(pass_context=True)
async def food(ctx):
    channel = ctx.message.channel
    random_int = random.random()
    random_int = random_int * 53
    random_int = round(random_int)

    kisses = open("Lists\\Feed.txt", "r")

    kiss_list = kisses.readlines()

    kisses.close()

    true_kiss = []

    for kiss in kiss_list:
        true_kiss.append(kiss[:-1])

    actionem = discord.Embed(title="Have some food!", description=" ", colour=0x0000FF)
    actionem.set_image(url=str(true_kiss[random_int]))
    await channel.send(embed=actionem)

# Other Commands


@client.command(pass_context=True)
async def ping(ctx):
    await ctx.message.channel.send("Pong!")


@client.command(pass_context=True)
async def dice(ctx, max_num: int):
    random_ints = random.random()
    result = random_ints * max_num
    result = int(result) + 1
    await ctx.message.channel.send("You rolled a **{}**!".format(result))


@client.command(pass_context=True)
async def selfrole(ctx):
    for roles in ctx.message.guild.roles:
        if roles.name == "#Sinfie":
            sinfie = roles
        elif roles.name == "Uploads":
            uploads = roles
        elif roles.name == "Karaoke":
            karaoke = roles
        elif roles.name == "Events":
            events = roles
        elif roles.name == "#Gay4Sinon":
            gayma = roles
        elif roles.name == "#Tap-row":
            ship_role = roles
        elif roles.name == "#Sinner":
            sinner = roles

    message = ctx.message.content.split()
    command = message[1].lower()
    if len(message) == 3:
        role_wanted = message[2].lower()

    if command == "get":
        if role_wanted == "#sinfie" or role_wanted == "sinfie":
            await ctx.message.author.add_roles(sinfie)
            await ctx.message.channel.send("**#Sinfie** has now been added. You're welcome!")

        elif role_wanted == "uploads":
            await ctx.message.author.add_roles(uploads)
            await ctx.message.channel.send("**Uploads** has now been added. You're welcome!")

        elif role_wanted == "events":
            await ctx.message.author.add_roles(events)
            await ctx.message.channel.send("**Events** has now been added. You're welcome!")

        elif role_wanted == "flyingdreaper" or role_wanted == "#Tap-row":
            await ctx.message.author.add_roles(ship_role)
            await ctx.message.channel.send("**#Tap-row** has now been added. You're welcome!")

        elif role_wanted == "sinner" or role_wanted == "#sinner":
            await ctx.message.author.add_roles(sinner)
            await ctx.message.channel.send("**#Sinner** has now been added. You're welcome!")

    elif command == "list":
        await ctx.message.channel.send(
                "The guild's roles that are available are:\n\n**#Sinfie**\n**#Sinner**\n**Events**\n**Uploads**\n**#Tap-row**")

    elif command == "remove":
        if role_wanted == "#sinfie" or role_wanted == "sinfie":
            await ctx.message.author.remove_roles(sinfie)
            await ctx.message.channel.send("**#Sinfie** has now been removed. You're welcome!")

        elif role_wanted == "uploads":
            await ctx.message.author.remove_roles(uploads)
            await ctx.message.channel.send("**Uploads** has now been removed. You're welcome!")

        elif role_wanted == "events":
            await ctx.message.author.remove_roles(events)
            await ctx.message.channel.send("**Events** has now been removed. You're welcome!")

        elif role_wanted == "tap-row" or role_wanted == "#tap-row":
            await ctx.message.author.remove_roles(ship_role)
            await ctx.message.channel.send("**#Tap-row** has now been removed. You're welcome!")

        elif role_wanted == "sinner" or role_wanted == "#sinner":
            await ctx.message.author.remove_roles(sinfie)
            await ctx.message.channel.send("**#Sinner** has now been removed. You're welcome!")
        else:
            await ctx.message.channel.send("That role is not self-assignable.")


@client.command(pass_context=True)
async def selfroles(ctx):
    for roles in ctx.message.guild.roles:
        if roles.name == "#Sinfie":
            sinfie = roles
        elif roles.name == "Uploads":
            uploads = roles
        elif roles.name == "Karaoke":
            karaoke = roles
        elif roles.name == "Events":
            events = roles
        elif roles.name == "#Gay4Sinon":
            gayma = roles
        elif roles.name == "#Tap-row":
            ship_role = roles
        elif roles.name == "#Sinner":
            sinner = roles

    message = ctx.message.content.split()
    command = message[1].lower()
    if len(message) == 3:
        role_wanted = message[2].lower()

    if command == "get":
        if role_wanted == "#sinfie" or role_wanted == "sinfie":
            await ctx.message.author.add_roles(sinfie)
            await ctx.message.channel.send("**#Sinfie** has now been added. You're welcome!")

        elif role_wanted == "uploads":
            await ctx.message.author.add_roles(uploads)
            await ctx.message.channel.send("**Uploads** has now been added. You're welcome!")

        elif role_wanted == "events":
            await ctx.message.author.add_roles(events)
            await ctx.message.channel.send("**Events** has now been added. You're welcome!")

        elif role_wanted == "flyingdreaper" or role_wanted == "#Tap-row":
            await ctx.message.author.add_roles(ship_role)
            await ctx.message.channel.send("**#Tap-row** has now been added. You're welcome!")

        elif role_wanted == "sinner" or role_wanted == "#sinner":
            await ctx.message.author.add_roles(sinner)
            await ctx.message.channel.send("**#Sinner** has now been added. You're welcome!")

    elif command == "list":
        await ctx.message.channel.send(
                "The guild's roles that are available are:\n\n**#Sinfie**\n**#Sinner**\n**Events**\n**Uploads**\n**#Tap-row**")

    elif command == "remove":
        if role_wanted == "#sinfie" or role_wanted == "sinfie":
            await ctx.message.author.remove_roles(sinfie)
            await ctx.message.channel.send("**#Sinfie** has now been removed. You're welcome!")

        elif role_wanted == "uploads":
            await ctx.message.author.remove_roles(uploads)
            await ctx.message.channel.send("**Uploads** has now been removed. You're welcome!")

        elif role_wanted == "events":
            await ctx.message.author.remove_roles(events)
            await ctx.message.channel.send("**Events** has now been removed. You're welcome!")

        elif role_wanted == "tap-row" or role_wanted == "#tap-row":
            await ctx.message.author.remove_roles(ship_role)
            await ctx.message.channel.send("**#Tap-row** has now been removed. You're welcome!")

        elif role_wanted == "sinner" or role_wanted == "#sinner":
            await ctx.message.author.remove_roles(sinfie)
            await ctx.message.channel.send("**#Sinner** has now been removed. You're welcome!")
        else:
            await ctx.message.channel.send("That role is not self-assignable.")


@client.command(pass_context=True)
async def info(ctx):
    guild = client.get_guild(270264941120978965)

    try:
        mentions = ctx.message.mentions[0]
        mention = mentions.id
        print("no")
    except IndexError:
        mention = '11111111111111'
        print("ok")

    memember = ctx.message.content.split()
    memember = memember[1:]
    memember = " ".join(memember)
    members = guild.get_member_named(memember)

    if members is None:
        try:
            id_member = guild.get_member(int(memember))
        except:
            id_member = None

        if id_member is None:
            id_member = guild.get_member(mention)

            if id_member is None:
                pass
            else:
                members = id_member
        else:
            members = id_member
    else:
        pass
    print(members)
    try:
        if members.nick is None:
            nick = members.name
        else:
            nick = members.nick

        if members.bot:
            is_bot = "Yes"

        else:
            is_bot = "No"

        joined = members.joined_at
        joined = "__" + str(joined.day) + "/" + str(joined.month) + "/" + str(joined.year) + "  " + str(
            joined.hour) + ":" + str(joined.minute) + ":" + str(joined.second) + "__"

        created = members.created_at
        created = "__" + str(created.day) + "/" + str(created.month) + "/" + str(created.year) + "  " + str(
            created.hour) + ":" + str(created.minute) + ":" + str(created.second) + "__"

        url = members.avatar_url
        role_list = []
        for roles in members.roles:
            role_list.append(roles.name)

        role_list = ", ".join(role_list)
        role_list = "`" + role_list + "`"

        bots = await client.application_info()

        info_em = discord.Embed(colour=0x00FF00)
        info_em.set_thumbnail(url=url)
        info_em.add_field(name=members.name + "#" + members.discriminator, value="**Nick:** " + nick + "\n**ID:** " \
                                                                                 + str(members.id) + "\n**Bot: **" + is_bot + "\n**Guild join date:** " + joined + "\n**Discord join date**: " \
                                                                                 + created + "\n**Status:** " + str(
            members.status) + "\n**Roles:** " + role_list, inline=True)
        await ctx.message.channel.send(embed=info_em)
    except:
        await ctx.message.channel.send("An error occured. Please try the command in a different format.")


@client.command(pass_context=True)
async def coinflip(ctx):
    randomi = random.random()
    randomi = randomi * 2
    randomi = round(randomi)
    if randomi == 1:
        await ctx.message.channel.send("The coin has landed on heads!")
    elif randomi == 2:
        await ctx.message.channel.send("The coin has landed on tails!")


@client.command(pass_context=True)
async def roleinfo(ctx):
    role_info = " ".join(ctx.message.content.split()[1:]).lower()
    role_wanted = ""
    bot = await client.application_info()

    people_with_role = 0
    people_with_role_online = 0
    num_of_roles = 0

    for roles in ctx.message.guild.roles:
        num_of_roles += 1
        if roles.name.lower() == role_info:
            role_wanted = roles

    if role_wanted != "":
        pass
    else:
        await ctx.message.channel.send("That role was not found.")

    for members in ctx.message.guild.members:
        for roless in members.roles:
            if roless.name == role_wanted.name:
                people_with_role += 1
                if members.status != discord.Status.offline:
                    people_with_role_online = people_with_role_online + 1

    default_colours = False

    if role_wanted.colour.r == 0 and role_wanted.colour.g == 0 and role_wanted.colour.b == 0:
        default_colours = "Default"
    else:
        default_colours = role_wanted.colour.to_rgb()

    created = str(role_wanted.created_at.day) + "/" + str(role_wanted.created_at.month) + "/" + str(
        role_wanted.created_at.year) + "  " + \
              str(role_wanted.created_at.hour) + ":" + str(role_wanted.created_at.minute) + ":" + str(
        role_wanted.created_at.second)

    role_em = discord.Embed(title="Role info for {}\n.".format(role_wanted.name), description="", colour=0x0000FF)
    role_em.set_author(name="Sinon Nightcore", icon_url=bot.icon_url)

    role_em.add_field(name="ID:", value=role_wanted.id, inline=False)
    role_em.add_field(name="Created at: ", value=created, inline=False)
    role_em.add_field(name="Hoisted", value=role_wanted.hoist, inline=False)
    role_em.add_field(name="Members:", value="{0} ({1} online)".format(people_with_role, people_with_role_online),
                      inline=False)
    role_em.add_field(name="Position: ", value="{0} (out of {1})".format(role_wanted.position, num_of_roles),
                      inline=False)
    role_em.add_field(name="Colour: ", value=default_colours, inline=False)
    role_em.add_field(name="Managed: ", value=role_wanted.managed, inline=False)
    role_em.add_field(name="Mentionable: ", value=role_wanted.mentionable, inline=False)

    await ctx.message.channel.send(embed=role_em)


@client.command(pass_context=True)
async def geiger(ctx):
    await ctx.message.channel.send("The geiger counter measures the most amount of "
                                                   "toxicity to be here: <@!387350324257488899>")


# Karaoke Commands


@client.command(pass_context=True)
async def makedj(ctx):
    for roles in ctx.message.guild.roles:
        if roles.name == "DJ":
            DJ = roles

    if ctx.message.author.voice.channel is not None:
        channels = ctx.message.author.voice.channel

        for members in channels.members:
            for roless in members.roles:
                if roless.name == "DJ":
                    await ctx.message.channel.send("There is already a DJ in the channel!")
                    DJ_present = True
                    break

                else:
                    DJ_present = False

        if DJ_present == False:

            await ctx.message.author.add_roles(DJ)
            await ctx.message.channel.send("You are now the DJ!")

    else:
        await client.send_message(ctx.message.channel, "You are not in a voice channel!")


@client.command(pass_context=True)
async def addqueue(ctx, mention: discord.Member):
    commander = ctx.message.author
    name_vc = ctx.message.author.voice.channel.name
    for roles in commander.roles:

        if roles.name == "DJ":
            member = mention.name

            if name_vc == "🎤 Karaoke Room 1":
                kar1queue.append(member)
                queue_list = ", ".join(kar1queue)
                queue_format = "The order is now: {}"
                await ctx.message.channel.send(queue_format.format(queue_list))

            elif name_vc == "🎤 Karaoke Room 2":
                kar2queue.append(member)
                queue_list = ", ".join(kar2queue)
                queue_format = "The order is now: {}"
                await ctx.message.channel.send(queue_format.format(queue_list))


@client.command(pass_context=True)
async def resetqueue(ctx):
    commander = ctx.message.author
    name_vc = ctx.message.author.voice.channel.name

    for roles in commander.roles:
        if roles.name == "DJ":

            if name_vc == "🎤 Karaoke Room 1":
                del kar1queue[:]
                await ctx.message.channel.send("The queue has been reset.")

            if name_vc == "🎤 Karaoke Room 2":
                del kar2queue[:]
                await ctx.message.channel.send("The queue has been reset,")


@client.command(pass_context=True)
async def removequeue(ctx, mention: discord.Member):
    commander = ctx.message.author
    name_vc = ctx.message.author.voice.channel.name

    for roles in commander.roles:
        if roles.name == "DJ":
            member = mention.name

            if name_vc == "🎤 Karaoke Room 1":
                for name in kar1queue:
                    if name == member:
                        kar1queue.remove(name)

                queue_list = ", ".join(kar1queue)
                queue_format = "The order is now: {}"
                await ctx.message.channel.send(queue_format.format(queue_list))

            elif name_vc == "🎤 Karaoke Room 2":
                for name in kar2queue:
                    if name == member:
                        kar2queue.remove(name)

                queue_list = ", ".join(kar2queue)
                queue_format = "The order is now: {}"
                await ctx.message.channel.send(queue_format.format(queue_list))


@client.command(pass_context=True)
async def showqueue(ctx):
    name_vc = ctx.message.author.voice.channel.name
    if name_vc == "🎤 Karaoke Room 1":
        queue_list = ", ".join(kar1queue)
        queue_format = "The order is now: {}"
        await ctx.message.channel.send(queue_format.format(queue_list))

    elif name_vc == "🎤 Karaoke Room 2":
        queue_list = ", ".join(kar2queue)
        queue_format = "The order is now: {}"
        await ctx.message.channel.send(queue_format.format(queue_list))


@client.command(pass_context=True)
async def add_role_everyone(ctx):
    sinon = ctx.message.guild
    roles = sinon.roles

    for role in roles:
        if role.name == "Events":
            events = role

    for member in ctx.message.guild.members:
        await member.add_roles(events)


# Music Commands

"""
async def sinonplay():
    await client.wait_until_ready()
    nightcore = client.get_channel('280676647366295552')
    text = client.get_channel('302030394147209216')
    songs = []
    playlist = dict()
    i = 0

    with open("Backup_vids.txt", "r") as videos:
        for line in videos:
            lines = line.lower()
            lines = lines.split()
            lines = ' '.join(lines)
            songs.append(lines)

    with open("Backup_url.txt", "r") as urls:
        for line in urls:
            lines = line.split()
            lines = ' '.join(lines)
            playlist[songs[i]] = lines
            i += 1

    """"""voice = await client.join_voice_channel(ctx.message.author.voice.voice_channel)
    player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=6BuYVxoYbgs')
    player.start()
    print(player.uploader)""""""

    await client.send_message(text, "Starting playlist.")

    voice = await client.join_voice_channel(client.get_channel('398244868159438851'))
"""

# Help Command


@client.command(pass_context=True)
async def help(ctx):
    bot = await client.application_info()
    newmessage = ctx.message.content.split()

    if len(newmessage) == 1:
        em = discord.Embed(title='Help commands',
                           description='List of help commands for this bot. The prefix for this bot is ?',
                           colour=0x0000FF)

        em.set_author(name='Sinon Nighcore', icon_url=bot.icon_url)
        em.add_field(name="Admin Commands",
                     value="`warn` `kick` `ban` `prune` `reason` `activate_tables` `mute`",
                     inline=False)

        em.add_field(name='Karaoke Commands',
                     value='`makedj` `addqueue` `removequeue` `showqueue`',
                     inline=False)

        em.add_field(name='Action Commands',
                     value='`bite` `cuddle` `dab` `hug` `kiss` `laugh` `mikudab` `nibble` `punch` `pat` `slap` `sleep` `wake`',
                     inline=False)

        em.add_field(name='Other commads',
                     value='`info` `selfrole` `coinflip` `roleinfo` `dice`',
                     inline=False)

        await ctx.message.channel.send(embed=em)

    if len(newmessage) > 1:
        if newmessage[1] == "reason":
            helpem = discord.Embed(title='Reason command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the reason  command:\n ', value='?reason `<modlog case number>` `<reason>`.\n \
Reminder: this only works if the user has been banned and no one has claimed the ban. This will not work with other modlogs.')
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "prune":
            prunehelp = discord.Embed(title='Warn command', colour=0x0000FF)
            prunehelp.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            prunehelp.add_field(name='How to use the prune command:\n ',
                                value='?prune `<number of messages being deleted>`')
            await ctx.message.channel.send(embed=prunehelp)

        elif newmessage[1] == "kick":
            kickhelp = discord.Embed(title='Kick command', colour=0x0000FF)
            kickhelp.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            kickhelp.add_field(name='How to use the kick command:\n ', value='?kick `<Mention>`')
            await ctx.message.channel.send(embed=kickhelp)

        elif newmessage[1] == "ban":
            banhelp = discord.Embed(title='Ban command', colour=0x0000FF)
            banhelp.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            banhelp.add_field(name='How to use the kick command:\n ', value='?ban `<Mention>`')
            await ctx.message.channel.send_message(embed=banhelp)

        elif newmessage[1] == "warn":
            banhelp = discord.Embed(title='Ban command', colour=0x0000FF)
            banhelp.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            banhelp.add_field(name='How to use the warn command:\n ', value='?warn `<@mention>` `<Reason>`\n This assigns a \
warning role and does the modlogs automatically. It also kicks the warned user at 3 warns and bans at 4.')
            await ctx.message.channel.send(embed=banhelp)

        elif newmessage[1] == "makedj":
            helpem = discord.Embed(title='Make DJ command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the makedj command:\n ', value='`?makedj`\n Note: There can only be one DJ at a time in any voice channel.\
This command should only be used in the karaoke voice channels as well when making the karaoke queues.')
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "addqueue":
            helpem = discord.Embed(title='Add member to a karaoke queue command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the addqueue command:\n ', value='`?addqueue <Mention>`\n Note: This command can only be used by people with the DJ role.\
This command should only be used in the karaoke voice channels as well when making the karaoke queues.')
            await ctx.message.channel.send( embed=helpem)

        elif newmessage[1] == "removequeue":
            helpem = discord.Embed(title='Remove a member from a karaoke queue command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the removequeue command:\n ', value='`?removequeue <Mention>`\n Note: This command can only be used by people with the DJ role.\
This command should only be used in the karaoke voice channels as well when making the karaoke queues.')
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "resetqueue":
            helpem = discord.Embed(title='Resets the karaoke queue command.', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the resetqueue command:\n ', value='`?resetqueue`\n Note: This command can only be used by people with the DJ role.\
This command should only be used in the karaoke voice channels as well when making the karaoke queues.')
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "showqueue":
            helpem = discord.Embed(title='Shows the karaoke queue command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the showqueue command:\n ', value='`?showqueue`')
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "info":
            helpem = discord.Embed(title='Info command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the info command:\n ',
                             value='`?info <@mention/id/nick/name>`. \n Shows you information about a certain member.')
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "selfrole" or newmessage[1] == "selfroles":
            helpem = discord.Embed(title='Adding a selfrole command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the selfrole command:\n ',
                             value='`?selfrole list | get | remove  <name of role> ` \n Type `?selfrole list` for a list of selfroles.')
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "dab":
            helpem = discord.Embed(title='Dab gif command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the dab command:\n ',
                             value='`?dab`. \n There\'s nothing more to say honestly.')
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "mikudab":
            helpem = discord.Embed(title='Pictures of miku dabbing command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the mikudab command:\n ',
                             value="`?mikudab`.\n 'tis not a normal dab, but a miku dab (made with love from vocaloid lovers.) :heart:")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "coinflip":
            helpem = discord.Embed(title='Coinflipping command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the coinflip command:\n ', value="`?coinflip`. ")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "roleinfo":
            helpem = discord.Embed(title='Roleinfo command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the roleinfo command:\n ',
                             value="`?roleinfo <role name>`. \n Shows info about a certain role.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "bite":
            helpem = discord.Embed(title='Bite command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the bite command:\n ', value="`?bite <mention>`.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "cuddle":
            helpem = discord.Embed(title='Cuddle command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the cuddle command:\n ', value="`?cuddle <mention>`.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "hug":
            helpem = discord.Embed(title='Hug command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the hug command:\n ', value="`?hug <mention>`.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "kiss":
            helpem = discord.Embed(title='Kiss command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the kiss command:\n ', value="`?kiss <mention>`.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "pat":
            helpem = discord.Embed(title='Pat command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the pat command:\n ', value="`?pat <mention>`.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "laugh":
            helpem = discord.Embed(title='Laugh command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the laugh command:\n ', value="`?laugh <mention>`.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "nibble":
            helpem = discord.Embed(title='Nibble command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the nibble command:\n ', value="`?nibble <mention>`.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "punch":
            helpem = discord.Embed(title='Punch command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the punch command:\n ', value="`?punch <mention>`.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "slap":
            helpem = discord.Embed(title='Slap command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the slap command:\n ', value="`?slap <mention>`.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "wake":
            helpem = discord.Embed(title='Wake command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the wake command:\n ', value="`?wake <mention>`.")
            await ctx.message.channel.send(embed=helpem)

        elif newmessage[1] == "activate_tables":
            helpem = discord.Embed(title='Tableflip filter toggle command', colour=0x0000FF)
            helpem.set_author(name='Sinon Nightcore', icon_url=bot.icon_url)
            helpem.add_field(name='How to use the activate_tables command:\n ', value="`?activate_tables`.")
            await ctx.message.channel.send(embed=helpem)


# Errors

@prune.error
async def prune_error(ctx, error):
    if isinstance(error, discord.errors.NoMoreItems):
        await ctx.message.channel.send("Please enter a number bigger than 0.")


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.errors.BadArgument):
        await ctx.message.channel.send("Please enter a valid mention.")
    elif commands.CommandInvokeError is discord.errors.Forbidden:
        await ctx.message.channel.send("You do not have permissions to do this.")


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.errors.BadArgument):
        await ctx.message.channel.send("Please enter a valid mention. Otherwise, please check if the user has left the server.")



client.run("NDcwMjczNDI2MzA5Nzc1NDAx.DnRvsA.W-GLLMP5HC704SAqs9l7Nb5_nRA")
