import matplotlib.pyplot as plt
from numpy import median

def display(data):

    plt.imshow(data, cmap='binary')
    plt.title("Image")
    plt.show()

def compress(data, filename):

    cmp = []
    for each in data:
        lst = map(str, each)
        cmp.append(int(''.join(lst), 2))

    med = int(median(cmp))
    cmp = [[i//med, i%med] for i in cmp]

    f = open("compress/cmp_" + filename, 'w')
    f.write("%s\n" % str(med))
    for item in cmp:
        f.write("%s\n" % (str(item[0]) + " " + str(item[1])))
    f.close()

def extract(data, filename, med):

    lst = []
    for i in data:
        val = (med*i[0]) + i[1]
        lst.append(med*i[0] + i[1])
    return lst
