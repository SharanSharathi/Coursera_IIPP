# List reference problem

###################################################
# Student should enter code below

a = [5, 3, 1, -1, -3, 5]
b = list(a)

b[0] = 0
print(a)
print(b)

###################################################
# Explanation
#
#when we use list fumction it only copies the list and not the refernce of memory address
#so when we update the value of b[0] it will not updte a[0]