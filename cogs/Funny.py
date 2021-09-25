import discord
from discord.ext import commands
import random

class administracion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info', alises=['info'], brief="[informacion del servidor]")
    async def info(self, ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}",
                              description="La casa de los giles",
                              color=discord.Color.blue())
        embed.add_field(name="servidor creado", value=f"{ctx.guild.created_at}")
        embed.add_field(name="Amo del servidor", value=f"{ctx.guild.owner}")
        embed.add_field(name="Region del servidor", value=f"{ctx.guild.region}")
        embed.add_field(name="ID del servidor", value=f"{ctx.guild.id}")
    #experimental embed.set_thumbnail(url=f"{ctx.guild.icon}")
        await ctx.send(embed=embed)






    @commands.command(name='say', alises=['say'], brief="[comando solo para admins]")
    async def say(self, ctx, *, text):
        message = ctx.message
        await message.delete()
        await ctx.send(f"{text}")






    @commands.command(name='avatar',
                 alises=['avatar'],
                 brief="[ve el avatar tuyo o de los demas]")
    async def avatar(self, ctx):
        args = ctx.message.content.split(" ")[1:]

        embed = discord.Embed()
        embed.colour = discord.Color.from_rgb(0, 255, 255)

        if len(args) == 0:
            embed.title = ctx.author.name
            embed.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        elif len(ctx.message.mentions) > 0:
            for member in ctx.message.mentions:
                embed.title = member.name
                embed.set_image(url=member.avatar_url)
                await ctx.send(embed=embed)

        elif args[0] in ("server", "guild"):
            embed.title = ctx.guild.name
            embed.set_image(url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        else:
            embed.title = "avatar"
            embed.description = f"Muestra tu avatar, de los usuarios mencionados o del servidor."
            embed.add_field(
                name="Uso:",
                value=
                f"{PREFIX}avatar\n{PREFIX}avatar @user1, @user2, ...\n{PREFIX}avatar server",
                inline=False)
            await ctx.send(embed=embed)






    @commands.command(aliases=['8ball'], brief="[¿quieres saber tu futuro?]")
    async def _8ball(self, ctx, *, question):
        response = [
            'En mi opinión, sí', 'Es cierto', 'Es decididamente así',
            'Probablemente', 'Buen pronóstico', 'Todo apunta a que sí', 'Sin duda',
            'Sí', 'Sí - definitivamente', 'Debes confiar en ello',
            'Respuesta vaga, vuelve a intentarlo', 'Pregunta en otro momento',
            'Será mejor que no te lo diga ahora', 'No puedo predecirlo ahora',
            'Concéntrate y vuelve a preguntar', 'Puede ser', 'No cuentes con ello',
            'Mi respuesta es no', 'Mis fuentes me dicen que no',
            'Las perspectivas no son buenas', 'Muy dudoso'
        ]
        _8ball_embed = discord.Embed(title='  ',
                                     description=f"  ",
                                     color=discord.Color.blue())
        _8ball_embed.add_field(
            name="Comando 8ball | :8ball:",
            value=
            f"**Pregunta:** {question}\n**Respuesta:** {random.choice(response)}"
        )  # Aqui es como quieres que sea su respuesta
        await ctx.send(embed=_8ball_embed)






    @commands.command(name="l",
                 help="Muestra un porcentaje de lo L que eres",
                 brief="[Que tan L eres?]")
    async def calculeL(self, ctx):
        try:
            random_porcentaje = random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29,
                 30,
                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                 57,
                 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
                 85,
                 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 200])
            await ctx.send(f'{ctx.author} es {random_porcentaje}% L ')
        except NameError as error:
            await ctx.send(f"Algun error ocurrio ...{error}")
        finally:
            print(f"{ctx.author}")







    @commands.command(name="user",
                 help="Mira la informacion de un miembro",
                 brief="[Mira la informacion de un miembro]")
    async def some_function_random_ctx(self, ctx, member: discord.Member):
        try:
            user_info_embed = discord.Embed(colour=0xff00ff).set_author(
                name=f"{member}", icon_url=member.avatar_url)
            user_info_embed.add_field(name=f"Entro a el servidor {ctx.guild}",
                                      value=member.joined_at)
            user_info_embed.add_field(name="Rol mas alto", value=member.top_role)
            user_info_embed.add_field(name="Creo su cuenta de discord",
                                      value=member.created_at)
            user_info_embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=user_info_embed)
        except:
            await ctx.send("Una excepcion ocurrio...")
        finally:
            await ctx.send(
                "informacion obtenida con exito, si no es asi, puede que haya ocurrido un error."
            )

    @commands.command(name="sabias", alises="sabias", brief="[quieres un dato interesante]")
    async def sabias(self, ctx):
        dato = [
            'Los flamencos doblan las piernas en el tobillo no la rodilla',
            'La rueda de la fortuna fue inventada para alejar a los americanos del pecado',
            'Los perezosos pueden aguantar más tiempo el aliento que los delfines',
            'Los Froot Loops son todos del mismo sabor', 'Las manzanas en el supermercado pueden tener hasta un año',
            'Los pulpos tienen 3 corazones', 'En las Filipinas, McDonald´s vende spaghetti',
            'Hitler fue nominado a un Nobel de la paz', 'Las langostas saborean con los pies',
            'El Empire State tiene su propio código postal',
            'Las sombras son más oscuras en la luna', 'La Estatua de la Libertad solía ser un faro',
            'Las ManhattAnts son una especie de hormigas únicas de Nueva York',
            'Los tanques británicos están equipados para hacer té',
            'Los elefantes son los únicos animales que no pueden saltar.',
            'La palabra [cementerio] significa dormitorio en griego antiguo.',
            ' Los ojos hacen más ejercicio que las piernas',
            'Nuestro aroma es tan único como nuestras huellas digitales', 'Puedes ver un óvulo a simple vista',
            'El corazón podría mover un coche', 'Nada es tan inútil como parece',
            'Eres el responsable de todo el polvo que se junta en tu casa',
            ' El calor corporal es más de lo que imaginas',
            'La lengua nunca descansa', 'Los hombres y mujeres escuchan de manera diferente',
            'Los bebés pueden curar a sus madres en el vientre',
            ' Para hacer un kilogramo de miel, una abeja debe recorrer 4 millones de flores, pero la miel es un alimento que no se pudre',
            'Las primeras almohadas eran de piedra', 'Los primeros despertadores… ¡Eran personas!',
            'El cuerpo humano contiene en promedio unos 37 litros de agua',
            'Una canilla que gotea desperdicia más de 75 litros de agua por día',
            'Se necesitan 200 litros de agua para producir un solo litro de gaseosa cola',
            'Una persona puede sobrevivir un mes sin alimentarse, pero puede estar como máximo siete días sin beber agua.',
            'sabias que naci por idea de mi novia'
        ]
        dato_embed = discord.Embed(title='  ',
                                   description=f"  ",
                                   color=discord.Color.blue())
        dato_embed.add_field(name="sabias que", value={random.choice(dato)})
        await ctx.send(embed=dato_embed)







    @commands.command(name="nivel",
                 help="Muestra un nivel de pvp",
                 brief="[Que tan pro eres?]")
    async def nivel(self, ctx):
        try:
            random_porcentaje = random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29,
                 30,
                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                 57,
                 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
                 85,
                 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 200])
            await ctx.send(f'{ctx.author} eres {random_porcentaje}% bueno en pvp ')
        except NameError as error:
            await ctx.send(f"Algun error ocurrio ...{error}")
        finally:
            print(f"{ctx.author}")







def setup(bot):
    bot.add_cog(administracion(bot))
