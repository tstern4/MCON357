# This program will replace digits with words

# Receive user's input
string = input("Please enter your phrase that contains a number:")

# Split the string into a list wherever there is a space
words = string.split()

# Loop through the length of the string to see if it contains any digits
for i in range(len(words)):
    word = words[i]
    # if the word is a digit, convert it to a word number
    if word.isdigit():
        if word == '0':
            word = 'zero'
        elif word == '1':
            word = 'one'
        elif word == '2':
            word = 'two'
        elif word == '3':
            word = 'three'
        elif word == '4':
            word = 'four'
        elif word == '5':
            word = 'five'
        elif word == '6':
            word = 'six'
        elif word == '7':
            word = 'seven'
        elif word == '8':
            word = 'eight'
        elif word == '9':
            word = 'nine'
        elif word == '10':
            word = 'ten'
        elif word == '11':
            word = 'eleven'
        elif word == '12':
            word = 'twelve'
        elif word == '13':
            word = 'thirteen'
        elif word == '14':
            word = 'fourteen'
        elif word == '15':
            word = 'fifteen'
        elif word == '16':
            word = 'sixteen'
        elif word == '17':
            word = 'seventeen'
        elif word == '18':
            word = 'eighteen'
        elif word == '19':
            word ='nineteen'
        # If it is none of the above numbers, use the two digit number formula
        else:
            firstDigit = word[0]
            secondDigit = word[1]
            if firstDigit == '2':
                word = 'twenty'
            elif firstDigit == '3':
                word = 'thirty'
            elif firstDigit == '4':
                word = 'forty'
            elif firstDigit == '5':
                word = 'fifty'
            elif firstDigit == '6':
                word = 'sixty'
            elif firstDigit == '7':
                word = 'seventy'
            elif firstDigit == '8':
                word = 'eighty'
            elif firstDigit == '9':
                word = 'ninety'
            if secondDigit == '1':
                word += ' one'
            elif secondDigit == '2':
                word += ' two'
            elif secondDigit == '3':
                word += ' three'
            elif secondDigit == '4':
                word += ' four'
            elif secondDigit == '5':
                word += ' five'
            elif secondDigit == '6':
                word += ' six'
            elif secondDigit == '7':
                word += ' seven'
            elif secondDigit == '8':
                word += ' eight'
            elif secondDigit == '9':
                word += ' nine'
                
        words[i] = word

# Print the modified phrase
for word in words:
    print(word, end = ' ')
       