#Invite link: https://discord.com/oauth2/authorize?client_id=835454389283192893&scope=bot&permissions=74752
import discord
intents = discord.Intents.default()
intents.members = True
max_messages = None

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #Stops the bot from activating itself.
    if message.author == client.user:
        return

    #Can be used in bot-wrangling by Ryan to make sure the bot is responsive.
    if message.content.startswith('.rybot foo'):
        if message.author.id == 465396405880487936:
                if message.channel.id == 361087387587051520:
                    await message.channel.send('bar')
                                
    #This  will start the process to delete all messages in the introductions channel by users who are no longer in the server.
    if message.content.startswith('.rybot purge'):
        #Limits the command to only user Beau or Ryan.
        if message.author.id == 119659671882563584 or message.author.id == 465396405880487936:
            #Limits the command to the introductions channel.
            if message.channel.id == 545567998375624714:
                #Stores the server.
                guild = client.get_guild(119660540468396032)
                #Stores the channel ID.
                channel = client.get_channel(545567998375624714)
                #Initiates a counter for the number of deleted messages.
                counter = 0
                async for message in channel.history():
                    #Stores the user ID of the author of the current message.
                    target = message.author.id
                    #Stores the message ID of the current message.
                    subject = message.id
                    #Checks for message author user IDs that do not match the list of current guild member IDs.
                    if guild.get_member(target) is None:
                        counter += 1
                        #Prints the number, userID, and messageID of each deleted message in terminal. For verification while the process is running.
                        print(counter)
                        print(target)
                        print(subject)
                        #Fetches the message ID of the currently processed message.
                        await channel.fetch_message(subject)
                        await message.delete()
                #Fetches Beaupedia's user ID.
                user = await client.fetch_user(119659671882563584)
                #Sends Beaupedia the results once the process has finished.
                if counter == 0:
                    await user.send('I found no messages to delete. If you believe this was in error, please contact <@!465396405880487936> so he can fix me and we can try again. Otherwise, I will remain in your server until you type `.rybot leave`.')
                else:
                    await user.send(f'I found and deleted {counter} message(s) from users no longer in your server. I apologize for any spam this may have created in your audit channels.\n\nBecause my task is now complete, I have left your server. Please send any feedback to <@!465396405880487936>.\n\nThank you, and have a wonderful day!')
                    #Leaves the guild, as this is bot is currently designed for one-time use.
                user = await client.fetch_user(465396405880487936)
                    await user.send(f'Found {counter} message(s) to delete.')
                    await guild.leave()                
            else:
                await message.channel.send('That command may not be run in this channel.')
        else:
            await message.channel.send('You do not have permission to use this command.')

    if message.content.startswith('.rybot leave'):
        if message.author.id == 119659671882563584 or message.author.id == 465396405880487936:
            guild = client.get_guild(119660540468396032)
            await message.channel.send('Thank you, and have a wonderful day!')
            await guild.leave()
        else:
            await message.channel.send('You do not have permission to use this command.')

client.run('<Bot Token>')
