
# Max Contiguous Subarray Sum - Cubic Time To Kadane's Algorithm ("Maximum Subarray" on LeetCode)

# can it has duplicate? y

A = [-2, 1, -3, 4, -1, 2, 4, -5, 2]
maxSum = A

for i in range(1, len(A)):
    maxSum[i] = max(A[i], A[i] + maxSum[i - 1])

print (maxSum)
s=sorted(maxSum)
print(s[-1])



