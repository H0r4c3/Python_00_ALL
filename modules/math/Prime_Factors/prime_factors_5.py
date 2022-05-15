'https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python'

numb=int(input("enter any number"))

facts=[]

for a in range(1,numb+1):

    if numb%a==0:

       facts.append(a)

print ("Factors of {} = {}".format(numb,facts))

