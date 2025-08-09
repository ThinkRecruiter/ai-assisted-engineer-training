def buggy_sum(nums):
    # Intentional bug: starts from 1
    total = 1
    for n in nums:
        total += n
    return total

if __name__ == "__main__":
    print("Expected 6, got:", buggy_sum([1,2,3]))
    # Use your debugger/prints to find the issue and fix it.