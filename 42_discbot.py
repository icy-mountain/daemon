#!/usr/bin/python3.6
import sys
import os
token = os.environ.get("DISC_TOKEN")
file = open("/home/ubuntu/daemon/my.log", "a")
file.write(str(sys.path) + "\n")
import ast
import urllib.request
import discord

def take_api():
    url = 'https://covidapi.info/api/v1/country/JPN'
    req = urllib.request.Request(url)
    ans = ""
    with urllib.request.urlopen(req) as res:
      body = res.read()
      dic = ast.literal_eval(body.decode("utf-8"))
      keys = list(dic["result"].keys())
      target = keys[-1]
      ans = "[" + target + "]  " + str(dic["result"][target])[1:-1]
    return ans

def main(token):
  client = discord.Client()

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
    if message.content == "/hoge" or message.content == "/bot":
      await message.channel.send('hello! my name is hoge\nmy content is (/covid JPN)')
    if message.content == "/covid JPN":
      await message.channel.send(take_api())
  client.run(token)

if __name__ == "__main__":
  main(token)
