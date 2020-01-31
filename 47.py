def qq(A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
           
            maxSum = max(maxSum, curSum)

        return maxSum
a=[-2,-3,4,-1,-2,1,5,-3]
print(qq(a))
