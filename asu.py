import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
   print("Bot logged on: " + bot.user.name + "//" + bot.user.id)

@bot.command()
async def astral(arg="Hey"):
   talkdict = {0: "NUMBERS!",
                 1: "I entrust the Numbers to you.",
                 2: "Yoomah...Yoomah",
                 3: "*Sigh*",
                 4: "*Groans*",
                 5: "...ura.",
                 6: "Back to the deck with you, Ninety-Six",
                 7: "Observation #2: You are weird.",
                 8: "Observation #3: Humans must eat and release energy in endless combination. However, they will die the moment anyone sees them doing this.",
                 9: "Observation #16: Kattobingu also means liking tomatoes.",
                 10: "Observation #21: Yuma would make a good cartoon character in real life.",
                 11: "Observation #88: Video games nurture the mind, but they also can be quite addictive and cause somebody to lose grip on reality. Sub-Observation #88.a: I would make a good Let's Play channel.",
                 12: "Kuri Kuri!",
                 13: "Chuuma",
                 14: "*Floats away*",
                 15: "I love your smile, I'll never forget it",
                 16: "Yes",
                 17: "No",
                 18: "*Pops out of the Key*",
                 19: "*Goes back to the key*",
                 20: "Please, you are embarrassing me, and I am invisible",
                 21: "Certainly",
                 22: "...",
                 23: ":chaos:",
               24: ":alsodead:",
               25: "EVIIIIIIIIIIIIIIILLLL",
               26: "Perhaps ask me when I collect more data.",
               27: "I do not have any data about that in my memory.",
               28: "Yes, thank you",
               29: "No, thank you",
               30: "I cannot say",
               31: "Good!",
               32: "*Hums 'Masterpiece'",
               33: "*Hides behind a tree*",
               34: "I truly appreciate that",
               35: "Thank you!",
               36: "You're the best!",
               37: "You're my Other Half",
               38: "*Thumbs up at you*",
               39: ":thenperish:",
               40: ":sparkling_heart:"
               }
   
   answerdict = {0: "Hey Astral"
                 }
   randomtalk = random.randrange(0, len(talkdict))
   randomanswer = random.randrange(0, len(answerdict))
   if arg and arg[-1] == "?":
       await bot.say(answerdict[randomanswer])
   else:
       await bot.say(talkdict[randomtalk])

bot.run("NTQ5OTk2NTc2MDUxOTUzNjc1.D1c-4Q.KesDx-TKgFc-psq_RxXbxxf2ha8")
