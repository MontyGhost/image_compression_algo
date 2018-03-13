from compress import display, compress, extract

def read_image(filename, splt=False):
    with open(filename, 'r') as f:
        data = f.readlines()
    if splt:
        return [map(int, list(i.strip())) for i in data]
    else:
        return [int(i) for i in data]

if __name__ == "__main__":

    data = []
    filename = "7.txt"
    data = read_image("images/" + filename, True)

    print data
    # display(data)
    compress(data, filename)

    data = read_image("compress/cmp_" + filename)
    print data
