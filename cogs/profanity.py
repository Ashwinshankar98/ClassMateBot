# Copyright (c) 2021 War-Keeper
"""This file contains serval methods to greet Hello"""

from operator import contains
from discord.ext import commands
from better_profanity import profanity
profanity.load_censor_words()


class Profanity(commands.Cog):
    """Class which deltes profane words and custom profane words"""
    def __init__(self, bot):
        self.bot = bot
        self.custom_words = []

    @commands.Cog.listener()
    async def on_message(self, message):
        if profanity.contains_profanity(message.content):
            await message.channel.send(message.author.name + ' says: ' +
                profanity.censor(message.content))
            print(profanity.censor(message.content))
            await message.delete()
        else:
            print(self.custom_words)
            if message in self.custom_words:
                await message.channel.send(message.author.name + 'says: ' +
                    '****')
                await message.delete()        

    # ------------------------------------------------------------------------------------------------------------------
    #    Function: on_message_edit
    #    Description: checks for profane words if certain messages have been edited
    #    Inputs:
    #    - member: before and after states of the edited message
    #    Outputs:
    #    -
    # ------------------------------------------------------------------------------------------------------------------

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        ''' run on message edited '''
        if profanity.contains_profanity(after.content):
            await after.channel.send(after.author.name + ' says: ' +
                profanity.censor(after.content))
            await after.delete()
        else:
            if after in self.custom_words:
                await after.channel.send(after.author.name + 'says' +
                    '****')
                await after.delete()        


    @commands.command(help='Add a word to be declared as profane from here on out')
    async def custom(self, ctx, text):
        if text in self.custom_words:
            await ctx.send("Already Added!!")
        else:
            self.custom_words.append(text)
            await ctx.message.delete()
            await ctx.send("Word added to custom profanity filter")


def setup(bot):
    """add the file to the bot's cog system"""
    bot.add_cog(Profanity(bot))
