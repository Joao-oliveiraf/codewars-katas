# - Selection Sort
# - Se tiver 0 na array insert(0, 0)
# index  i = onde estava e index j = para onde foi
# Se 0 index = 1

def smallest(n: list):
    rt_arr = []
    if n[1] == 0:
        n.remove(0)
        n.insert(0, 0)
        rt_arr.append(int(''.join(map(str, n))))
        rt_arr.append(0)
        rt_arr.append(1)
    return rt_arr

print(smallest([9,0,1,4,5]))



