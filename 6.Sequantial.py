def search (arr,x):
    l = len(arr)

    for i in range(l):
        if(arr[i] == x):
            return i
    return -1

arr = [2, 3, 4, 10, 40]
x = 1

res = search(arr,x)
if res == -1:
    print("Element not present in array")
else:
    print(f"Element is present in {res} index ")