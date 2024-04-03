def avgSumOfSubArrOfK(k:int,arr:list)->list:
    result = [0.0] * (len(arr) - k + 1)
    for i in range(len(arr)-k+1):
        sum = 0
        for j in range(i,i+k):
            sum += arr[j]
        result[i] = sum/k
    return result

def findAverages(K, arr):
        result = [0.0] * (len(arr) - K + 1)
        for i in range(len(arr) - K + 1):
            # Find sum of next 'K' elements
            summation = 0
            for j in range(i, i + K):
                summation += arr[j]
            result[i] = summation / K  # Calculate average
        return result

li = [1,3,2,6,-1,4,1,8,2]
# print(findAverages(5,li))
print(avgSumOfSubArrOfK(5,li))
            