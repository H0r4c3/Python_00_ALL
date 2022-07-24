'https://compucademy.net/recursion-in-python-programming/'

def countdown(n):
  if n <= 0:
    print("LIFTOFF!")
  else:
    print(n)
    countdown(n - 1)



countdown(10)
