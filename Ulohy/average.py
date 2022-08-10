def streamAvg(arr, n):
    avg = 0
    for i in range(n):
        avg = (avg * i + arr[i]) / (i + 1)
        print("Average of "+ str(i + 1)+" numbers is ", avg)

# Driver Code
arr = [10, 20, 30,
       40, 50, 60]
n = len(arr)
streamAvg(arr, n)
