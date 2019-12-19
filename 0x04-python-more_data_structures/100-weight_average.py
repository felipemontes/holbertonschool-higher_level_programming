#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = 0
    wg = 0
    lists = [[first*second for first, second in
              zip(elem, elem[1:])] for elem in my_list]
    second = [[n2 for n2 in zip(nums[1:])] for nums in my_list]

    for elem in lists:
        for nums in elem:
            res += nums
    for li in second:
        for tup in li:
            for i in tup:
                wg += i

    return res / wg
