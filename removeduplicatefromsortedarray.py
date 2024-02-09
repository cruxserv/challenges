def removeDuplicates(nums):
    if not nums:
        return 0
    
    # Initialize the counter at the first element.
    i = 0
    
    # Start the loop from the second element.
    for j in range(1, len(nums)):
        # Only if we find a new element (not a duplicate)
        if nums[j] != nums[i]:
            # Increment the counter.
            i += 1
            # Only perform the assignment if it's needed.
            if i != j:
                nums[i] = nums[j]
                
    # The length of the unique elements is i + 1.
    return i + 1
