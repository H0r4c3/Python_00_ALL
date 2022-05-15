def number_2_word(n):
    digits_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
 
    if n==0:
        return ""
     
    else:
        # compute spelling for the last digit
        units = digits_list[n % 10]
 
        # keep computing for the previous digits and add the spelling for the last digit
        words = number_2_word(int(n/10)) + units + " "
     
    return words

# print(number_2_word(123))

# https://stackoverflow.com/questions/19504350/how-to-convert-numbers-to-words-without-using-num2word-library

def convert(num):
    units = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens = ("", "", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    if num < 0:
        return "minus "+ convert(-num)

    if num < 20:
        return  units[num] 

    if num < 100:

        return  tens[num // 10]  + units[int(num % 10)] 

    if num < 1000:
        return units[num // 100]  + "hundred " + convert(int(num % 100))

    if num < 1000000: 
        return  convert(num // 1000) + "thousand " + convert(int(num % 1000))

    if num < 1000000000:    
        return convert(num // 1000000) + "million " + convert(int(num % 1000000))

    return convert(num // 1000000000) + "billion " + convert(int(num % 1000000000))


print(convert(1234))