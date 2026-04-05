nums = [2, 7, 11, 15]
target = 9;

def twoSum(arr, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if(arr[i] + arr[j] == target) :
                return [i, j]
            

print(twoSum(nums, target))