import discord
from discord.ext import commands
import os
from model import birds

class_name = open("labels.txt", "r").readlines()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def SECRETCONTEXTBOTEZEZEZ(ctx):
    await ctx.send(f'after getting energy from coal, theres a smoke that are bad for ozone layer, it getting more thinner, and bcs of that, sun is more powerful, but its not good, bcs of that flowers are blooming in antarctica. thats not good, now, every glacier will be smaller, because of stronger sun. not even one company that getting energy out of a coal will see this message, so, we need now only to watch, how our planed will cosplay page from bible. if you wanna know how to stop this - theres no way, only to slow it, while im printing this message, ozone layer becomes more weaker and weaker, so if you, who sees this message, can do something, just use solar battery, this will be more usefull in sunny citys, but not in russia, coal is more effective, you can get more money, but if you dont live just some longer, can you get more money? - no, so stop it, everyone wants live just some longer, so help, please.')

@bot.command()
async def what_bird(ctx):
       try:
           if ctx.message.attachments:
               attachment = ctx.message.attachments[0]
               image_path = os.path.join('saved_images', attachment.filename)
               os.makedirs('saved_images', exist_ok=True)
               await attachment.save(image_path)
               await ctx.send(f'Изображение сохранено: {image_path}')
               bird = birds(image_path)
               await ctx.send(f'На картинке изображено {bird}')
               
               if class_name == 1:
                  await ctx.send(f'кормите голубьок')
               elif class_name == 0:
                    await ctx.send(f'кормите синеву')


           else:
               await ctx.send('Пожалуйста, прикрепите изображение к сообщению.')
       except Exception as e:
           await ctx.send(f'Произошла ошибка: {e}')

@bot.command()
async def save_image(ctx):
       try:
           if ctx.message.attachments:
               attachment = ctx.message.attachments[0]
               image_path = os.path.join('saved_images', attachment.filename)
               os.makedirs('saved_images', exist_ok=True)
               await attachment.save(image_path)
               await ctx.send(f'Изображение сохранено: {image_path}')
           else:
               await ctx.send('Пожалуйста, прикрепите изображение к сообщению.')
       except Exception as e:
           await ctx.send(f'Произошла ошибка: {e}')

bot.run("")
