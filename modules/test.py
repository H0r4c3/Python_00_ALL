
def sumOrProduct(N, Q):

    # Write your Code here.
	if Q == 1:
		return sum(list(range(N+1)))
	elif Q == 2:
		number = 1
		for i in range((N+1)):
			number *= i
		return number
  
print(sumOrProduct(4, 1))