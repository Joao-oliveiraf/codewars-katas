# - Selection Sort
# - Se tiver 0 na array insert(0, 0)
# index  i = onde estava e index j = para onde foi
# Se 0 index = 1
def smallest(n: int):
    rt_arr = []
    n = str(n)
    n = [i for i in map(int, n)]
    # Transform int(n) into string and segregates the elements into a list
    # afterward, using map function, transform each element of the list to int, now segregated
    # (12345) -> [1, 2, 3, 4, 5]
    if n[1] == 0:
        # If zero is the 2nd number
        n.remove(0)
        n.insert(0, 0)
        rt_arr.append(int(''.join(map(str, n))))
        rt_arr.append(0)
        rt_arr.append(1)
        return rt_arr
    else:
        # If the first digit is the smallest
        if min(n) == n[0]:
            fst_smallest = min(n)
            n.remove(fst_smallest)
            scnd_smallest = min(n)
            scnd_index = n.index(min(n)) + 1
            n.remove(scnd_smallest)
            n.insert(0, fst_smallest)
            n.insert(1, scnd_smallest)
            rt_arr.append(int(''.join(map(str, n))))
            rt_arr.append(scnd_index)
            rt_arr.append(1)
            return rt_arr
        else:
            # Smallest number is somewhere else in the array
            smallest_number = min(n)
            smallest_number_index = n.index(smallest_number)
            n.remove(smallest_number)
            n.insert(0, smallest_number)
            rt_arr.append(int(''.join(map(str, n))))
            rt_arr.append(smallest_number_index)
            rt_arr.append(0)
            return rt_arr
[395855753, 1, 0] should equal [358557539, 0, 8]

print(smallest(209917))
print(smallest(285365))
print(smallest(296837))
