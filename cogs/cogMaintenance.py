import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class CogMaintenance(commands.Cog):
    """DM functionality"""
    def __init__(self, bot):
        self.bot = bot

    """
    Function: load
    Description: Command for loading a cog
    Inputs:
    - ctx: used to access the values passed through the current context
    - extension: name of the cog that is to be added
    Outputs:
    - response from bot
    """
    @commands.command(name='loadCog',help="loads a specific cog")
    @has_permissions(administrator=True)
    async def load(self,ctx,extension):
        self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(str(extension)+' cog has been added')


    """
    Function: unload
    Description: Command for unloading a cog
    Inputs:
    - ctx: used to access the values passed through the current context
    - extension: name of the cog that is to be removed
    Outputs:
    - response from bot
    """

    @commands.command(name='unloadCog',help="unloads a specific cog")
    @has_permissions(administrator=True)
    async def unload(self,ctx,extension):
        self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(str(extension)+' cog has been removed')

    """
    Function: reload
    Description: Command for reloading a cog after an update is made
    Inputs:
    - ctx: used to access the values passed through the current context
    - extension: name of the cog that is to be reloaded
    Outputs:
    - response from bot
    """
    @commands.command(name='reloadCog',help="reloads a specific cog")
    @has_permissions(administrator=True)
    async def reload(self,ctx,extension):
        self.bot.unload_extension(f"cogs.{extension}")
        self.bot.load_extension(f"cogs.{extension}")

        await ctx.send(str(extension)+' cog has been reloaded')

def setup(bot):
    """add the file to the bot's cog system"""
    bot.add_cog(CogMaintenance(bot))
