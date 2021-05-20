f = open("day2/info.txt", "r")
# entries = set(f.read().split( ))
# print(f.readline())
# print(f.readline())
# print(f.readline())
valid_passwords = 0

for i in range(1000):
    curr_line = f.readline()
    curr_line = curr_line.split()
    temp = curr_line[0].split("-")
    max = temp[1]
    min = temp[0]
    letter = curr_line[1][0]
    # count = 0
    # print(letter)
    # for j in curr_line[2]:
    #     if j == letter:
    #         count = count + 1
    print('max: ', max, "min: ", min, "string: ", curr_line[2])
    if( (letter == curr_line[2][int(min) - 1]) != (letter == curr_line[2][int(max) - 1])):
        valid_passwords = valid_passwords + 1
print(valid_passwords)

f.close()