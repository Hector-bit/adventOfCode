def getLetters(message, rule, d):
    #takes message and reduces it, if a rule works
    builder = []
    multi_rules = d[rule].split("|")
    print("=======", multi_rules, "===========")
    if d[rule].isdigit():
        getLetters(message,rule,d[rule])
    #if we are done searching through rules and get letters then
    for i in d[rule]:
        builder.append(i)
    print(builder)

def messageCheck(message, ruleD):
    if message[0].isdigit():
        return False
    #i have the message and rules , what now????
    #all i have to make sure is that rule 0 works for the message and then return true
    rule_zero = ruleD["0"]
    cleanArray = rule_zero.split(" ")
    for i in cleanArray:
        #returns shorter array
        getLetters(message, i, ruleD)
    if len(message) == 0:
        return True

with open('test.txt') as raw_input:
    #part one is build a dictionary of rules
    rules_dict = {}
    for i in raw_input:
        if i[0].isdigit():
            #add to dictionary
            keyAndVal = i.split(': ')
            rules_dict[keyAndVal[0]] = keyAndVal[1].replace("\n", "")
        else:
            break
    #count how many messages fit our rules
    messagesPassed = 0
    for j in raw_input:
        if messageCheck(j, rules_dict):
            messagesPassed += 1
    print(messagesPassed)


