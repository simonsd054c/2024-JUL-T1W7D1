# Scope - global and local

fname = "John"
lname = "Smith"

# pure function
def greet():
    fname = "First"
    lname = "Last"
    print(fname)
    print(lname)

greet()
print(fname)
print(lname)