# Sample array to be sorted
arr = [-5, -10, 0, -3, 8, 5, -1, 10] 

minEl = min(arr)

# Finding range of elements, needed for setting 0 index
rangeOfElements = max(arr) - minEl + 1

# Setting up the output and count arrays
output = [0 for i in range(len(arr))]
count = [0 for i in range(rangeOfElements)]

# Setting up the counts for each elements
for x in arr:
    count[x - minEl]+=1

# Incrementing counts based on count of previous element
for i in range(1,rangeOfElements):
    count[i] += count[i-1]

# Set up output array based on counts
for i in range(len(arr)):
    output[count[arr[i] - minEl]-1]=arr[i]
    count[arr[i]-minEl]-=1

print("Original Array: ",end='')
print(arr)
print("Sorted Array: ",end='')
print(output)

