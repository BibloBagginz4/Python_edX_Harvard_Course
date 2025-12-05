import random

random_number_list = []
coin_flip_list = []
coin_flip_dict = {}
x = 100

for i in range(0, x):
    n = random.randint(1, 10)
    random_number_list.append(n)
    c = random.choice(["heads", "tails"])
    coin_flip_list.append(c)
    coin_flip_dict[c] = coin_flip_dict.get(c, 0) + 1


print(f"Length of random_number_list: ", len(random_number_list))
print(f"Length of coin_flip_list: ", len(coin_flip_list))
print(f"coin_flip_dict: ", coin_flip_dict)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

print(cards)