'Function that converts a number from decimal to binary using recursion'

# Solution 1
def convert(decimal_num):
    # Base case: if the decimal number is 0, the binary representation is also 0
    if decimal_num == 0:
        return "0"
    # Base case: if the decimal number is 1, the binary representation is 1
    elif decimal_num == 1:
        return "1"
    else:
        # Recursive case: convert the quotient to binary and concatenate the remainder
        return convert(decimal_num // 2) + str(decimal_num % 2)

# Example usage:
decimal_number = 10
print(f"The binary representation of {decimal_number} is: {convert(decimal_number)}")




# Solution 2

def convert(num): 
   if num == 0:
      return 0
   elif num == 1:
      return 1
   else:
      return (num % 2 + 10 * convert(num // 2)) 

num = 10
print(convert(num))