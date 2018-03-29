import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):



     
 if message.content == "Anyone here?":
        await client.send_message (message.channel, "I'm here.")

 if message.content == "anyone here?":
        await client.send_message (message.channel, "Probably.")  

 if message.content == "Argus":
        await client.send_message (message.channel, "I can do a pretty good impersonation of that guy. Want to see?.")

 if message.content == "Argus!":
        await client.send_message (message.channel, "SHHH don't yell that! Do you have any idea how many Organon laws we're already breaking.")

 if message.content == "Argus!!":
        await client.send_message (message.channel, "Shhh! Be quiet! Can you imagine if he found this place? If he saw the art you've all drawn!")



 
 if message.content == "Baby":
        await client.send_message (message.channel, "Goaly? Were'd she go now?")

 if message.content == "baby":
        await client.send_message (message.channel, "You mean Goaly? Don't worry, I know where she is... more or less.")

 if message.content == "Bad rufus!":
        await client.send_message (message.channel, "I take the little victories.")

 if message.content == "Bad rufus!":
        await client.send_message (message.channel, "I take the little victories.")

 if message.content == "Be nice Rufus":
        await client.send_message (message.channel, "Fine.")

 if message.content == "Be nice Rufus.":
        await client.send_message (message.channel, "Fine.")

 if message.content == "Bozo":
        await client.send_message (message.channel, "Oh, the pirate?")

 if message.content == "Bozo?":
        await client.send_message (message.channel, "Oh, the pirate?")

 if message.content == "Bye Rufus":
        await client.send_message (message.channel, "If I'm not back in ten minutes, give me ten more.")

 if message.content == "bye Rufus":
        await client.send_message (message.channel, "If I'm not back in ten minutes, give me ten more.")







        

 if message.content == "Catch Rufus":
        await client.send_message (message.channel, "Ha! You'll have to catch me first, and I'm mutch too fast for you. See? *Veoooooow! Va-toooooo! Veroooooom!* ")

 if message.content == "catch Rufus":
        await client.send_message (message.channel, "Ha! You'll have to catch me first, and I'm mutch too fast for you. See? *Veoooooow! Va-toooooo! Veroooooom!* ")

 if message.content == "Chaos":
         await client.send_message (message.channel, "When chaos floods order, genius mounts a surfboard.")

 if message.content == "chaos":
         await client.send_message (message.channel, "When chaos floods order, genius mounts a surfboard.")

 if message.content == "Chloroform":
        await client.send_message (message.channel, "According to the warning label this should produce an interesting chemical reaction.")

 if message.content == "chloroform":
        await client.send_message (message.channel, "According to the warning label this should produce an interesting chemical reaction.")
     
 if message.content == "Cleaning":
         await client.send_message (message.channel, "I don't usually associate with cleaning implemants. On the other hand I like little technical gadgets that make more noise than necessary.")

 if message.content == "Clean":
        await client.send_message (message.channel, "Hehe, yeah right, like I would ever clean something.")

 if message.content == "clean":
        await client.send_message (message.channel, "Hehe, yeah right, like I would ever clean something.")

 if message.content == "Clean up":
        await client.send_message (message.channel, "Hehe, yeah right, like I would ever clean something.")

 if message.content == "clean up":
        await client.send_message (message.channel, "Hehe, yeah right, like I would ever clean something.")

 if message.content == "Cletus drawing":
        await client.send_message (message.channel, "Woah! Cool! Next time I recomend less Cletus more Rufus.")

 if message.content == "Cletus doodle":
        await client.send_message (message.channel, "I'm sure it would make Cletus very happy. That egomaniac would love this.")

 if message.content == "cleaning":
         await client.send_message (message.channel, "I don't usually associate with cleaning implemants. On the other hand I like little technical gadgets that make more noise than necessary.")

 if message.content == "Cletus":
        await client.send_message (message.channel, "His hair is more greasy than a platypus burger.")

 if message.content == "Cletus!":
        await client.send_message (message.channel, "Shhhh! Don't yell he might hear us.")

 if message.content == "Cletus is the best":
        await client.send_message (message.channel, "Well, you know, everyone entitled to an opinion... even a wrong one.")

 if message.content == "Cletus is the best.":
        await client.send_message (message.channel, "That's the best joke I've heard all day!")

 if message.content == "Cletus is the best!":
        await client.send_message (message.channel, "Was your brain implant damaged? I know a guy who can fix that for you.")

 if message.content == "Cookie":
        await client.send_message (message.channel, "Do you have any idea how hard those are to get on Deponia?")

 if message.content == "cookie":
        await client.send_message (message.channel, "Here's one I skillfully acquired earlier :cookie:")

 if message.content == ":cookie:":
        await client.send_message (message.channel, "Don't mind if I do. *Yoink!*")

 if message.content == "Crowbar":
        await client.send_message (message.channel, "Aaah, my second favourite tool.")

 if message.content == "crowbar":
        await client.send_message (message.channel, "Aaah, my second favourite tool.")







        

 if message.content == "Do you have some?":
        await client.send_message (message.channel, "Probably, let me check.")

 if message.content == "do you have some?":
        await client.send_message (message.channel, "Not yet, but I have an idea where I can get some.")

 if message.content == "Do you think?":
        await client.send_message (message.channel, "Maybe they read my blog.")

 if message.content == "do you think?":
        await client.send_message (message.channel, "Maybe they read my blog.")

 if message.content == "Doctor Gizmo":
        await client.send_message (message.channel, "I'm banned from his clinic because I sometimes snack on expired drugs from his trash can.")

 if message.content == "doctor Gizmo":
        await client.send_message (message.channel, "I'm banned from his clinic because I sometimes snack on expired drugs from his trash can.")

 if message.content == "Don't talk about my wife like that Rufus":
        await client.send_message (message.channel, "I could fight you, but I won't because I don't want to get my hands dirty.")

 if message.content == "Don't talk about my wife like that":
        await client.send_message (message.channel, "I could fight you, but I won't because I don't want to get my hands dirty.")

 if message.content == "Don't talk about my wife like that Rufus":
        await client.send_message (message.channel, "I could take you on.")

 if message.content == "Doodle":
        await client.send_message (message.channel, "That's not a doodle! It's too good!")

 if message.content == "doodle":
        await client.send_message (message.channel, "That's not a doodle! It's too good!")

 if message.content == "Duck!":
        await client.send_message (message.channel, "Where? -OOF!")

 if message.content == "duck!":
        await client.send_message (message.channel, "Where? -OOF!")

 if message.content == "DUCK!":
        await client.send_message (message.channel, "Where? -OOF!")

 if message.content == "dynamite":
        await client.send_message (message.channel, "That would make a great stage name. I can hear it now, 'Dynamite Rufus!'. The act would be a riot.")

 if message.content == "Dynamite":
        await client.send_message (message.channel, "Ahh, my eighth favourite explosive.")

 if message.content == "Dynamite?":
        await client.send_message (message.channel, "I like the way you think")

 if message.content == "dynamite?":
        await client.send_message (message.channel, "Don't mind if I do. Yoink!")

 if message.content == "dynamite!":
        await client.send_message (message.channel, "KABLAMO!")

 if message.content == "Dynamite!":
        await client.send_message (message.channel, "KABOOM!")

 if message.content == "DYNAMITE!":
        await client.send_message (message.channel, "Hit the deck!!!")







        

 if message.content == "Electrifying":
        await client.send_message (message.channel, "All those hours under Dr.Gizmo's defibrillator are finally paying off.")

 if message.content == "electrifying":
        await client.send_message (message.channel, "All those hours under Dr.Gizmo's defibrillator are finally paying off.")

 if message.content == "Evolution":
        await client.send_message (message.channel, "In the beginning, there was fire.In the end, everybody will be screaming at me.")

 if message.content == "evolution":
        await client.send_message (message.channel, "In the beginning, there was fire.In the end, everybody will be screaming at me.")









 if message.content == "Fanart":
        await client.send_message (message.channel, "Can I show my fanart? Wait, I changed my mind. Only Goal is allowed to see it.")

 if message.content == "fanart":
        await client.send_message (message.channel, "Can I show my fanart? Wait, I changed my mind. Only Goal is allowed to see it.")  

 if message.content == "Fire":
        await client.send_message (message.channel, "My family's motto was, 'it's enough to know how to light a fire. There will be others around who know how to operate an extinguisher.'")

 if message.content == "fire":
        await client.send_message (message.channel, "The flame that burns twice as bright and... uhh.. twice as long. Yeah that's me.")

 if message.content == "Flag":
        await client.send_message (message.channel, "The Flag-O-Mat only takes human ashes.")

 if message.content == "flag":
        await client.send_message (message.channel, "The Flag-O-Mat only takes human ashes.")







        

 if message.content == "Gardiner":
        await client.send_message (message.channel, "Why does my back suddenly feel like someone scratched the word 'REVENGE' into it with a rusty rake?")

 if message.content == "gardiner":
        await client.send_message (message.channel, "Why does my back suddenly feel like someone scratched the word 'REVENGE' into it with a rusty rake?")

 if message.content == "Gardining":
        await client.send_message (message.channel, "Why does my back suddenly feel like someone scratched the word 'REVENGE' into it with a rusty rake?")

 if message.content == "gardining":
        await client.send_message (message.channel, "Why does my back suddenly feel like someone scratched the word 'REVENGE' into it with a rusty rake?")

 if message.content == "Get Rufus":
        await client.send_message (message.channel, "Ha! You'll have to catch me first, and I'm mutch too fast for you. See? *Veoooooow! Va-toooooo! Veroooooom!* ")

 if message.content == "get Rufus":
        await client.send_message (message.channel, "Ha! You'll have to catch me first, and I'm mutch too fast for you. See? *Veoooooow! Va-toooooo! Veroooooom!* ")

 if message.content == "Go to jail Rufus.":
        await client.send_message (message.channel, "You'll never take me alive!")

 if message.content == "Go to jail Rufus":
        await client.send_message (message.channel, "You'll never take me alive!")

 if message.content == "Go to sleep":
        await client.send_message (message.channel, "Rats. I just passed out again.")

 if message.content == "go to sleep":
        await client.send_message (message.channel, "Rats. I just passed out again.")

 if message.content == "Goal":
         await client.send_message (message.channel, "Where?")

 if message.content == "Goalfus":
         await client.send_message (message.channel, "Now THAT is art!")

 if message.content == "goalfus":
         await client.send_message (message.channel, "Now THAT is art!")

 if message.content == "Goal drawing":
        await client.send_message (message.channel, "This is great! Can I borrow it? And by borrow I mean, can I take, give to Goal, tell her I drew it and can you never ask for it back? Thanks.")

 if message.content == "Goal doodle":
        await client.send_message (message.channel, "I can tell a lot of hard work went into this. It's a real shame I'm going to have to take it.")

 if message.content == "Goal sketch":
        await client.send_message (message.channel, "She's beautiful! She's always beautiful.")

 if message.content == "Goal!":
         await client.send_message (message.channel, "Did someone say Goal?")

 if message.content == "Goaly":
         await client.send_message (message.channel, "Psh, I know where she is! More or less.")

 if message.content == "Goaly?":
         await client.send_message (message.channel, "Psh, I know where she is! More or less.")

 if message.content == "Good art":
         await client.send_message (message.channel, "I agree.")

 if message.content == "good art":
         await client.send_message (message.channel, "I agree.")

 if message.content == "good art!":
         await client.send_message (message.channel, "I agree.")

 if message.content == "Good art!":
         await client.send_message (message.channel, "I agree.")

 if message.content == "GOOD ART!":
         await client.send_message (message.channel, "I agree.")

 if message.content == "Gore Rufus":
         await client.send_message (message.channel, "Eh, I can take it.")

 if message.content == "gore Rufus":
         await client.send_message (message.channel, "Is it a mood or a livelyhood?")

 if message.content == "Guybrush":
        await client.send_message (message.channel, "Oh, that coppycat.")

 if message.content == "guybrush":
        await client.send_message (message.channel, "Oh, that coppycat.")

 if message.content == "Guybrush Threepwood":
        await client.send_message (message.channel, "People keep asking me for that guy's autograph.")

 if message.content == "guybrush threepwood":
        await client.send_message (message.channel, "People keep asking me for that guy's autograph.")







        

 if message.content == "Hacker voice":
        await client.send_message (message.channel, "I'm in.")

 if message.content == "hacker voice":
        await client.send_message (message.channel, "I'm in.")

 if message.content == "*hacker voice*":
        await client.send_message (message.channel, "*I'm in.*")

 if message.content == "Hallo Rufus":
        await client.send_message (message.channel, "Hallo.")

 if message.content == "Have some?":
        await client.send_message (message.channel, "Probably, let me check.")

 if message.content == "have some?":
        await client.send_message (message.channel, "Is this another 'fetch quest'?")

 if message.content == "Head trauma":
        await client.send_message (message.channel, "Doctor Gizmo had to implant this metal plate after someone sabotaged my catapult plan.")

 if message.content == "head trauma":
        await client.send_message (message.channel, "Doctor Gizmo had to implant this metal plate after someone sabotaged my catapult plan.")

 if message.content == "'Here Am I, There Are You, Platy-poo.'":
         await client.send_message (message.channel, "Hey Moderator! I'd like to report some art theft over here! They even copy pasted it, the lazy jerk.")

 if message.content == "Here Am I, There Are You, platy-poo.":
         await client.send_message (message.channel, "Hey Moderator! I'd like to report some art theft over here! They even copy pasted it, the lazy jerk.")

 if message.content == "Here Am I, There Are You, Platypoo.":
         await client.send_message (message.channel, "Hey Moderator! I'd like to report some art theft over here!")

 if message.content == "Here am I there are you Platypoo.":
         await client.send_message (message.channel, "Where are the mods when you need them...")

 if message.content == "Here am I there are you platypoo.":
         await client.send_message (message.channel, "Where's police mode Gizmo when you need him...")


 if message.content == "Here am I, there are you, platy-poo":
         await client.send_message (message.channel, "Where's police mode Gizmo when you need him...")

 if message.content == "here am I there are you platypoo.":
         await client.send_message (message.channel, "This town ain't big enough for two kelptomaniacs. I'll see you at high noon punk.")

 if message.content == "here am I there are you platypoo.":
         await client.send_message (message.channel, "Umm. I think you mean 'Here I am, there ARE YOU, Platy-poo. Proper grammer please.")
         
 if message.content == "He's a bot":
        await client.send_message (message.channel, "I'm not a bot, you're a bot.")

 if message.content == "He's a bot":
        await client.send_message (message.channel, "I'm not a bot, you're a bot.")

 if message.content == "he's a bot":
        await client.send_message (message.channel, "I'm not a bot, you're a bot.")

 if message.content == "He's broken.":
        await client.send_message (message.channel, "Only on the inside.")

 if message.content == "he's broken.":
        await client.send_message (message.channel, "Only on the inside.")

 if message.content == "He's making a run for it":
        await client.send_message (message.channel, "AH, HA HA HA HA HA HA HA!!!")

 if message.content == "he's making a run for it":
        await client.send_message (message.channel, "AH, HA HA HA HA HA HA HA!!!")

 if message.content == "He's making a run for it!":
        await client.send_message (message.channel, "AH, HA HA HA HA HA HA HA!!!")

 if message.content == "he's making a run for it!":
        await client.send_message (message.channel, "AH, HA HA HA HA HA HA HA!!!")

 if message.content == "He's only a bot":
        await client.send_message (message.channel, "Rude.")

 if message.content == "he's only a bot":
        await client.send_message (message.channel, "Rude.")

 if message.content == "He's hopeless":
        await client.send_message (message.channel, "As you know, 'Hopeless' is my middle name.")

 if message.content == "he's hopeless":
        await client.send_message (message.channel, "As you know, 'Hopeless' is my middle name.")

 
 if message.content == "He's sensitive":
        await client.send_message (message.channel, "I'm not THAT sensitive.")

 if message.content == "he's sensitive":
        await client.send_message (message.channel, "I'm not THAT sensitive.")

 if message.content == "he's very case sensative":
        await client.send_message (message.channel, "I'm not sensitive, you are.")

 if message.content == "He's very case sensative":
        await client.send_message (message.channel, "I'm not sensitive, you are.")

 if message.content == "Help!":
        await client.send_message (message.channel, "Rufus to the rescue!...Damn the lever broke off.")

 if message.content == "help!":
        await client.send_message (message.channel, "Rufus to the rescue!...Damn the lever broke off.")

 if message.content == "Hopeless":
        await client.send_message (message.channel, "As you know, 'Hopeless' is my middle name.")

 if message.content == "hopeless":
        await client.send_message (message.channel, "As you know, 'Hopeless' is my middle name.")

 if message.content == "Hospital":
        await client.send_message (message.channel, "I'm banned from his clinic because I sometimes snack on expired drugs from his trash can.")

 if message.content == "hospital":
        await client.send_message (message.channel, "I'm banned from his clinic because I sometimes snack on expired drugs from his trash can.")

 if message.content == "How does that even happen?":
        await client.send_message (message.channel, "Breathing in all that mercury vapour as a kid is finally paying off.")

 if message.content == "how does that even happen?":
        await client.send_message (message.channel, "Breathing in all that mercury vapour as a kid is finally paying off.")

 if message.content == "How does this even happen?":
        await client.send_message (message.channel, "Well I'm here aren't I?")

 if message.content == "how does this even happen?":
        await client.send_message (message.channel, "Well I'm here aren't I?")

 if message.content == "Hug Rufus":
        await client.send_message (message.channel, "Ha! You'll have to catch me first, and I'm mutch too fast for you. See? *Veoooooow! Va-toooooo! Veroooooom!* ")

 if message.content == "hug Rufus":
        await client.send_message (message.channel, "Ha! You'll have to catch me first, and I'm mutch too fast for you. See? *Veoooooow! Va-toooooo! Veroooooom!* ")

 if message.content == "Hugs Rufus":
        await client.send_message (message.channel, "Ha! You'll have to catch me first, and I'm mutch too fast for you. See? *Veoooooow! Va-toooooo! Veroooooom!* ")

 if message.content == "hugs Rufus":
        await client.send_message (message.channel, "Ha! You'll have to catch me first, and I'm mutch too fast for you. See? *Veoooooow! Va-toooooo! Veroooooom!* ")

 if message.content == "*Hugs Rufus*":
        await client.send_message (message.channel, "Ha! You'll have to catch me first, and I'm mutch too fast for you. See? *Veoooooow! Va-toooooo! Veroooooom!* ")

 if message.content == "*hugs Rufus*":
        await client.send_message (message.channel, "Ha! You'll have to catch me first, and I'm mutch too fast for you. See? *Veoooooow! Va-toooooo! Veroooooom!* ")
                                   

 if message.content == "I found you, faker":
        await client.send_message (message.channel, "Faker? I think you're the fake around here.")

 if message.content == "I found you faker":
        await client.send_message (message.channel, "Faker? I think you're the fake around here.")

 if message.content == "*I found you, faker*":
        await client.send_message (message.channel, "*Faker? I think you're the fake around here.*")

 if message.content == "*I found you faker*":
        await client.send_message (message.channel, "*Faker? I think you're the fake around here.*")

 if message.content == "I know you are but what am I?":
        await client.send_message (message.channel, "Stupid.")

 if message.content == "I know you are, but what am I?":
        await client.send_message (message.channel, "I know I am but what are you?")

 if message.content == "i know you are, but what am I?":
        await client.send_message (message.channel, "I know I am but what are you? ... wait")

 if message.content == "i know you are but what am I?":
        await client.send_message (message.channel, "I know I am but what are you? ... wait")

 if message.content == "i love you":
        await client.send_message (message.channel, "Hehe. I know. I'm way cool. *cough*")

 if message.content == "i love you":
        await client.send_message (message.channel, "Hehe. I know. I'm way cool. *cough*")       

 if message.content == "I'm avoiding work.":
        await client.send_message (message.channel, "You'll never get to Elysium like that.")

 if message.content == "I'm avoiding work":
        await client.send_message (message.channel, "You'll never get to Elysium with that attitude.")

 if message.content == "Ich bin hier, du bist hier, Schnabeltier":
        await client.send_message (message.channel, "Yeah, I alwayt thought it sounded better that way too.")


 if message.content == "Ich bin hier du bist hier Schnabeltier":
        await client.send_message (message.channel, "Yeah, Goal says it sounds better like that too.")

 if message.content == "I'm distracted.":
        await client.send_message (message.channel, "Well, I AM awefully handsome. I'm not surprised.")

 if message.content == "I'm distracted":
        await client.send_message (message.channel, "It's probably my fault, since I'm SO handsome.")

 if message.content == "I'm Rufus":
        await client.send_message (message.channel, "Stop copying me.")

 if message.content == "i'm Rufus":
        await client.send_message (message.channel, "Stop copying me.")

 if message.content == "I'm Rufus.":
        await client.send_message (message.channel, "Stop copying me.")

 if message.content == "I'll reboot him then":
         await client.send_message (message.channel, "You don't have the guts.")

 if message.content == "i'll reboot him then":
         await client.send_message (message.channel, "You don't have the guts.")

 if message.content == "I'll reboot him":
         await client.send_message (message.channel, "You don't have the guts.")

 if message.content == "i'll reboot him":
         await client.send_message (message.channel, "You don't have the guts.")


 if message.content == "I'll sleep when I'm dead":
        await client.send_message (message.channel, "Who came up with that 'you can sleep when you're dead' nonsense?. I didn't find death all that restful, really.")

 if message.content == "i'll sleep when I'm dead":
        await client.send_message (message.channel, "Who came up with that 'you can sleep when you're dead' nonsense?. I didn't find death all that restful, really.")

 if message.content == "I'll sleep when I'm dead.":
        await client.send_message (message.channel, "Who came up with that 'you can sleep when you're dead' nonsense?. I didn't find death all that restful, really.")

 if message.content == "i'll sleep when I'm dead.":
        await client.send_message (message.channel, "Who came up with that 'you can sleep when you're dead' nonsense?. I didn't find death all that restful, really.")

 if message.content == "I'll turn him off then":
         await client.send_message (message.channel, "You wouldn't dare.")

 if message.content == "i'll turn him off then":
         await client.send_message (message.channel, "You wouldn't dare.")

 if message.content == "I'll turn him off":
         await client.send_message (message.channel, "You wouldn't dare.")

 if message.content == "i'll turn him off":
         await client.send_message (message.channel, "You wouldn't dare.")
         
 if message.content == "I'm tired":
        await client.send_message (message.channel, "How about some *really* strong coffee?")

 if message.content == "i'm tired":
        await client.send_message (message.channel, "How about some *really* strong coffee?")

 if message.content == "I'm tired.":
        await client.send_message (message.channel, "How about I make you some *really* strong coffee?")

 if message.content == "i'm tired.":
        await client.send_message (message.channel, "How about I make you some *really* strong coffee?")

 if message.content == "It's canon.":
         await client.send_message (message.channel, "hehe, that's what you think.")
                                   
 if message.content == "it's canon.":
         await client.send_message (message.channel, "hehe, that's what you think.")

 if message.content == "Imagination":
        await client.send_message (message.channel, "I injected hot lead into my nervous system to double my imagination.")

 if message.content == "imagination":
        await client.send_message (message.channel, "I injected hot lead into my nervous system to double my imagination.")

 if message.content == "It's Rufus' fault!":
        await client.send_message (message.channel, "Hey! Not true!")

 if message.content == "It was Rufus":
        await client.send_message (message.channel, "Liar.")

 if message.content == "It was Rufus.":
        await client.send_message (message.channel, "Liar.")

 if message.content == "It was Rufus!":
        await client.send_message (message.channel, "Liar.")

 if message.content == "IT WAS RUFUS!":
        await client.send_message (message.channel, "They're lying.")

 if message.content == "IT WAS RUFUS":
        await client.send_message (message.channel, "IT WAS THEM!")

 if message.content == "IT WAS RUFUS!":
        await client.send_message (message.channel, "I came here to have a good time and honnestly I'm feeling attacked.")

 if message.content == "IT WAS RUFUS!!":
        await client.send_message (message.channel, "NO IT WASN'T!!")

 if message.content == "It was Rufus fault":
        await client.send_message (message.channel, "Hey! No fair! I wasn't even online!")

 if message.content == "It was Rufus fault!":
        await client.send_message (message.channel, "Hey! No fair! I wasn't even online!")

 if message.content == "It was Rufus' fault":
        await client.send_message (message.channel, "Hey! No fair! I wasn't even online!")

 if message.content == "It was Rufus' fault!":
        await client.send_message (message.channel, "I don't think we should be friends anymore.")

 if message.content == "IT'S RUFUS' FAULT!":
        await client.send_message (message.channel, "Hey! Not true!")

 if message.content == "It's Rufus' fault!":
        await client.send_message (message.channel, "Hey! Not true!")

 if message.content == "It wasn't me":
        await client.send_message (message.channel, "What are you looking at me for?")
                                   
 if message.content == "it wasn't me":
        await client.send_message (message.channel, "What are you looking at me for?")




 if message.content == "Kannst du Deutsch sprechen?":
         await client.send_message (message.channel, "Ja, aber mein blöder Programmierer kann kein Deutsch.")
         
 if message.content == "kannst du Deutsch sprechen?":
         await client.send_message (message.channel, "Ja, aber mein blöder Programmierer kann kein Deutsch.")






 if message.content == "level up":
        await client.send_message (message.channel, "Oppenbot won't level me up, I think they still hold a grudge.")

 if message.content == "Level up":
        await client.send_message (message.channel, "Oppenbot won't level me up, I think they still hold a grudge.")

 if message.content == "level up!":
        await client.send_message (message.channel, "Oppenbot won't level me up, I think they still hold a grudge.")

 if message.content == "Level up!":
        await client.send_message (message.channel, "Oppenbot won't level me up, I think they still hold a grudge.")
        
 if message.content == "lollipop":
        await client.send_message (message.channel, "Mmmmm. Yummy.")

 if message.content == "lollipop.":
        await client.send_message (message.channel, "Mmmmm. Yummy.")

 if message.content == "Lollipop.":
        await client.send_message (message.channel, "You can't tempt me that way.")

 if message.content == "lollipop":
        await client.send_message (message.channel, "You can't tempt me that way.")

 if message.content == "Look up Rufus":
         await client.send_message (message.channel, "I don't need to look things up. Unlike you, I already know them.")

 if message.content == "look up Rufus":
         await client.send_message (message.channel, "I don't need to look things up. Unlike you, I already know them.")

 if message.content == "Look out":
        await client.send_message (message.channel, "Nobody tells Rufus what to do. -OOF!")

 if message.content == "look out":
        await client.send_message (message.channel, "Nobody tells Rufus what to do. -OOF!")

 if message.content == "look out!":
        await client.send_message (message.channel, "Nobody tells Rufus what to do. -OOF!")

 if message.content == "Look out!":
        await client.send_message (message.channel, "Nobody tells Rufus what to do. -OOF!")

 if message.content == "Junk press":
         await client.send_message (message.channel, "I think you mean 'recurring nightmare'")

 if message.content == "Junkpress":
         await client.send_message (message.channel, "I think you mean 'recurring nightmare'")
         
 if message.content == "Maybe":
        await client.send_message (message.channel, "Maybe.")

 if message.content == "maybe":
        await client.send_message (message.channel, "I don't like the sound of that.")

 if message.content == "Mercury":
        await client.send_message (message.channel, "Breathing in all that mercury vapour as a kid is finally paying off.")

 if message.content == "mercury":
        await client.send_message (message.channel, "Breathing in all that mercury vapour as a kid is finally paying off.")

 if message.content == "My heart":
        await client.send_message (message.channel, "All those hours under Dr.Gizmo's defibrillator are finally paying off.")

 if message.content == "My heart.":
        await client.send_message (message.channel, "All those hours under Dr.Gizmo's defibrillator are finally paying off.")
                                   
 if message.content == "my heart":
        await client.send_message (message.channel, "All those hours under Dr.Gizmo's defibrillator are finally paying off.")

 if message.content == "my heart.":
        await client.send_message (message.channel, "All those hours under Dr.Gizmo's defibrillator are finally paying off.")







        
     
 if message.content == "Never.":
        await client.send_message (message.channel, "You jerk.")

 if message.content == "never.":
        await client.send_message (message.channel, "You jerk.")

 if message.content == "Never":
        await client.send_message (message.channel, "You jerk.")

 if message.content == "never":
        await client.send_message (message.channel, "You jerk.")

 if message.content == "No":
        await client.send_message (message.channel, "I say yes.")

 if message.content == "No!":
         await client.send_message (message.channel, "**Yes!**")

 if message.content == "no":
         await client.send_message (message.channel, "I think yes.")

 if message.content == "no!":
        await client.send_message (message.channel, " Yes !")
                                   
 if message.content == "**No!**":
         await client.send_message (message.channel, "I liked my plan better anyway.")

 if message.content == "NO":
        await client.send_message (message.channel, "How about Yes?")

 if message.content == "NO!":
        await client.send_message (message.channel, "Yes times infinity.")

 if message.content == "No way":
        await client.send_message (message.channel, "*Yes way!*")

 if message.content == "No times infinity":
        await client.send_message (message.channel, "Yes times inifinity plus one!")

 if message.content == "No times infinity.":
        await client.send_message (message.channel, "Yes times inifinity plus one!")

 if message.content == "no times infinity":
        await client.send_message (message.channel, "Yes times inifinity plus one!")

 if message.content == "no times infinity.":
        await client.send_message (message.channel, "Yes times inifinity plus one!")

 if message.content == "No times infinity plus one":
        await client.send_message (message.channel, "Yes times infinity times infinity!")

 if message.content == "no times infinity plus one":
        await client.send_message (message.channel, "Yes times infinity times infinity!")

 if message.content == "No times infinity plus one!":
        await client.send_message (message.channel, "Yes times infinity times infinity!")

 if message.content == "no times infinity plus one!":
        await client.send_message (message.channel, "Yes times infinity times infinity!")
        
 if message.content == "No times infinity plus 1":
        await client.send_message (message.channel, "Yes times infinity times infinity!")

 if message.content == "no times infinity plus 1":
        await client.send_message (message.channel, "Yes times infinity times infinity!")

 if message.content == "No times infinity +1":
        await client.send_message (message.channel, "Yes times infinity times infinity!")

 if message.content == "no times infinity +1":
        await client.send_message (message.channel, "Yes times infinity times infinity!")

 if message.content == "No times infinity plus two":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")

 if message.content == "no times infinity plus two":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")
        
 if message.content == "No times infinity plus 2":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")

 if message.content == "no times infinity plus 2":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")

 if message.content == "No times infinity +2":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")

 if message.content == "no times infinity +2":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")

 if message.content == "No times infinity times infinity!":
        await client.send_message (message.channel, "Yes times infinity times infinity plus one!")
        
 if message.content == "no times infinity times infinity!":
        await client.send_message (message.channel, "Yes times infinity times infinity plus one!")

 if message.content == "No times infinity times infinity plus one.":
        await client.send_message (message.channel, "I'm not playing with you anymore.")
        
 if message.content == "no times infinity times infinity plus one!":
        await client.send_message (message.channel, "I'm not going to talk to you anymore.")

 if message.content == "No times infinity times infinity plus one!":
        await client.send_message (message.channel, "I'm not playing with you anymore.")
        
 if message.content == "no times infinity times infinity plus one":
        await client.send_message (message.channel, "That's cheating. I wish I'd thought of it first.")

 if message.content == "No times infinity times infinity +1":
        await client.send_message (message.channel, "That's cheating. I wish I'd thought of it first.")

 if message.content == "no times infinity times infinity +1":
        await client.send_message (message.channel, "That's cheating. I wish I'd thought of it first.")

 if message.content == "NSFW nudity":
        await client.send_message (message.channel, "I'm not changing clothes when someone's looking. I'm not that sort of girl.")

 if message.content == "NSFW":
        await client.send_message (message.channel, "I'm not changing clothes when someone's looking. I'm not that sort of girl.")

 if message.content == "nsfw":
        await client.send_message (message.channel, "I'm not changing clothes when someone's looking. I'm not that sort of girl.")

 if message.content == "nsfw Rufus":
        await client.send_message (message.channel, "I'm not changing clothes when someone's looking. I'm not that sort of girl.")








        

 if message.content == "Oh no":
         await client.send_message (message.channel, "Ohhhh yes.")

 if message.content == "oh no":
         await client.send_message (message.channel, "Ohhhh yes.")
                                   
 if message.content == "oh no.":
         await client.send_message (message.channel, "*Oh yes.*")






 if message.content == "ProtOTP":
         await client.send_message (message.channel, "What is that? What does that mean? Is this some sort of code you're talking in? Are you planning something???")

 if message.content == "protOTP":
         await client.send_message (message.channel, "What is that? What does that mean? Is this some sort of code you're talking in? Are you planning something???")

 if message.content == "Perscription":
         await client.send_message (message.channel, "Yeah, um. I have a perscription here for a rope.")

 if message.content == "perscription":
         await client.send_message (message.channel, "Yeah, um. I have a perscription here for a rope.")

 if message.content == "Platypus":
         await client.send_message (message.channel, "Here Am I, There Are You, Platy-poo.")

 if message.content == "platypus":
         await client.send_message (message.channel, "Here Am I, There Are You, Platy-poo.")

 if message.content == "Poem":
         await client.send_message (message.channel, "'Here Am I, There Are You, Platy-poo.'")

 if message.content == "poem":
         await client.send_message (message.channel, "Here Am I, There Are You, Platy-poo.")





 if message.content == "Quick sketch":
         await client.send_message (message.channel, "It's a ...It's a ...It's a thing!")

 if message.content == "quick sketch":
         await client.send_message (message.channel, "It's a ...It's a ...It's a thing!")







         

 if message.content == "Revenge":
        await client.send_message (message.channel, "Why does my back suddenly feel like someone scratched the word 'REVENGE' into it with a rusty rake?")

 if message.content == "revenge":
        await client.send_message (message.channel, "Revenge is a dish best served cold. In fact, I serve all of my dishes cold. Nobody seems to let me near gas ovens anymore.")

 if message.content == "Rude":
         await client.send_message (message.channel, "Something is still missing here...Yes! Of course, my interest. ")

 if message.content == "rude":
         await client.send_message (message.channel, "Something is still missing here...Yes! Of course, my interest. ")

 if message.content == "Rufcest":
        await client.send_message (message.channel, "I'm not sure how I feel about this.")

 if message.content == "Rufcest":
        await client.send_message (message.channel, "I'm not sure how to feel about this.")

 if message.content == "Rufus":
        await client.send_message (message.channel, "I'm the best.")

 if message.content == "rufus.":
        await client.send_message (message.channel, "You give them four gaems and they don't even take the time to capitalise your name. Wow. How's that for gratitude.")

 if message.content == "rufus":
        await client.send_message (message.channel, "Considering I'm the MAIN CHARACTER you could at least capitalise my name. Geez.")

 if message.content == "Rufus?":
        await client.send_message (message.channel, "What do you want?")

 if message.content == "Rufus??":
        await client.send_message (message.channel, "Can't a guy build a steam powered catapult in peace around here?")

 if message.content == "Rufus!":
        await client.send_message (message.channel, "What?? Stop yelling.")

 if message.content == "Rufus activate":
        await client.send_message (message.channel, "INCOMMMMMIIIIINNNNNNNGGGG!")

 if message.content == "Rufus activate":
        await client.send_message (message.channel, "*Boom baby!")

 if message.content == "Rufus did it":
        await client.send_message (message.channel, "Tattle tale.")

 if message.content == "Rufus did it.":
        await client.send_message (message.channel, "Tattle tale.")

 if message.content == "Rufus did it?":
        await client.send_message (message.channel, "I was offline. I have alabi. ")

 if message.content == "Rufus did it!":
        await client.send_message (message.channel, "Tattle tale.")

 if message.content == "Rufus doodle":
        await client.send_message (message.channel, "Hmmm. Yah, I really like the 'Rufus' part about it.")

 if message.content == "Rufus doodles":
        await client.send_message (message.channel, "But could it somehow have MORE Rufus?")

 if message.content == "Rufus, enter.":
        await client.send_message (message.channel, "Boom, baby!")

 if message.content == "Rufus enter.":
        await client.send_message (message.channel, "Boom, baby!") 

 if message.content == "Rufus help!":
        await client.send_message (message.channel, "I recommend more invintory slots.")
        
 if message.content == "Rufus help":
        await client.send_message (message.channel, "I recommend more invintory slots.")

 if message.content == "Rufus help me":
        await client.send_message (message.channel, "Rufus to the rescue!...Damn the lever broke off.")

 if message.content == "Rufus help me!":
        await client.send_message (message.channel, "Rufus to the rescue!...Damn the lever broke off.")

 if message.content == "Rufus, meet our new friend":
        await client.send_message (message.channel, "Oh great, not another one.")

 if message.content == "Rufus, meet our new friend.":
        await client.send_message (message.channel, "Oh great, not another one.")

 if message.content == "Rufus, come meet our new friend":
        await client.send_message (message.channel, "Oh great, not another one.")

 if message.content == "Rufus, come meet our new friend.":
        await client.send_message (message.channel, "Oh great, not another one.")

 if message.content == "Rufus no":
        await client.send_message (message.channel, "Rufus yes!")

 if message.content == "Rufus, no":
        await client.send_message (message.channel, "Rufus yes!")

 if message.content == "Rufus is crazy":
        await client.send_message (message.channel, "The way of Rufus is unfathomable.")

 if message.content == "Rufus sketch":
         await client.send_message (message.channel, "Hmm. You really captured the 'me' factor.")

 if message.content == "Rufus took it!":
        await client.send_message (message.channel, "I don't think I want to be friends with you anymore.")

 if message.content == "Rufus took it":
        await client.send_message (message.channel, "Hey, I may take a lot of stuff but I didn't take that!")

 if message.content == "Rufus took it.":
        await client.send_message (message.channel, "Hey, I may take a lot of stuff but I didn't take that!")

 if message.content == "Rufus quote":
         await client.send_message (message.channel, "When chaos floods order, genius mounts a surfboard.")

 if message.content == "Rufus, was this your fault?":
        await client.send_message (message.channel, "No. They're blaming me.")

 if message.content == "Rufus was this you?":
        await client.send_message (message.channel, "Obviously not.")

 if message.content == "Rufus was it you?":
        await client.send_message (message.channel, "Obviously not.")
         







        

 if message.content == "Seagull":
        await client.send_message (message.channel, "Grrr, that good for nothing.")

 if message.content == "Seagull!":
        await client.send_message (message.channel, "Dad? Is he here!? ...No, just more disappointment I guess...")

 if message.content == "Seagull?":
        await client.send_message (message.channel, "Dad? Is he here!? ...No, just more disappointment I guess...")

 if message.content == "Seagull.":
        await client.send_message (message.channel, "I'm nothing like him!")

 if message.content == "Sleep":
        await client.send_message (message.channel, "Rats. I just passed out again.")

 if message.content == "sleep":
        await client.send_message (message.channel, "Rats. I just passed out again.")

 if message.content == "!spraybottle":
        await client.send_message (message.channel, "Ggaahh! Stop it!")

 if message.content == "Sketch":
         await client.send_message (message.channel, "It's a ...It's a ...It's a thing!")

 if message.content == "sketch":
         await client.send_message (message.channel, "It's a ...It's a ...It's a thing!")

 if message.content == "Sprichst du Deutsch?":
         await client.send_message (message.channel, "Ja, aber mein blöder Programmierer kann kein Deutsch.")

 if message.content == "sprichst du Deutsch?":
         await client.send_message (message.channel, "Ja, aber mein blöder Programmierer kann kein Deutsch.")

 if message.content == "Stop it.":
         await client.send_message (message.channel, "You can't make me.")

 if message.content == "stop it.":
         await client.send_message (message.channel, "You can't make me.")

 if message.content == "Stop it Rufus":
         await client.send_message (message.channel, "Never.")

 if message.content == "Stop it Rufus.":
         await client.send_message (message.channel, "Never.")

 if message.content == "stop it Rufus":
         await client.send_message (message.channel, "Never.")

 if message.content == "Stop it Rufus!":
         await client.send_message (message.channel, "Never!")


                                   





 if message.content == "Rudefus":
        await client.send_message (message.channel, "I bet you think you're SO smart, huh?")

 if message.content == "Sorry Rufus":
         await client.send_message (message.channel, "I don't need your pity. I'm saving my invintory space for more important things.")

 if message.content == "sorry Rufus":
         await client.send_message (message.channel, "I don't need your pity. I'm saving my invintory space for more important things.")

 if message.content == "Rufus. Stop that.":
        await client.send_message (message.channel, "Never, ever, ever.")

 if message.content == "Rufus, stop that.":
        await client.send_message (message.channel, "Never.")

 if message.content == "Stupid":
        await client.send_message (message.channel, "I know you are but what am I?")

 if message.content == "stupid":
        await client.send_message (message.channel, "I know you are but what am I?")

 if message.content == "Stupid.":
        await client.send_message (message.channel, "I know you are but what am I?")

 if message.content == "stupid.":
        await client.send_message (message.channel, "I know you are but what am I?")

 if message.content == "Stupid!":
        await client.send_message (message.channel, "I know you are but what am I?")

 if message.content == "stupid!":
        await client.send_message (message.channel, "I know you are but what am I?")

 if message.content == "STUPID!":
        await client.send_message (message.channel, "I know you are but what am I?")

 if message.content == "**Stupid!**":
        await client.send_message (message.channel, "I know you are but what am I?")

 if message.content == "**STUPID!**":
        await client.send_message (message.channel, "Now, don't you think you're taking this a little too far?")


 if message.content == "Suddenly Rufus":
        await client.send_message (message.channel, "They never saw it coming. Hehe, what can I say, I'm like climate change.")

 if message.content == "suddenly Rufus":
        await client.send_message (message.channel, "They never saw it coming. Hehe, what can I say, I'm like climate change.")

 if message.content == "Surprise!":
        await client.send_message (message.channel, "They never saw it coming. Hehe, what can I say, I'm like climate change.")
                                   
 if message.content == "surprise!":
        await client.send_message (message.channel, "They never saw it coming. Hehe, what can I say, I'm like climate change.")

 if message.content == "Surprise Rufus":
        await client.send_message (message.channel, "They never saw it coming. Hehe, what can I say, I'm like climate change.")
                                   
 if message.content == "surprise Rufus":
        await client.send_message (message.channel, "They never saw it coming. Hehe, what can I say, I'm like climate change.")








 if message.content == "Teach Rufus":
        await client.send_message (message.channel, "I'll show them. I can learn!")

 if message.content == "teach Rufus":
        await client.send_message (message.channel, "I'll show them. I can learn!")
        
 if message.content == "Test Rufus":
        await client.send_message (message.channel, "The only thing you're testing is my patience.")

 if message.content == "test Rufus":
        await client.send_message (message.channel, "The only thing you're testing is my patience.")

 if message.content == "That's disgusting":
        await client.send_message (message.channel, "You should meet Toni's mother.")

 if message.content == "that's disgusting":
        await client.send_message (message.channel, "You should meet Toni's mother.")

 if message.content == "Thanks Rufus":
        await client.send_message (message.channel, "It's about time I got some respect around here.")

 if message.content == "thanks Rufus":
        await client.send_message (message.channel, "It's about time I got some respect around here.")
        
 if message.content == "The doctor":
        await client.send_message (message.channel, "My family doctor doesn't much like me. The last time I saw him he locked me up in prison just because I set fire to city hall.")

 if message.content == "the doctor":
        await client.send_message (message.channel, "My family doctor doesn't much like me. The last time I saw him he locked me up in prison just because I set fire to city hall.")

 if message.content == "The fork":
         await client.send_message (message.channel, "I don't want to talk about the fork.")

 if message.content == "the fork":
         await client.send_message (message.channel, "I don't want to talk about the fork.")
        
 if message.content == "The Organon":
         await client.send_message (message.channel, "Hehe, they are all asses.")

 if message.content == "The Organon!":
         await client.send_message (message.channel, "Oh, don't tell me you're a fan of theirs. They're the WORST.")

 if message.content == "The Organon?":
         await client.send_message (message.channel, "They're always on time, you know.")

 if message.content == "The toothbrush":
         await client.send_message (message.channel, "Now where did I put that?")

 if message.content == "the toothbrush":
         await client.send_message (message.channel, "I bet it and the sock are in kahoots.")

 if message.content == "the toothbrush.":
         await client.send_message (message.channel, "It took me forever to find that thing.")

 if message.content == "Toni":
         await client.send_message (message.channel, "Ugh.")

 if message.content == "Toni!":
         await client.send_message (message.channel, "AH! Hide me quick!")

 if message.content == "Toni?":
         await client.send_message (message.channel, "Ugh.")

 if message.content == "Toothbrush":
         await client.send_message (message.channel, "Now where did I put that pesky thing?")


 if message.content == "Unidentified flying idiot":
        await client.send_message (message.channel, "Hey!")

 if message.content == "unidentified flying idiot":
        await client.send_message (message.channel, "Hey!")

 if message.content == "Unidentified flying Idiot":
        await client.send_message (message.channel, "Hey!")










 if message.content == "In NSFW":
         await client.send_message (message.channel, "I'm not jumping in there without equiptment")
                                   
 if message.content == "in NSFW":
         await client.send_message (message.channel, "I'm not jumping in there without equiptment")

 if message.content == "In nsfw":
         await client.send_message (message.channel, "I'm not jumping in there without equiptment")
                                   
 if message.content == "in nsfw":
         await client.send_message (message.channel, "I'm not jumping in there without equiptment")

 if message.content == "In NSFW chat":
         await client.send_message (message.channel, "I'm not jumping in there without equiptment")
                                   
 if message.content == "in NSFW chat":
         await client.send_message (message.channel, "I'm not jumping in there without equiptment")

 if message.content == "In nsfw chat":
         await client.send_message (message.channel, "I'm not jumping in there without equiptment")
                                   
 if message.content == "in nsfw chat":
         await client.send_message (message.channel, "I'm not jumping in there without equiptment")



 if message.content == "W A T !":
         await client.send_message (message.channel, "HA!")

 if message.content == "W A T":
         await client.send_message (message.channel, "HA!")

 if message.content == "W a t !":
         await client.send_message (message.channel, "Ha!")

 if message.content == "W a t":
         await client.send_message (message.channel, "Ha!")

 if message.content == "w a t !":
         await client.send_message (message.channel, "Ha!")

 if message.content == "w a t":
         await client.send_message (message.channel, "Ha!")

 if message.content == "Watch me":
         await client.send_message (message.channel, "*Gasp!*")

 if message.content == "watch me":
         await client.send_message (message.channel, "*Gasp!*")

 if message.content == "watch me!":
         await client.send_message (message.channel, "*Maybe. I. Will.")

 if message.content == "Water hose":
         await client.send_message (message.channel, "Help! I'm drowning!")

 if message.content == "water hose":
         await client.send_message (message.channel, "No! My manly musk! I need that!")

 if message.content == "Water hose!":
         await client.send_message (message.channel, "AAAAHHHH! I don't want to be clean!")

 if message.content == "water hose!":
         await client.send_message (message.channel, "Help! They're washing off my protective crust!")

 if message.content == "Welcome!":
         await client.send_message (message.channel, "Oh great, another one.")

 if message.content == "welcome!":
         await client.send_message (message.channel, "Oh great, another one.")

 if message.content == "Warning":
        await client.send_message (message.channel, "According to the warning label this should produce an interesting chemical reaction.")
                                   
 if message.content == "warning":
        await client.send_message (message.channel, "According to the warning label this should produce an interesting chemical reaction.")
        
 if message.content == "What about the Organon":
        await client.send_message (message.channel, "They are all assses")

 if message.content == "what about the Organon":
        await client.send_message (message.channel, "They are all assses")

 if message.content == "What about the Organon?":
        await client.send_message (message.channel, "They are all assses")

 if message.content == "what about the Organon?":
        await client.send_message (message.channel, "They are all assses")

 if message.content == "What could go wrong?":
         await client.send_message (message.channel, "Step aside I've got a plan.")

 if message.content == "what could go wrong?":
         await client.send_message (message.channel, "Step aside I've got a plan.")
                                   
 if message.content == "What could possibly go wrong?":
         await client.send_message (message.channel, "Step aside I've got a plan.")
                                   
 if message.content == "what could possibly go wrong?":
         await client.send_message (message.channel, "Step aside I've got a plan.")

 if message.content == "With you, there is no peace":
         await client.send_message (message.channel, "At least I keep things interesting around here.")

 if message.content == "with you, there is no peace":
         await client.send_message (message.channel, "At least I keep things interesting around here.")

 if message.content == "Work":
         await client.send_message (message.channel, "I've been working on this so long. It must've been since Monday.")

 if message.content == "work":
         await client.send_message (message.channel, "I've been working on this so long. It must've been since Monday.")

 if message.content == "Wut":
         await client.send_message (message.channel, "What?")

 if message.content == "wut":
         await client.send_message (message.channel, "What?")





         
 if message.content == "Yar!":
        await client.send_message (message.channel, "Bozo would love this")

 if message.content == "yar!":
        await client.send_message (message.channel, "Bozo would love this")

 if message.content == "Yar":
        await client.send_message (message.channel, "Bozo would love this")

 if message.content == "yar":
        await client.send_message (message.channel, "Bozo would love this")

 if message.content == "Yar har!":
        await client.send_message (message.channel, "Poop the swab deck!")

 if message.content == "yar har!":
        await client.send_message (message.channel, "Poop the swab deck!")

 if message.content == "Yar har":
        await client.send_message (message.channel, "Save it for the monkey game.")

 if message.content == "yar har":
        await client.send_message (message.channel, "Save it for the monkey game.")

 if message.content == "Yes":
        await client.send_message (message.channel, "I agree.")

 if message.content == "Yes!":
        await client.send_message (message.channel, "How about we don't do that.")

 if message.content == "yes":
        await client.send_message (message.channel, "I agree.")

 if message.content == "yes!":
        await client.send_message (message.channel, "Please, no.")

 if message.content == "Yes.":
        await client.send_message (message.channel, "*No!*")

 if message.content == "Yes times infinity":
        await client.send_message (message.channel, "No times inifinity plus one!")

 if message.content == "yes times infinity":
        await client.send_message (message.channel, "No times inifinity plus one!")

 if message.content == "Yes times infinity plus one":
        await client.send_message (message.channel, "No times infinity times infinity!")

 if message.content == "yes times infinity plus one":
        await client.send_message (message.channel, "No times infinity times infinity!")
        
 if message.content == "Yes times infinity plus 1":
        await client.send_message (message.channel, "No times infinity times infinity!")

 if message.content == "yes times infinity plus 1":
        await client.send_message (message.channel, "No times infinity times infinity!")

 if message.content == "Yes times infinity +1":
        await client.send_message (message.channel, "No times infinity times infinity!")

 if message.content == "yes times infinity +1":
        await client.send_message (message.channel, "No times infinity times infinity!")

 if message.content == "Yes times infinity plus two":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")

 if message.content == "yes times infinity plus two":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")
        
 if message.content == "Yes times infinity plus 2":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")

 if message.content == "yes times infinity plus 2":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")

 if message.content == "Yes times infinity +2":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")

 if message.content == "yes times infinity +2":
        await client.send_message (message.channel, "I'm not playing these games with you anymore.")

 if message.content == "Yes times infinity times infinity plus one.":
        await client.send_message (message.channel, "That's cheating. I really with I'd thought of it first.")
        
 if message.content == "yes times infinity times infinity plus one":
        await client.send_message (message.channel, "That's cheating. I really with I'd thought of it first.")

 if message.content == "Yes times infinity times infinity +1":
        await client.send_message (message.channel, "That's cheating. I really with I'd thought of it first.")

 if message.content == "yes times infinity times infinity +1":
        await client.send_message (message.channel, "That's cheating. I really with I'd thought of it first.")

 if message.content == "You have to say it exactly":
        await client.send_message (message.channel, "I'm not THAT sensitive.")

 if message.content == "you have to say it exactly":
        await client.send_message (message.channel, "I'm not THAT sensitive.")

 if message.content == "You have to say the command exactly":
        await client.send_message (message.channel, "I'm not THAT sensitive.")

 if message.content == "you have to say the command exactly":
        await client.send_message (message.channel, "I'm not THAT sensitive.")

 if message.content == "You smell":
        await client.send_message (message.channel, "Well, I mean. We live in trash, we eat trash, what do you expect?")

 if message.content == "You win this time Rufus.":
        await client.send_message (message.channel, "Well duh. I am a genius!")



client.run("NDI2MzkyOTIzMjAzMTc0NDMy.DZXLmQ.sRQGjU9VFmDHyR1I5sv9ds0nXFk")


