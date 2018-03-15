from compress import display, compress, extract

def read_image(filename, splt=False):
    with open(filename, 'r') as f:
        data = f.readlines()
    if splt:
        return [map(int, list(i.strip())) for i in data]
    else:
        return [map(int, i.split()) for i in data[2:]], int(data[1]), int(data[0])

if __name__ == "__main__":

    data = []
    filename = "7.txt"

    data = read_image("images/" + filename, True)
    display(data)

    compress(data, filename)

    data, med, size = read_image("compress/cmp_" + filename)
    # print data, med, size
    data = extract(data, filename, med, size)
    # print data
    display(data)
