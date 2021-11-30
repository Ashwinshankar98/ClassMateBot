import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class BanUsers(commands.Cog):
    """DM functionality"""
    def __init__(self, bot):
        self.bot = bot
    """
    Function: Ban
    Description: Command for banning spammers
    Inputs:
    - ctx: used to access the values passed through the current context
    - member: name of the memeber
    - reason: reason for ban
    Outputs:
    - response from bot
    """
    @commands.command(name='ban',help="bans a member")
    @has_permissions(administrator=True)
    async def ban(self,ctx,member:discord.Member,*,reason=None):

        await member.ban(reason=reason)
        await ctx.send(str(member.mention)+' has been banned for '+reason)

    """
    Function: unBan
    Description: Command for unbanning 
    Inputs:
    - ctx: used to access the values passed through the current context
    - member: name of the memeber
    Outputs:
    - response from bot
    """

    @commands.command(name='unban',help="unbans a member")
    @has_permissions(administrator=True)
    async def unban(self,ctx,*,member):

        banned_users= await ctx.guild.bans()

        member_name,member_discriminator=member.split('#')

        for entry in banned_users:

            user=entry.user
            if (user.name,user.discriminator)==(member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send('unbanned '+member.mention)
                return

def setup(bot):
    """add the file to the bot's cog system"""
    bot.add_cog(BanUsers(bot))
