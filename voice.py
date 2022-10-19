import discord
from discord.ext import commands
from discord.commands import Option


class Voice(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  #It works till echo
  @commands.command()
  async def echo(self, ctx: commands.Context):
    await ctx.send("Carpal Tunnel acting up? Try speaking what you want to type")

  
  @commands.command()
  async def join(self, ctx: commands.Context, *, channel: discord.VoiceChannel):
    try:
      if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
      await channel.connect()
    except:
      await ctx.send(f"Try /join 'voice_channel_name'")

  @commands.command()
  async def start(self, ctx: commands.Option(str, choices=['mp3','wav','pcm'])):
    myvoice = ctx.author.voice
    if not myvoice:
      return await ctx.respond("You are not in a voice channel right now")
    vc = await myvoice.channel.connect()
    bot.connections.update({ctx.guild.id:vc})
    vc.start_recording(
      discord.Sink(encoding=encoding),
      finished_callback,
      ctx.channel,
    )
    await ctx.respond("The recording has started")
    

def setup(bot):
  bot.add_cog(Voice(bot))
