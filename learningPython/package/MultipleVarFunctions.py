# edit the functions prototype and implementation
def foo(a, b, *c):
    if len(list(c)) > 0:
        return (len(list(c))-1)
    else:
        return 0
def bar(a, b, bb, **c):
    return c["magicnumber"] == 7


# test code
if foo(1,2,3,4) == 1:
    print "Good."
if foo(1,2,3,4,5) == 2:
    print "Better."
if bar(1,2,3,magicnumber = 6) == False:
   print "Great."
if bar(1,2,3,magicnumber = 7) == True:
    print "Awesome!"