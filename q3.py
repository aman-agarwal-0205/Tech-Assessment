def XORSum(nums):
    def generateSubsets(index, current_xor):
        nonlocal total_xor
        if index == len(nums):
            total_xor += current_xor
            return
        generateSubsets(index + 1, current_xor ^ nums[index])
        generateSubsets(index + 1, current_xor)

    total_xor = 0
    generateSubsets(0, 0)
    return total_xor

nums = [1, 3]
print("Sum of XOR totals in case 1 : ", XORSum(nums))  

nums = [5, 1, 6]
print("Sum of XOR totals in case 2 : ", XORSum(nums))  