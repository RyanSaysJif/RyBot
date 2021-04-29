# Invite link: https://discord.com/oauth2/authorize?client_id=835454389283192893&scope=bot&permissions=74752
# Version 1.1.1
import sys
import discord
import datetime
intents = discord.Intents.default()
intents.members = True
max_messages = None

client = discord.Client(intents=intents)

#User ID constants. Set these as needed.:
dev_id = 465396405880487936
owner_user_id = 119659671882563584

#Channel ID constants. Set these as needed. Audit channel is preferably a staff-only channel.
target_channel_id = 545567998375624714
audit_channel_id = 361087387587051520
test_channel_id = 835434576708894730

#Error messages:
no_perms = 'You do not have permission to use that command!'
wrong_channel = 'You can not use that command in this channel!'

bot_prefix = '.rybot'

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_guild_join(guild):
    await guild.owner.send('Hello there! My name is RyBot, a custom made bot for your server!\n\nCommand prefix:`.rybot`\n\nThe following commands are currently available:\n`omnomnom`: **O**ld **M**essages **N**ow **O**bsolete **M**eaning **N**o **O**vert **M**ass - Deletes messages in the channel by users no longer in your Discord server. This program currently runs only in your #introductions channel.\n`leave`: You wouldn\'t really do this to me, would you?')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(f'{bot_prefix} foo'):
        await message.delete(delay=5)
        if message.author.id == dev_id:
            await message.channel.send('bar', delete_after=5)
        else:
            await message.channel.send(no_perms, delete_after=5)
                                
    if message.content.startswith(f'{bot_prefix} omnomnom'):
        await message.delete()
        if message.author.id == message.guild.owner_id or message.author.id == dev_id:
            if message.channel.id == target_channel_id or message.channel.id == test_channel_id:
                guild = message.guild.id
                channel = message.channel
                stdout_fileno = sys.stdout
                sys.stdout = open('Output.log', 'a')
                num_deleted_messages = 0
                async for message in channel.history(oldest_first=True):
                    message_author_id = message.author.id
                    queried_message_id = message.id
                    if message.guild.get_member(message.author.id) is None:
                        num_deleted_messages += 1
                        dt = datetime.datetime.now()
                        dt_string = dt.strftime('%d/%m/%Y %H:%M:%S')
                        sys.stdout.write(f'{dt_string} - Deleted message in {message.guild}:{message.channel}({message.guild.id}:{message.channel.id}) from {message.created_at} UTC by {message.author}({message.author.id}) saying:\n\"{message.content}\"' + '\n')
                        await message.delete()
                sys.stdout.close()
                sys.stdout = stdout_fileno
                user = await client.fetch_user(owner_user_id)
                if num_deleted_messages == 0:
                    await message.guild.owner.send(f'I found no messages to delete. If you believe this was in error, please contact <@!{dev_id}> so he can fix me and we can try again. Otherwise, I will remain in your server until you type `.rybot leave`.')
                    user = await client.fetch_user(dev_id)
                    await user.send(f'Found no messages to delete.')
                else:
                    await message.guild.owner.send(f'I found and deleted {num_deleted_messages} message(s) from users no longer in your server. I apologize for any spam this may have created in your audit channels.\n\nBecause my only function is now complete, I have left your server. Please send any feedback to <@!{dev_id}>.\n\nThank you, and have a wonderful day!')
                    print('Finished purge operation.')
                    user = await client.fetch_user(dev_id)                   
                    await user.send(f'Found {num_deleted_messages} message(s) to delete.')
                    await message.guild.leave()
            else:
                await message.channel.send(wrong_channel, delete_after=5)
        else:
            await message.channel.send(no_perms, delete_after=5)

    if message.content.startswith(f'{bot_prefix} leave'):
        await message.delete(delay=5)
        if message.author.id == owner_user_id or message.author.id == dev_id:
            await message.channel.send('Thank you, and have a wonderful day!')
            await message.guild.leave()
        else:
            await message.channel.send(no_perms, delete_after=5)

with open('BotToken.txt') as file:
    x = file.read()
client.run(x)
