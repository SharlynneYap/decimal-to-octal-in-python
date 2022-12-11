# input and other variables
decNum = int(input("Enter a decimal integer: "))
remainder = 0
octNum = ''

print("Quotient Remainder Octal")
while decNum != 0:
    remainder = decNum % 8
    decNum //= 8
    octNum = str(remainder) + octNum
    print("%5d%8d%12s" % (decNum, remainder, octNum))

print("The octal representation is", octNum)
