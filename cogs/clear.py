from discord.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        return await ctx.send(f'Purged {amount} messages.', delete_after=5)


async def setup(bot):
    await bot.add_cog(Clear(bot))
