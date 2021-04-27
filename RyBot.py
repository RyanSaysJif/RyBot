# Invite link: https://discord.com/oauth2/authorize?client_id=835454389283192893&scope=bot&permissions=74752
# Version 0.1.0
import discord
intents = discord.Intents.default()
intents.members = True
max_messages = None

client = discord.Client(intents=intents)

#User ID constants:
ryan_user_id = '465396405880487936'
beau_user_id = '119659671882563584'

#Guild ID constant:
queercraft_guild_id = '119660540468396032'

#Channel ID constants:
introductions_channel_id = '545567998375624714'
bot_wrangling_channel_id = '361087387587051520'

#Error messages:
no_perms = 'You do not have permission to use that command!'
wrong_channel = 'You can not use that command in this channel!'

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.rybot foo'):
        if message.author.id == ryan_user_id:
            if message.channel.id == bot_wrangling_channel_id:
                await message.channel.send('bar')
            else:
                await message.channel.send(wrong_channel)
        else:
            message.channel.send(no_perms)
                                
    if message.content.startswith('.rybot purge'):
        if message.author.id == beau_user_id or message.author.id == ryan_user_id:
            if message.channel.id == introductions_channel_id:
                guild = client.get_guild(queercraft_guild_id)
                channel = client.get_channel(introductions_channel_id)
                num_deleted_messages = 0
                async for message in channel.history():
                    message_author_id = message.author.id
                    queried_message_id = message.id
                    if guild.get_member(target) is None:
                        num_deleted_messages += 1
                        print(num_deleted_messages)
                        print(message_author_id)
                        print(queried_message_id)
                        await message.delete()
                user = await client.fetch_user(beau_user_id)
                if num_deleted_messages == 0:
                    await user.send(f'I found no messages to delete. If you believe this was in error, please contact <@!{ryan_user_id}> so he can fix me and we can try again. Otherwise, I will remain in your server until you type `.rybot leave`.')
                else:
                    await user.send(f'I found and deleted {num_deleted_messages} message(s) from users no longer in your server. I apologize for any spam this may have created in your audit channels.\n\nBecause my task is now complete, I have left your server. Please send any feedback to <@!{ryan_user_id}>.\n\nThank you, and have a wonderful day!')
                    await guild.leave()  
                print('Finished purge operation.')
                user = await client.fetch_user(ryan_user_id)
                await user.send(f'Found {num_deleted_messages} message(s) to delete.')
                                  
            else:
                await message.channel.send(wrong_channel)
        else:
            await message.channel.send(no_perms)

    if message.content.startswith('.rybot leave'):
        if message.author.id == beau_user_id or message.author.id == ryan_user_id:
            guild = client.get_guild(queercraft_guild_id)
            await message.channel.send('Thank you, and have a wonderful day!')
            await guild.leave()
        else:
            await message.channel.send(no_perms)

with open(BotToken.txt) as file:
    x = file.read()
client.run(x)
