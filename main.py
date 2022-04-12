import discord
import os
import requests
import json
import random
from flask import request
from replit import db
import update

client = discord.Client()

sad_words = ["sad", "depressed", "sucks"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there!",
  "You are doing great!"
]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):

  msg = message.content

  if msg.startswith('who'):
   await message.channel.send('Probably someone awesome!')

  options = starter_encouragements
  if "encouragements" in db.keys():
    options = options + db["encouragements"]

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added! Thank you for making be smorter.")

  if msg.startswith("$delete"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$delete",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

client.run(os.getenv('TOKEN'))