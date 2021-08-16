#Enoch Leow 30600022

def counting_sort(list, max):
    length = max + 1
    count = length * [0]

    for i in list:
        count[i] += 1
    print(count)

    sorted = []
    for j in range(length):
        print(j)
        print(count[j])
        if count[j] != 0:
            for repeats in range(count[j]):
                sorted.append(j)

    return sorted


def radix_sort(list, base):
