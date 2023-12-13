# 04/20/2022

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


from ast import Num


ONES = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
TENS = {0:'',1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'} # for 1Xs use -teen exception
TEENS = {11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
HUNDREDS = {} # add "hundred and" to ones
THOUSANDS = {} # add thousand to ones

Numbers = list()
limit = 1000
totalLetters = 0

for n in range(1,limit+1):
    if len(str(n)) == 1:
        Numbers.append(ONES[n])
    elif len(str(n)) == 2:
        if 10 < n and n < 20:
            Numbers.append(TEENS[n])
        else:
            temp = ''
            nString = str(n)
            temp += TENS[int(nString[0])]
            temp += ONES[int(nString[1])]
            Numbers.append(temp)
    elif len(str(n)) == 3:
        ten = str(n)[-2:]
        hund = int(str(n)[0])
        temp = ''
        if int(ten) == 0:
            temp += ONES[hund] + "hundred"
        else: 
            temp += ONES[hund] + "hundredand"
        if 10 < int(ten) and int(ten) < 20:
            temp+=TEENS[int(ten)]
        else:
            nString = str(ten)
            temp += TENS[int(nString[0])]
            temp += ONES[int(nString[1])]
        Numbers.append(temp)
    else:  
        Numbers.append("ONETHOUSAND")

for n in Numbers:
    print(n)
    totalLetters += len(n)

print(totalLetters)

# 21124