'''
Problem from Lab 1 at MCTC.
Program that turns a sentence into camel case.
The first word is lowercase, the rest of the words have their initial letter capitalized,
and all of the words are joined together.
'''
# camelCase = "fOnt proCESSOR and ParsER"
def convertToCamelCase(camelCaseSentence):
    splitCamelCase = camelCaseSentence.lower().title().split()
    # This line will convert everything to lower and capitalized the first letter or each.
    counter = 0
    # This counter is for the forloop to get the first word.
    lowerCamelCase = []
    # List to append the first word in lower case only.
    for x in splitCamelCase:
        if counter == 0:
            lowerCamelCase.append(x.lower())
            # This assures that the first word gets changed to lower.
        else:
            lowerCamelCase.append(x)
            # everything else is then append normal.
        counter += 1
        # Just to make sure that it is incremented.
    # print(lowerCamelCase)
    # print an example.
    backToString = "".join(lowerCamelCase)
    # This will join the words.
    print(backToString)

userInput = str(input("Enter a sentence and I will camelCase it:\n").lstrip())
# Enter a sentence but if it doesn't starts with a letter it will ask the user to re type.
# The str.lstrip() works realy good in this way.
while True:
    if userInput[0].isalpha(): # The first char must start with alpha, space is not a problem.
        break
    else:
        userInput = str(input("Enter a sentence and I will camelCase it.\
        \nMake sure the sentence starts with a letter: \n").lstrip())
        continue

convertToCamelCase(userInput)
