def stats(nums):
    small = nums[0]
    large = nums[0]
    total = 0
    
    for n in nums:
        if n < small:
            small = n
        if n > large:
            large = n
        total += n
        
    avg = total / len(nums)
    return (small, large, avg)

nums_list = [int(x) for x in input("Enter integers: ").split()]
result_tuple = stats(nums_list)
print(result_tuple)