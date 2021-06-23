
def getLetters(ruleNum, dictionary):
    letters = ''
    for i in ruleNum.split(" "):
        print(i, "===<<<")
        # while i.isdigit():
            # print(letters, i)
        if dictionary[i] == 'a':
            letters = letters + 'a'
        elif dictionary[i] == 'b':
            dictionary[i] + 'b'
        if not dictionary[i].isdigit():
            newRule = dictionary[i].split(" | ")
            # print(newRule)
            ruleNum = newRule
        else: 
            i = dictionary[i]
    return letters

def messageCheck(message, ruleD):
    if message[0].isdigit():
        return False
    #i have the message and rules , what now????
    #all i have to make sure is that rule 0 works for the message and then return true
    print("MESSAGE", message)
    rule_zero = ruleD["0"]
    cleanArray = rule_zero.split(" ")
    for i in cleanArray:
        letters = getLetters(i, ruleD)
        print(letters, "<==")
        if letters not in message:
            return False
    return True

with open('test.txt') as raw_input:
    #part one is build a dictionary of rules
    rules_dict = {}
    for i in raw_input:
        if i[0].isdigit():
            #add to dictionary
            keyAndVal = i.split(': ')
            if "a" in keyAndVal[1]:
                rules_dict[keyAndVal[0]] = 'a'
            elif "b" in keyAndVal[1]:
                rules_dict[keyAndVal[0]] = 'b'
            else:
                rules_dict[keyAndVal[0]] = keyAndVal[1].replace("\n", "")
        else:
            break
    print(rules_dict)
    #count how many messages fit our rules
    messagesPassed = 0
    for j in raw_input:
        if messageCheck(j, rules_dict):
            messagesPassed += 1
    print(messagesPassed)


