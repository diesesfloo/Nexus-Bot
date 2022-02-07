import asyncio
from turtle import title
import discord
from discord.ext import commands
from discord import Embed, Game, Intents

class clearCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount = None):
        author = ctx.message.author
        if amount is None:
            noneEmbed = Embed(title="♾️ Clear", description="You need to give the amount to delete.")
            await ctx.reply(embed=noneEmbed)
            return

        if not str(amount).isdigit():
            noNumberEmbed = Embed(title="♾️ Clear", description="You need to enter a number.")
            await ctx.reply(embed=noNumberEmbed)
            return

        amount = int(amount)

        if author.guild_permissions.manage_messages:
            amount = amount + 1
            if(amount > 101):
                bigEmbed = Embed(title= "♾️ Clear", description=f"<@{author.id}>, I'm sorry, but I can't delete more than 100 messages.")
                await ctx.reply(embed=bigEmbed)
                return
            try:
                await ctx.channel.purge(limit=amount)

                finishEmbed = Embed(title = "♾️ Clear", description=f"Sucessfully deleted **{amount - 1}** messages.")
                await ctx.send(embed = finishEmbed, delete_after=5)
            except:
                errorEmbed = Embed(title="♾️ Clear", desciption=f"Hey <@{author.id}>, someting went wrong 👾. Please try again.")
                ctx.reply(embed=errorEmbed)
        else:
            noPermEmbed = Embed(title = "♾️ Clear", description=f"<@{author.id}>, you are missing the permission `MANAGE_MESSAGES`.")
            await ctx.reply(embed=noPermEmbed)