# finding the maximum element in a finit sequence
def procedure_01(*ints):
    m = ints[0]
    for i in range(1, len(ints)):
        a = ints[i]
        if m < a:
            m = a

    return m

def procedure_02(x, *ints):
    n = len(ints)
    i = 0
    while ((i <= n )and (x != ints[i])):
        i += 1
    if i <= n:
        loc = i
    else:
        loc = 0
    return loc
