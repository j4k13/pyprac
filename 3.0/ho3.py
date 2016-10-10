#Highest of Three
a , b , c = 30 , 2 , 20
if a > b:
    print ("a is bigger than b")
    if c > a:
        print ("c is bigger than a")
        if c > b:
            print ("c is bigger than b")
            print ("c is biggest of the three")
        elif b > c:
            print ("b is bigger than c")
            print ("b is biggest of the three")
    elif a > c:
        print ("a is bigger than c")
        print ("a is biggest of the three")
elif b > c:
    print ("b is bigger than c")
    print ("b is biggest of the three")
