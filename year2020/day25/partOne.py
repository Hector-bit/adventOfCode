# so with this question I have no idea what im suppose to do
# do I try different encryption methods until one words???
# even the question doesn't give an answer it just says "trial&error"

testCardPK = 5764801
testDoorPK = 17807724

# i have to figure out how to get loop size 8 from cardpk
# then loop size 11 for doorpk

subjectNumber = 7


value = 1
subject = 1004920
card = 5764801
door = 17807724

one = 10441485
two = 1004920

card_loop = 1
while pow(7, card_loop, 20201227) != one:
    card_loop += 1
print(card_loop)

door_loop = 1
while pow(7, door_loop, 20201227) != two:
    door_loop += 1
print(door_loop)

print('nothing', value)
