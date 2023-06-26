arr = [7, 10, 4, 10, 6, 5, 2]
n = len(arr)

max_val = arr[n - 1] 
leaders = [max_val]  

for i in range(n - 2, -1, -1):
    if arr[i] > max_val:
        leaders.append(arr[i])
        max_val = arr[i]

leaders.reverse() 

print("Leaders : ", end=" ")
for leader in leaders:
    print(leader, end=" ")