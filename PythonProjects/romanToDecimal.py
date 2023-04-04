roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # specify more numerals if you wish
}

def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if roman[left] < roman[right]:
            sum -= roman[left]
        else:
            sum += roman[left]
    sum += roman[romanNumeral[-1]]
    return sum

a= input("Enter the number required to be changed to decimal: ")
print(RomanNumeralToDecimal(a))