import discord
from discord.ext import commands


class CreateService(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Create a service ticket')
    async def create_service(self, ctx):
        embed = discord.Embed(title="Clue Service", description="Fill in the fields below to create a service.",
                              color=0x00ff00)
        embed.set_footer(text="Created by: " + ctx.author.name)

        embed_msg = await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        question_embed_msg = await ctx.send("How many clues will you do?")
        response_0 = await self.bot.wait_for('message', check=check)
        embed.add_field(name="Total clues quantity", value=response_0.content, inline=False)
        await question_embed_msg.delete()
        await response_0.delete()
        await embed_msg.edit(embed=embed)

        question_embed_msg = await ctx.send("Easy Clues:")
        response_1 = await self.bot.wait_for('message', check=check)
        embed.add_field(name="Easy clues quantity", value=response_1.content, inline=False)
        await question_embed_msg.delete()
        await response_1.delete()
        await embed_msg.edit(embed=embed)

        question_embed_msg = await ctx.send("Medium Clues:")
        response_2 = await self.bot.wait_for('message', check=check)
        embed.add_field(name="Medium clues quantity", value=response_2.content, inline=False)
        await question_embed_msg.delete()
        await response_2.delete()
        await embed_msg.edit(embed=embed)

        question_embed_msg = await ctx.send("Hard Clues:")
        response_3 = await self.bot.wait_for('message', check=check)
        embed.add_field(name="Hard clues quantity", value=response_3.content, inline=False)
        await question_embed_msg.delete()
        await response_3.delete()
        await embed_msg.edit(embed=embed)

        question_embed_msg = await ctx.send("Elite Clues:")
        response_4 = await self.bot.wait_for('message', check=check)
        embed.add_field(name="Elite clues quantity", value=response_4.content, inline=False)
        await question_embed_msg.delete()
        await response_4.delete()
        await embed_msg.edit(embed=embed)

        question_embed_msg = await ctx.send("Masters Clues:")
        response_5 = await self.bot.wait_for('message', check=check)
        embed.add_field(name="Masters clues quantity", value=response_5.content, inline=False)
        await question_embed_msg.delete()
        await response_5.delete()
        await embed_msg.edit(embed=embed)

        question_embed_msg = await ctx.send("Requester:")
        response_6 = await self.bot.wait_for('message', check=check)
        embed.add_field(name="Requester", value=response_6.content, inline=False)
        await question_embed_msg.delete()
        await response_6.delete()
        await embed_msg.edit(embed=embed)

        question_embed_msg = await ctx.send("Payment:")
        response_7 = await self.bot.wait_for('message', check=check)
        embed.add_field(name="Requester", value=response_7.content, inline=False)
        await question_embed_msg.delete()
        await response_7.delete()
        await embed_msg.edit(embed=embed)

        question_embed_msg = await ctx.send("Can you confirm the creation of the service?")
        await question_embed_msg.add_reaction('✅')
        await question_embed_msg.add_reaction('❌')
        response_8 = await self.bot.wait_for('reaction_add')
        if response_8[0].emoji == '✅':
            await ctx.send("Service created!")
        else:
            await ctx.send("Service canceled!")
        await question_embed_msg.delete()


async def setup(bot):
    await bot.add_cog(CreateService(bot))
