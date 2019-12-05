# -*- coding: utf-8 -*-
import random

namelistMale = ["Oskar ", "Henry ", "Linus ", "Mark ", "Tobias ", "Benedikt ", "Killian ", "Nicklas "]
namelistFemale = ["Uma ", "Jocelyn ", "Rosely ", "Hester ", "Letica "]
accusationMaleFemale = ["hatte ein Kafal mit ", "liebt ", "mag ", "küsste "]
accusation = ["raucht", "trinkt", "ist ausgestiegen"]
oneGuyToBlame = namelistMale + namelistFemale

coin = (1, 2)
randomizer = random.choice(coin)
order = random.choice(coin)

OneOne = (random.choice(namelistMale) + random.choice(accusationMaleFemale) + random.choice(namelistFemale))
OneTwo = (random.choice(namelistFemale) + random.choice(accusationMaleFemale) + random.choice(namelistMale))
Two = (random.choice(oneGuyToBlame) + random.choice(accusation))

if randomizer == 1:

    #Two people
    if order == 1:
        print(OneOne)
        
    elif order == 2:
        print(OneTwo)

    
elif randomizer == 2:
    print(Two)


