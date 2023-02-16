#first function
def emobilis():
    print("This is my First function")
emobilis()
#calc function
def calculatesquare():
    x=5
    y=6
    print(x*y)
calculatesquare()
#name function
def majina(fname,lname,age):
    print(fname+ lname+ age)
majina("Ken","Json","7")
#DoB function
def DoB(dd,mm,yyyy):
    print(dd+ mm+ yyyy)
DoB("03","01","2004")
#max function
def maximum(a,b,c,d,e):
    return max(a,b,c,d,e)
results=maximum(5,15,67,0,89)
print(results)
#min function
def minimum(e,d,c,b,a):
    return min(e,d,c,b,a)
results=minimum(5,15,67,0,89)
print(results)
#Range function
def print_numbers(nambari):
    for i in range(nambari):
        print(i)
print(10)