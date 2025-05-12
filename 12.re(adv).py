import re

s ="The Rain In Spain"
while True:
    ch = int(input("Choice"))
    if ch == 1:
        x = re.findall("[a-m]",s)
        print(x)
    elif ch == 2:
        x = re.search('Rain',s)
        print (x)
    elif ch == 3:
        x = re.split(r"\s",s)
        print(x)
    elif ch == 4:
        x = re.sub(r"\s", "9",s)
        print(x)
    elif ch == 5:
        break
    
        