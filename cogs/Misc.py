import discord
from discord.ext import commands
import random

class administracion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





    @commands.command(name='hug', alises=['abrazo'], brief="[abraza a un usuario]")
    async def hug(self, ctx, *, member: discord.Member):
        listGifs = [
            'https://cdn.weeb.sh/images/BkHA_O7v-.gif',
            'https://cdn.weeb.sh/images/SywetdQvZ.gif',
            'https://cdn.weeb.sh/images/ry6o__7D-.gif',
            'https://cdn.weeb.sh/images/BkuUhO1OW.gif',
            'https://cdn.weeb.sh/images/rkV6r56Oz.gif',
            'https://cdn.weeb.sh/images/ByPGRkFVz.gif'
        ]
        hug_embed = discord.Embed(
            title='  ',
            description=
            f"**{member}** recibe un caluroso abrazo de **{ctx.author}** >u<",
            color=discord.Color.blue())
        hug_embed.set_image(url=random.choice(listGifs))
        await ctx.send(embed=hug_embed)







    @commands.command(name='kiss', alises=['beso'], brief="[besa a un usuario]")
    async def kiss(self, ctx, *, member: discord.Member):
        listGifs = [
            'https://i.pinimg.com/originals/68/a3/7a/68a37a5a1b86f227b8e1169f33a6a6bb.gif',
            'https://media2.giphy.com/media/bGm9FuBCGg4SY/giphy.gif',
            'https://i.pinimg.com/originals/13/06/73/1306732d3351afe642c9a7f6d46f548e.gif',
            'https://i.gifer.com/XkMW.gif',
            'https://data.whicdn.com/images/331386660/original.gif',
            'https://i.imgur.com/4AaMn5E.gif',
            'https://i.imgur.com/oXRW1XU.gif'
        ]
        kiss_embed = discord.Embed(
            title='  ',
            description=f"**{member}** recibio un beso de **{ctx.author}** >u<",
            color=discord.Color.blue())
        kiss_embed.set_image(url=random.choice(listGifs))
        await ctx.send(embed=kiss_embed)






    @commands.command(name='blush',
                 alises=['sonrojar'],
                 brief="[¿te hicieron sonrojar?]")
    async def blush(self, ctx):
        listGifs = [
            'https://i.pinimg.com/originals/c8/51/28/c851280dfc35207936e407655e2226bb.gif',
            'https://i.pinimg.com/originals/2c/72/ce/2c72ced3ce7f01e53b68d532355e36de.gif',
            'https://i.pinimg.com/originals/10/42/5b/10425bd8382e2ec59a864b7055f98b38.gif',
            'https://acegif.com/wp-content/gif/blushing-35.gif',
            'https://i.gifer.com/755P.gif',
            'https://thumbs.gfycat.com/AcidicSecondhandBanteng-size_restricted.gif',
            'https://media.tenor.com/images/19f8b4bc44c9d95444b09d2a8cf23c55/tenor.gif'
        ]
        blush_embed = discord.Embed(
            title='  ',
            description=f"{ctx.author} se ha sonrojado** >u<",
            color=discord.Color.blue())
        blush_embed.set_image(url=random.choice(listGifs))
        await ctx.send(embed=blush_embed)







    @commands.command(name='mimir', alises=['dormir'], brief="[me fui a dormir uwu]")
    async def mimir(self, ctx):
        listGifs = [
            'https://acegif.com/wp-content/gif/anime-sleep-9.gif',
            'https://acegif.com/wp-content/gif/anime-sleep-11.gif',
            'https://acegif.com/wp-content/gif/anime-sleep-1.gif',
            'https://acegif.com/wp-content/gif/anime-sleep-31.gif',
            'https://acegif.com/wp-content/gif/anime-sleep-81.gif',
            'https://acegif.com/wp-content/gif/anime-sleep-47.gif',
            'https://acegif.com/wp-content/gif/anime-sleep-39.gif'
        ]
        mimir_embed = discord.Embed(
            title='  ',
            description=f"{ctx.author} se ha puesto a dormir porque esta cansado:C",
            color=discord.Color.blue())
        mimir_embed.set_image(url=random.choice(listGifs))
        await ctx.send(embed=mimir_embed)









    @commands.command(name='punch', alises=['golpear'], brief="[Golpea a un usuario]")
    async def punch(self, ctx, *, member: discord.Member):
        listGifs = [
            'https://acegif.com/wp-content/uploads/funny-anime-gif-31.gif',
            'https://i.pinimg.com/originals/65/ad/d9/65add9483a450f1d66d08e29b5b9ab4d.gif',
            'https://pa1.narvii.com/6295/319c20edf9cd7044fd613f6f98f7da50bb44787e_hq.gif',
            'https://thumbs.gfycat.com/AnxiousAdmirableEnglishsetter-size_restricted.gif',
            'https://media.tenor.com/images/a01f7057bb4c72c72e5ad13cb73d1b6f/tenor.gif',
            'https://pa1.narvii.com/6502/96218a6d9cfe6d1b4d2ab4984b1614d20e10fb42_hq.gif',
            'https://i.gifer.com/9KyA.gif'
        ]
        punch_embed = discord.Embed(
            title='  ',
            description=f"{ctx.author} se agarro a golpes a {member}",
            color=discord.Color.blue())
        punch_embed.set_image(url=random.choice(listGifs))
        await ctx.send(embed=punch_embed)






    @commands.command(name='scared',
                 alises=['asustar'],
                 brief="[¿te da miedo un usuario?]")
    async def scared(self, ctx, *, member: discord.Member):
        listGifs = [
            'https://i.pinimg.com/originals/ec/cf/01/eccf012575465ae194f31695b9043560.gif',
            'https://i.pinimg.com/originals/ac/ed/dd/aceddd9405a53c356a38d15b89bd6213.gif',
            'https://giphy.com/gifs/transparent-scared-kT7VY5eUanako',
            'http://pa1.narvii.com/6333/e2fb4348b2a8e20915d276a2edffefc109f7bd67_00.gif',
            'https://i.imgur.com/dMecNcX.gif',
            'https://i.gifer.com/Bazt.gif',
            'https://data.whicdn.com/images/198903294/original.gif'
        ]
        scared_embed = discord.Embed(
            title='  ',
            description=f"{ctx.author} le tiene miedo a {member}",
            color=discord.Color.blue())
        scared_embed.set_image(url=random.choice(listGifs))
        await ctx.send(embed=scared_embed)






    @commands.command(name='cry', alises=['cry'], brief="[¿quien te hizo llorar?]")
    async def cry(self, ctx, *, member: discord.Member):
        listGifs = [
            'https://i.gifer.com/V2Kw.gif',
            'https://i.pinimg.com/originals/cd/4f/4e/cd4f4eb7cbb5343e561810ea6adf63e5.gif',
            'https://i.pinimg.com/originals/ac/38/2e/ac382e22af3f7f14683feb011f432b0b.gif',
            'https://i.gifer.com/C1la.gif',
            'https://media.tenor.com/images/567cee456578c0689ec4a91b45f0d905/tenor.gif',
            'https://i.imgur.com/pls8egF.gif',
            'http://mrwgifs.com/wp-content/uploads/2013/05/Dramatic-Crying-In-Anime-Gif.gif'
        ]
        cry_embed = discord.Embed(
            title='  ',
            description=f"a {ctx.author} lo ha hecho llorar {member}",
            color=discord.Color.blue())
        cry_embed.set_image(url=random.choice(listGifs))
        await ctx.send(embed=cry_embed)






    @commands.command(name='drog', brief="[Puedes sacar esto?]")
    async def drog(self, ctx):
        a = [
            'https://drogadiccionmdna12.files.wordpress.com/2012/08/cocaine-coke-dollar-drugs-gif-favim-com-239370.gif',
            'https://media1.tenor.com/images/6647d619684099a1b185e6b52c167aa2/tenor.gif'
            ]
        drog_embed = discord.Embed(
            title='  ',
            description=f"{ctx.author} ha sacado lo prohibido",
            color=discord.Color.blue())
        drog_embed.set_image(url=random.choice(a))
        await ctx.send(embed=drog_embed)






    @commands.command(name='poli', brief="[¿alto ahi perro?]")
    async def poli(self, ctx, *, member: discord.Member):
        e = ['https://media1.tenor.com/images/9d02871b26ab82b59066d2655ab09153/tenor.gif',
             'https://c.tenor.com/goq48dvYSFYAAAAC/fbi-calling.gif',
             'https://thumbs.gfycat.com/PreciousHeartyDrafthorse-size_restricted.gif',
             'https://monophy.com/media/cLwQ6W9OywmXeCdaok/monophy.gif'
             ]
        poli_embed = discord.Embed(
            title='  ',
            description=f"{member} te ha reportado con la policia {ctx.author} corre",
            color=discord.Color.blue())
        poli_embed.set_image(url=random.choice(e))
        await ctx.send(embed=poli_embed)






    @commands.command(name='pat',
                 alises=['pat'],
                 brief="[acaria a alguien]")
    async def pat(self, ctx):
        args = ctx.message.content.split(" ")[1:]
        embed = discord.Embed(title='  ', description=f"{ctx.author} te esta acariciando", color=discord.Color.blue())
        embed.colour = discord.Color.from_rgb(0, 255, 255)

        pat = ['https://i.pinimg.com/originals/a3/3a/46/a33a46a9e0a0e894f12ba4a6f9e4c7b0.gif',
               'https://i.pinimg.com/originals/7b/4e/27/7b4e27392baf0fc817223e6bcffc9818.gif',
               'https://pa1.narvii.com/6255/61411fa7cb845c5cd20308e73558b7419438c81c_hq.gif',
               'https://media.tenor.com/images/f9cc67c97b6b6399ba921bd71bb8a618/tenor.gif']
        if len(args) == 0:
            embed.title = ctx.author.name
            embed.set_image(url=random.choice(pat))
            await ctx.send(embed=embed)


        elif len(ctx.message.mentions) > 0:
            for member in ctx.message.mentions:
                embed.title = member.name
                embed.set_image(url=random.choice(pat))
                await ctx.send(embed=embed)

        elif args[0] in ("server", "guild"):
            embed.title = ctx.guild.name
            embed.set_image(url=random.choice(pat))
            await ctx.send(embed=embed)

        else:
            embed.title = "pat"
            embed.description = f"acaricia a alguien uwu."
            embed.add_field(
                name="Uso:",
                value=
                f"{PREFIX}avatar\n{PREFIX}avatar @user1, @user2, ...\n{PREFIX}avatar server",
                inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(administracion(bot))
