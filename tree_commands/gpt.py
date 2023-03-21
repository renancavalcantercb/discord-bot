from dotenv import load_dotenv
from os import getenv
from discord import Embed, NotFound
import openai

load_dotenv()


class Gpt:
    def __init__(self, bot):
        self.bot = bot
        self.question = None
        self.api_key = getenv('OPENAI_API_KEY')

    async def gpt(self, ctx, question):
        await ctx.response.defer()
        try:
            openai.api_key = self.api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a chatbot"},
                    {"role": "user", "content": question},
                ],
                temperature=0.5,
                max_tokens=1024,
            )
            result = ''
            for choice in response.choices:
                result += choice.message.content
            answer_embed = Embed(title=question, description=result, color=0x00ff00)
            await ctx.followup.send(embed=answer_embed)
        except NotFound:
            await ctx.followup.send('I can\'t find that message.')
