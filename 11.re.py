import re

s ="The Rain In Spain.32"
while True:
    ch = int(input("Choice"))
    if ch == 1:
        x = re.findall("^The",s)
        print(x)
    elif ch == 2:
        x = re.findall('32$',s)
        print (x)
    elif ch == 3:
        x = re.findall("ain*",s)
        print(x)
    elif ch == 4:
        x = re.findall(r"\d",s)
        print(x)
    elif ch == 5:
        break
    
        