from compress import display, compress, extract
import os

def read_image(filename, splt=False):
    with open(filename, 'r') as f:
        data = f.readlines()
    if splt:
        return [map(int, list(i.strip())) for i in data]
    else:
        return [map(int, i.split()) for i in data[2:]], int(data[1]), int(data[0])

if __name__ == "__main__":

    data = []
    filename = "batman.txt"

    data = read_image("images/" + filename, True)
    # print data
    display(data)

    compress(data, filename)

    data, med, size = read_image("compress/cmp_" + filename)
    # print data, med, size
    data = extract(data, filename, med, size)
    # print data
    display(data)

    original_size = os.path.getsize("images/" + str(filename))
    compressed_size = os.path.getsize("compress/cmp_" + str(filename))
    print "File size"
    print "Original Size : ", original_size
    print "Compressed Size : ", compressed_size
    print "Compression factor : ", float(original_size)/compressed_size
