import discord
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot is online as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Wassup! I am HusyBot")

    if message.content.startswith("!help"):
        await message.channel.send("Commands: !hello, !help, !weather [city], !wiki [topic], !joke, !Fact")

    if message.content.startswith("!weather"):
        city = message.content[9:].strip()
        if not city:
            await message.channel.send("Usage: !weather [city]")
        else:
            url = f"https://wttr.in/{city}?format=3"
            response = requests.get(url)
            await message.channel.send(response.text)

    if message.content.startswith("!wiki"):
        topic = message.content[6:].strip()
        if not topic:
            await message.channel.send("Usage: !wiki [topic]")
        else:
            url = f"https://en.wikipedia.org/wiki/{topic}"
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find("div", id="mw-content-text").find_all("p")
            summary = ""
            for p in paragraphs:
                if len(p.text.strip()) > 100:
                    summary = p.text.strip()
                    break
            await message.channel.send(summary[:500] + "...")

    if message.content.startswith("!joke"):
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        joke = response.json()
        await message.channel.send(f"{joke['setup']}\n{joke['punchline']}")
    if message.content.startswith("!fact"):
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        response = requests.get(url)
        fact = response.json()
        await message.channel.send(f"Fun fact: {fact['text']}")
client.run("Place_holder_for_token")