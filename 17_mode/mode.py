def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    number_count = {}

    for num in nums:
        number_count[num] = number_count.get(num, 0) + 1

    max_value = max(number_count.values())

    for key in number_count:
        if max_value == number_count[key]:
            return key
        




