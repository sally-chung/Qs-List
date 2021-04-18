# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 12:56:28 2021

@author: sally
"""

import nest_asyncio
nest_asyncio.apply()

import discord
from discord.ext import commands

from craigslist import CraigslistHousing
from datetime import datetime, date, timedelta

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def ping(ctx):
    await ctx.send('Pong!')
    
@client.command()
async def rooms(ctx):
    
    # id
    # repost_of
    # name = ctx
    # url = ctx
    # datetime
    # last_updated = ctx
    # price
    # where
    # has_image
    # geotag
    # deleted


    # "apa" is craigslist's url key for "apartments / housing for rent"
    sgv_rooms = CraigslistHousing(site="losangeles", area="sgv", category="roo")
    # post = next(sgv_rooms.get_results())
    current_date_time = datetime.now()
    
    for post in sgv_rooms.get_results():
        # get post_date
        post_date_time = datetime.strptime(post.get("datetime"), '%Y-%m-%d %H:%M')
        
        # compare post_date with current_date
        if current_date_time-timedelta(hours=2) <= post_date_time <= current_date_time:
            print(post)

    
client.run('ODMzMDM0MDUyOTA1NzMwMDg5.YHsdaw.BNWpL28bP5eISMUX7ugDF4DOVKg')