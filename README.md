# Statstok
<center> A simple python script that scrapes tiktok account's likes and followers using bs4 and requests </center>

## Functions

```get_followers(username)``` will return the username's follower count


```get_likes(username)``` will return the username's total like count

## Dependancies

Statstok depends on `bs4` and `requests`

## Installation

### Installation via PiP

For windows users, you can do

`pip install statstok`

For linux and mac users, you can do 

`pip3 install statstok`

To manually install and add this to your project, simply clone foo `statstok.py` bar into the directory of your project 

Make sure to add `from statstok import get_followers` or `from statstok import get_likes` before you start using statstok

### Examples

Discord Bot

``` python
import discord
from discord.ext import commands
from statstok import statstok

bot = commands.Bot(command_prefix="!")

@bot.command()
async def followers(ctx, username):
    await ctx.send(f"That user has {statstok.get_followers(username)} followers")

bot.run("TOKEN")
```


## Help and Support

If you need help with Statstok, you can either <a href="discord.gg/MwmnXNsjsj"> join the discord </a> or submit an issue request
