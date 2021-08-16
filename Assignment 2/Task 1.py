"""Task 1 - Oscillations"""


def longest_oscillation(L):
    maxlen = [0] * len(L)
    maxlen[0] = (1, 1)

    for i in range(1, len(L)):
        smallmax = 0
        largemax = 0
        for j in range(0, i):

            if L[i] < L[j]:
                temp = maxlen[j][1] + 1
                if temp > smallmax:
                    smallmax = temp
                if maxlen[j][1] > largemax:
                    largemax = maxlen[j][1]

            if L[i] > L[j]:
                temp = maxlen[j][0] + 1
                if temp > largemax:
                    largemax = temp
                if maxlen[j][0] > smallmax:
                    smallmax = maxlen[j][0]

            else:
                if maxlen[j][1] > largemax:
                    largemax = maxlen[j][1]
                if maxlen[j][0] > smallmax:
                    smallmax = maxlen[j][0]

        maxlen[i] = (smallmax, largemax)

    long_osc = []
    count = 0
    exclude = 0

    for i in range(len(maxlen)-1):
        if max(maxlen[i][0], maxlen[i][1]) == (max(maxlen[i+1][0], maxlen[i+1][1])-1):
            long_osc.append(i)
            count += 1
            exclude = 0

        elif L[i] == L[1+1]:
            if exclude == 0:
                long_osc.append(i)
                count += 1
                exclude = 1

        elif i == len(maxlen) - 2:
            long_osc.append(i)
            count += 1
            exclude = 1
        else:
            exclude = 1

    if exclude == 0:
        long_osc.append(len(maxlen)-1)
        count += 1

    return count, long_osc



