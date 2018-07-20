# Vector addition function

###################################################
# Student should enter code below
def add_vector(a,b):
    a[0] = a[0] + b[0]
    a[1] = a[1] + b[1]
    return (a)

###################################################
# Test

print add_vector([4, 3], [0, 0])
print add_vector([1, 2], [3, 4])
print add_vector([2, 3], [-6, -3])



###################################################
# Output

#[4, 3]
#[4, 6]
#[-4, 0]

