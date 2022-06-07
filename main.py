import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

quotes = ["\"Forget the Stack\" - Dr. Beasley 01/27/2022", "\"Imagine if we didn't hit a base case. Then your stack...would overflow\" - Dr. Beasley 01/27/2022", "\"Don't turn that into the TA's you won't get any points for that, you will just be making enemies\" - Dr. Beasley 02/09/2022", "\"3-1 is 2 which is greater than 1\" - Dr. Beasley 02/24/2022", "\"If I don't assign points to it, nobody is going to do it\" - Dr. Beasley 02/24/2022", "\"Will you be able to do this on the exam?\" - Dr. Beasley 03/03/2022", "\"I want to store their social security numbers\" - Dr. Beasley 03/08/2022", "\"Merge sort is like war\" - Dr. Beasley 03/24/2022", "That's a nice umbrella, might have to keep it\" - Dr. Beasley 03/24/2022", "\"No quicksort, mergesort, AVL trees on the exam... Oh wait hang on a second\" - Dr. Beasley 03/29/2022", "\"Chad gets mapped into slot 1 but there’s already someone there\" - Dr. Beasley 03/29/2022", "\"I increased the size of my vector\" - Dr. Beasley 04/05/2022", "\"This is not the D we were looking at\" - Dr. Beasley 04/07/2022", "\"It's a shame that this kind of content has to be in your Data Structures class...\" - Dr. Beasley 04/19/2022", "\"The best class I took was Object Oriented Programming\" - Jonathan the Guest Speaker 04/26/2021", "\"When I used to teach I would call on kids but now apparently that is taboo so I don't do it anymore instead I beg you guys to answer\" - Dr. Yalcin 04/27/2022", "\"You can share your P, but do not share your D\" - Dr. Theado 03/09/2022", "\"I am going to change it to my favorite color blue\" - Dr. Theado 03/09/2022", "\"Use your D to encrypt this\" - Dr. Theado 03/21/2022", "\"Here is an example no one cares about\" - Dr. Theado 04/04/2022", "\"Once we figure out where the balls go...\" - Dr. Theado 04/06/2022", "\"I am not making an easier exam, just learnthe concepts\" - Dr. Theado 04/20/2022", "\"When I was a kid, I had my favorite bowl I'd eat cereal out of. It was a blue plastic bowl. I just think blue is the best color\" - Dr. Theado 04/29/2022", "\"No one uses kmaps, in-fact, no one uses quine-mccluskey\" - Dr. Karam 02/07/2022", "\"Alright we need to end this\" - Dr. Yalcin 02/14/2022", "\"kmaps are fun and all, well actually no\" - Dr. Karam 02/15/2022", "\"Anyone wanna draw their tree that way\" - Dr. Beasley 02/22/2022", "\"I know there are not many fans of assembly here\" - Dr. Karam 02/24/2022", "\"I want ice-cream now\" - Dr. Karam 03/07/2022", "\"that kmap is messed up\" - Dr. Karam 03/07/2022", "\"watch out for hazards\" - Dr. Karam 03/07/2022", "\"If you're a bad designer, all bets are off\" - Dr. Karam 03/21/2022", "\"Sounds like it’s actually raining\" - Dr. Karam 03/24/2022", "\"This may have useful properties but I can't think of one right now\" - Dr. Karam 03/29/2022", "\"A lot of things in engineering are about just doing 'good enough\" - Dr. Karam 04/06/2022", "\"Why are going over this towards the end of the semester? This [functional programming] content had to be put in the program somewhere... and they chose Data Structures, so here we are, and I have to teach it to you\" - Dr. Beasley 04/14/2022", "\"I TOLD U IT WAS SUBTLE!\" - Dr. Beasley 05/26/2022", "\"So these may sound like gibberish, but I've got theseup here.. just because I think they're cool\" - Dr. Beasley 05/17/2022", "\"What's that company out in San Francisco... Yelp!\" - Dr. Beasley 05/19/2022", "\"Yeah, you probably won't see me sign this... I try and stay away from these Manifesto's myself\" - Dr. Beasley 05/24/2022", "\"Most of us have 10 fingers if you have more that's not normal\" - Dr. Rubel 05/31/2022", "\"Okay I think we have enough information about this subject.\" - Dr. Rubel 05/31/2022"]

Beasley=["\"Forget the Stack\" - Dr. Beasley 01/27/2022", "\"Imagine if we didn't hit a base case. Then your stack...would overflow\" - Dr. Beasley 01/27/2022", "\"Don't turn that into the TA's you won't get any points for that, you will just be making enemies\" - Dr. Beasley 02/09/2022", "\"3-1 is 2 which is greater than 1\" - Dr. Beasley 02/24/2022", "\"If I don't assign points to it, nobody is going to do it\" - Dr. Beasley 02/24/2022", "\"Will you be able to do this on the exam?\" - Dr. Beasley 03/03/2022", "\"I want to store their social security numbers\" - Dr. Beasley 03/08/2022", "\"Merge sort is like war\" - Dr. Beasley 03/24/2022", "That's a nice umbrella, might have to keep it\" - Dr. Beasley 03/24/2022", "\"No quicksort, mergesort, AVL trees on the exam... Oh wait hang on a second\" - Dr. Beasley 03/29/2022", "\"Chad gets mapped into slot 1 but there’s already someone there\" - Dr. Beasley 03/29/2022", "\"I increased the size of my vector\" - Dr. Beasley 04/05/2022", "\"This is not the D we were looking at\" - Dr. Beasley 04/07/2022", "\"It's a shame that this kind of content has to be in your Data Structures class...\" - Dr. Beasley 04/19/2022", "\"Anyone wanna draw their tree that way\" - Dr. Beasley 02/22/2022", "\"Why are going over this towards the end of the semester? This [functional programming] content had to be put in the program somewhere... and they chose Data Structures, so here we are, and I have to teach it to you\" - Dr. Beasley 04/14/2022", "\"I TOLD U IT WAS SUBTLE!\" - Dr. Beasley 05/26/2022", "\"So these may sound like gibberish, but I've got theseup here.. just because I think they're cool\" - Dr. Beasley 05/17/2022", "\"What's that company out in San Francisco... Yelp!\" - Dr. Beasley 05/19/2022", "\"Yeah, you probably won't see me sign this... I try and stay away from these Manifesto's myself\" - Dr. Beasley 05/24/2022"]

Theado=["\"You can share your P, but do not share your D\" - Dr. Theado 03/09/2022", "\"I am going to change it to my favorite color blue\" - Dr. Theado 03/09/2022", "\"Use your D to encrypt this\" - Dr. Theado 03/21/2022", "\"Here is an example no one cares about\" - Dr. Theado 04/04/2022", "\"Once we figure out where the balls go...\" - Dr. Theado 04/06/2022", "\"I am not making an easier exam, just learnthe concepts\" - Dr. Theado 04/20/2022", "\"When I was a kid, I had my favorite bowl I'd eat cereal out of. It was a blue plastic bowl. I just think blue is the best color\" - Dr. Theado 04/29/2022"]

Yalcin=["\"When I used to teach I would call on kids but now apparently that is taboo so I don't do it anymore instead I beg you guys to answer\" - Dr. Yalcin 04/27/2022", "\"Alright we need to end this\" - Dr. Yalcin 02/14/2022"]

Karam=["\"No one uses kmaps, in-fact, no one uses quine-mccluskey\" - Dr. Karam 02/07/2022", "\"Alright we need to end this\" - Dr. Yalcin 02/14/2022", "\"kmaps are fun and all, well actually no\" - Dr. Karam 02/15/2022", "\"I know there are not many fans of assembly here\" - Dr. Karam 02/24/2022", "\"I want ice-cream now\" - Dr. Karam 03/07/2022", "\"that kmap is messed up\" - Dr. Karam 03/07/2022", "\"watch out for hazards\" - Dr. Karam 03/07/2022", "\"If you're a bad designer, all bets are off\" - Dr. Karam 03/21/2022", "\"Sounds like it’s actually raining\" - Dr. Karam 03/24/2022", "\"This may have useful properties but I can't think of one right now\" - Dr. Karam 03/29/2022", "\"A lot of things in engineering are about just doing 'good enough\" - Dr. Karam 04/06/2022"]

Rubel=["\"Most of us have 10 fingers if you have more that's not normal\" - Dr. Rubel 05/31/2022", "\"Okay I think we have enough information about this subject.\" - Dr. Rubel 05/31/2022"]

profs=["$beasley", "$theado", "$yalcin", "$karam", "$rubel"]

@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if '$quote' in message.content.lower():
        quote = random.choice(quotes)
        await message.channel.send(quote)
        
    elif '$beasley' in message.content.lower() and not('$theado' in message.content.lower() or '$yalcin' in message.content.lower() or '$karam' in message.content.lower() or '$rubel' in message.content.lower()):
        Beasleys = random.choice(Beasley)
        await message.channel.send(Beasleys)
    
    elif '$theado' in message.content.lower() and not('$beasley' in message.content.lower() or '$theado' in message.content.lower() or '$yalcin' in message.content.lower() or '$karam' in message.content.lower() or '$rubel' in message.content.lower()):
        Theados = random.choice(Theado)
        await message.channel.send(Theados)
    
    elif '$yalcin' in message.content.lower() and not('$beasley' in message.content.lower() or '$theado' in message.content.lower() or '$karam' in message.content.lower() or '$rubel' in message.content.lower()):
        Yalcins = random.choice(Yalcin)
        await message.channel.send(Yalcins)
    
    elif '$karam' in message.content.lower() and not('$beasley' in message.content.lower() or '$theado' in message.content.lower() or '$yalcin' in message.content.lower() or '$rubel' in message.content.lower()):
        Karams = random.choice(Karam)
        await message.channel.send(Karams)
    
    elif '$rubel' in message.content.lower() and not('$beasley' in message.content.lower() or '$theado' in message.content.lower() or '$yalcin' in message.content.lower() or '$karam' in message.content.lower()):
        Rubels = random.choice(Rubel)
        await message.channel.send(Rubels)
    
    elif any(word in message.conetnet.lower() for word in profs):
         prof = random.choice(profs)
         if prof == '$beasley':
             quote = random.choice(Beasley)
             await message.channel.send(quote)
         elif prof == '$theado':
             quote = random.choice(Theado)
             await message.channel.send(quote)
         elif prof == '$yalcin':
             quote = random.choice(Yalcin)
             await message.channel.send(quote)
         elif prof == '$karam':
             quote = random.choice(Karam)
             await message.channel.send(quote)
         elif prof == '$rubel':
             quote = random.choice(Rubel)
             await message.channel.send(quote)

keep_alive()
client.run(os.getenv('TOKEN'))
