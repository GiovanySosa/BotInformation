import discord
from discord.ext import commands
import asyncio

class administracion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def kick(self, ctx, *, member: discord.Member, reason=None):
        if ctx.message.author.guild_permissions.administrator:
            await member.kick(reason=reason)
            await ctx.send(f'usuario {member} ha sido expulsado')




    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)
        embed = discord.Embed(title="muteado", description=f"{member.mention} haz sido muteado",
                              colour=discord.Colour.light_gray())
        embed.add_field(name="razon:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" haz sido muteado por: {guild.name} razon: {reason}")




    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        embed = discord.Embed(title="desmuteado", description=f" desmuteado-{member.mention}",
                              colour=discord.Colour.light_gray())
        await ctx.send(embed=embed)




    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def tempmute(self, ctx, member: discord.Member, time):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        tempmute = int(time[0]) * time_convert[time[-1]]
        await ctx.message.delete()
        await member.add_roles(muted_role)
        embed = discord.Embed(description=f"{member.display_name} haz sido muteado temporalmente por {time}",
                              color=discord.Color.green())
        await ctx.send(embed=embed, delete_after=60)
        await asyncio.sleep(tempmute)
        await member.remove_roles(muted_role)



    @commands.command()
    async def ban(self, ctx, *, member: discord.Member, reason=None):
        if ctx.message.author.guild_permissions.administrator:
            await member.ban(reason=reason)

            ban = discord.Embed(title="BANEADO", description=f" {member} ha sido baneado", colour=discord.Colour.blue())

            await ctx.send(embed=ban)

    @commands.command()
    async def anuncio(self, ctx, *, text):
        if ctx.message.author.guild_permissions.administrator:
            message = ctx.message
            embed = discord.Embed(title='  ', description=f"{text}", colour=discord.Colour.blue())
        await message.delete()
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(administracion(bot))
