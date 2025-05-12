try:
    x = 12/0
    print(x)
except ValueError:
    print("Invalid DT")
except ZeroDivisionError:
    print("cantr be devided by zero")
except Exception as e:
    print(e)
finally:
    print("yeahhhh")