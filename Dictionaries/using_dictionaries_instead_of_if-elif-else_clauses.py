'https://blog.tplus1.com/blog/2007/06/24/using-dictionaries-rather-than-complex-if-elif-else-clauses/'

'Lately, I’ve been using dictionaries as a dispatching mechanism. It seems especially elegant when I face some fairly elaborate switching logic.'

#For example, instead of:
if a == 1 and b == 1:
    log("everything worked!")
    commit()


elif a == 1 and b == 0:
    log("a good, b bad")
    report_that_b_failed()


else:
    log("a failed")
    report_that_a_failed()

#Do this:


d = {
(1, 1): commit,
(1, 0): report_that_b_failed,
(0, 0): report_that_a_failed
}


k = (a, b)
f = d[k]
f()

'''This approach is also really useful when you face the need to change logic based on runtime values. 
You can imagine that d might be built after parsing an XML file.
'''