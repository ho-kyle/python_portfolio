from random import randint
suit = ["♠️", "♥️", "♦️", "♣️"]
order = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = []
for i in suit:
    for j in order:
        deck.append(i + j)
c = []
for i in range(5):
    c.append(deck.pop(randint(0, len(deck) - 1)))
print(c)