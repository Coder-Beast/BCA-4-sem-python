import math
a,b,c = 1,-5,6

if a==0:
    print("not valid")
else:
    disc = b*b - 4*a*c
    sv = math.sqrt(abs(disc))

    if disc > 0:
        r1 = (-b+sv)/(2*a)
        r2 = (-b-sv)/(2*a)
        print("Real and distinct roots\n", r1,r2)
    elif disc == 0:
        print("Real And Equal Roots:", (-b/(2*a)))
    else:
        print("Real And Equal Roots:")
        print(-b/(2*a), "+j", sv)
        print(-b/(2*a), "-j", sv)