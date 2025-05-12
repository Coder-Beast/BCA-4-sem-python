def selecition(arr):
    l = len(arr)
    for i in range(l):
        mini = i
        for j in range(i+1,l):
            if arr[j] < arr[mini]:
                mini = j
        arr[i],arr[mini] =arr[mini], arr[i]

ar =[2 ,445,43,22,1,5,9]
selecition(ar)
print('sorted array:', ar)
