"""
This functionality tracks student activity and rewards students
 with level ups. Students can track their activities with $level and see their
 progress towards the next level. The bot continually listens for user messages
 and adds it to the user's personal experience/level score
"""
from math import floor
import json
import os
from datetime import datetime
import discord
from discord.ext import commands

class userRanking(commands.Cog):
    """Class provides several methods to manage user ranking."""
    def __init__(self, client):
        cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.chdir(cur_dir)
        self.client = client

    @commands.Cog.listener()

    async def on_member_join(self, member):
        """
            Sees a user has joined and adds their information
            Parameters:
                self: used to access parameters passed to the class through
                member: used to access the values passed through the current context
        """
        with open('./data/participation/users.json', 'r', encoding='utf-8') as file:
            users = json.load(file)

        await self.update_data(users, member)

        with open('./data/participation/users.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)

    @commands.Cog.listener()
    async def on_message(self, message):
        """
            Sees a user has messaged and adds their information
            Parameters:
                self: used to access parameters passed to the class through
                message: used to access the values passed through the current context
        """
        if not message.author.bot:
            cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            os.chdir(cur_dir)
            with open('./data/participation/users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
            await self.update_data(users, message.author)
            await self.add_experience(users, message.author)
            await self.level_up(message, users)

            with open('./data/participation/users.json', 'w', encoding='utf-8') as file:
                json.dump(users, file, indent=4)

    async def update_data(self, users, user):
        """
            Updates the data of the user
            Parameters:
                self: used to access parameters passed to the class through
                users: the json file
                user: the user
        """
        if not str(user.id) in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 0
            users[str(user.id)]['level'] = 1

    async def add_experience(self, users, user):
        """
            Adds experience to the user
            Parameters:
                self: used to access parameters passed to the class through
                users: the json file
                user: the user
        """
        users[str(user.id)]['experience'] += 15

    async def level_up(self, ctx, users):
        """
            Levels up a user
            Parameters:
                self: used to access parameters passed to the class through
                ctx: used to access the values passed through the current context
                users: the json file
        """
        user = ctx.author
        experience = users[str(user.id)]['experience']
        lvl = users[str(user.id)]['level']
        lvl_end = 5 * (lvl ** 2) + (50 * lvl) + 100

        if lvl_end <= experience:
            channel = discord.utils.get(ctx.guild.channels, name="general")
            await channel.send('{} has levelled up to level {} ! 🙌'.format(user.mention, lvl + 1))
            # .format(user.mention, lvl + 1))
            users[str(user.id)]['level'] = lvl + 1
            users[str(user.id)]['experience'] -= lvl_end

    async def to_integer(self, dt_time):
        """
            Gets an integer from a date/time
            Parameters:
                self: used to access parameters passed to the class through
                dt_time: the time
            Returns:
                an integer of delay
        """
        answer = 100000000 * dt_time.year + 1000000 * \
                 dt_time.month + 10000 * dt_time.day + 100 * dt_time.hour + dt_time.minute
        return int(answer)

    @commands.command()
    async def level(self, ctx, user: discord.Member = None):
        """
            Presents level information about a user
            Parameters:
                self: used to access parameters passed to the class through
                ctx: used to access the values passed through the current context
                user: the discord member
        """
        with open('./data/participation/users.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
        await ctx.send('Contribute more to level up!')
        if user is None:
            if not str(ctx.author.id) in users:
                users[str(ctx.author.id)] = {}
                users[str(ctx.author.id)]['experience'] = 0
                users[str(ctx.author.id)]['level'] = 0

            user = ctx.author
            lvl = int(users[str(ctx.author.id)]['level'])
            exp = int(5 * (lvl ** 2) + (50 * lvl) + 100)  # XP cap
            experience = int(users[str(user.id)]['experience'])
            boxes = floor((experience * 20) / exp)
            embed = discord.Embed(Title=f"**{user}'s Rank**",
                                  Description=f"Experience: {lvl}/{exp}", color=0x0091ff)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.add_field(name=f"**{user}'s Rank**",
                            value="🙌  ", inline=False)
            embed.add_field(name="Level",
                            value=f"**{users[str(user.id)]['level']}**", inline=True)
            embed.add_field(name="Experience",
                            value=f"**{str(int(users[str(user.id)]['experience']))} / {exp}**",
                            inline=True)
            embed.add_field(name="Progress Bar",
                            value=boxes * ":blue_square:" + (20 - boxes) *
                                    ":white_large_square:", inline=False)
            embed.set_footer(text=f"next level: {lvl + 1}")
            await ctx.send(embed=embed)

        else:
            if not str(user.id) in users:
                users[str(user.id)] = {}
                users[str(user.id)]['experience'] = 0
                users[str(user.id)]['level'] = 0
                users[str(user.id)]['LastMessage'] = await self.to_integer(datetime.now())
            lvl = int(users[str(user.id)]['level'])
            exp = int(5 * (lvl ** 2) + (50 * lvl) + 100)
            experience = int(users[str(user.id)]['experience'])
            boxes = floor((experience * 20) / exp)

            embed = discord.Embed(Title=f"**{user}'s Rang**",
                                  Description=f"Experience: {lvl}/"
                                              f"{5 * (lvl ** 2) + (50 * lvl) + 100}",
                                  color=0x0091ff)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.add_field(name=f"**{user}'s Rang**", value="🙌  ", inline=False)
            embed.add_field(name="Level",
                            value=f"**{users[str(user.id)]['level']}**", inline=True)
            embed.add_field(name="Experience",
                            value=f"**{str(int(users[str(user.id)]['experience']))} / {exp}**",
                            inline=True)
            embed.add_field(name="Progress Bar",
                            value=boxes * ":blue_square:" + (20 - boxes) *
                                  ":white_large_square:", inline=False)
            embed.set_footer(text=f"next level: {lvl + 1}")
            await ctx.send(embed=embed)

        with open('./data/participation/users.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)

    @commands.command()
    async def add_database(self, ctx, user: discord.Member):
        """
            Adds user to the database
            Parameters:
                self: used to access parameters passed to the class through
                ctx: used to access the values passed through the current context
                user: the discord member to be added
        """
        with open('./data/participation/users.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
        if not str(user.id) in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 0
            users[str(user.id)]['level'] = 0
            users[str(user.id)]['LastMessage'] = await self.to_integer(datetime.now())
            await ctx.send("added to database!")
        else:
            await ctx.send("already in database!")

        with open('./data/participation/users.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)

def setup(bot):
    """
        Adds the cog to the bots list
        Parameters:
            bot: the bot adding the cog
    """
    bot.add_cog(userRanking(bot))
