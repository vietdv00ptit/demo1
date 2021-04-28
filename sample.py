def findnear(a, b):
    vmin = a[b] - a[b - 1]
    imin = b
    for i in range(b + 1, len(a)):
        if a[i] - a[b - 1] > 0 and a[i] - a[b - 1] < vmin:
            vmin = a[i] - a[b - 1]
            imin = i
    return imin
def fl(a, i):
    m = findnear(a, i)
    tmp = a[i - 1]
    a[i - 1] = a[m]
    a[m] = tmp
    a[i:].sort()
    aa = a[i:]
    aa.sort()
    a = a[:i] + aa
    return a
def stringsRearrangement(inputArray):
    ax = [[]]
    i = len(inputArray) - 1
    a = []
    for j in range(0, i + 1):
        a.append(j)
        ax[0].append(j)

    while i > 0:
        a = ax[len(ax) - 1].copy()
        if a[i] > a[i - 1]:

            ax.append(fl(a,i))
            i = len(a)
        i -= 1
    for i in range(0, len(ax)):
        count = 0
        print(i,'------------------',ax[i])
        for j in range(1, len(ax[i])):
            count = 0
            for k in range(0, len(inputArray[0])):
                if inputArray[ax[i][j]][k] != inputArray[ax[i][j-1]][k]:
                    count += 1
            print(inputArray[ax[i][j]],inputArray[ax[i][j-1]],count)
            if count!=1:
                 break

        if count < 2:
            return True
    return False
print(stringsRearrangement(["abc", "bef", "bcc", "bec", "bbc", "bdc"]))

