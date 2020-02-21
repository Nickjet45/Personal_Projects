import random


text = input('What to say? ')

troll = []
def Tweet_Troll(text):
    for char in text:
        r = random.randint(0, 1)
        if r == 1:
            troll.append(char.upper())
        else:
            troll.append(char.lower())
    return ''.join(troll) + ' oK bOoMeR'


print(Tweet_Troll(text))