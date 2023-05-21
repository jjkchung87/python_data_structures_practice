def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """

    # total = 0

    # if start is not None:
    #     if end is not None:
    #         new_nums = nums[start:end+1]
    #         for num in new_nums:
    #             total += num
    #         return total
    #     elif end is None:
    #         new_nums = nums[start:]
    #         for num in new_nums:
    #             total += num
    #         return total
    
    # elif start is None:
    #     if end is not None:
    #         new_nums = nums[:end+1]
    #         for num in new_nums:
    #             total += num
    #         return total
    #     if end is None:
    #         for num in nums:
    #             total += num
    #         return total

    if end is None:
        end = len(nums)

    return sum(nums[start:end + 1])



