# List reference problem

###################################################
# Student should enter code below

a = [5, 3, 1, -1, -3, 5]
print("a: "+str(a))
b = a
b[0] = 0
print("a: "+str(a))
print("b: "+str(b))

###################################################
# Explanation
"""
the list b has the same memory adress of a,
so, if we change the value of b, a value also change.
"""