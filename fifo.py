# file input and file output (fifo)
# every persistent file is just a bunch of data
# we can choose to encode as plain text or as bytes (or others too)
# it all work via file access objects
def main():
    # 'at' to append text (the default) 'wt' will (over)write 'xt' for exclusive write
    fout = open('out.txt', 'at') # 't' is default output
    # we can switch the context of the print statement by specifying a file
    print('here is some text', file=fout) # direct the print to our file access object
    fout.close()

def my_read():
    # we need a file access object
    fin = open('out.txt', 'r') # 'rt' to read text (default)
    received = fin.read() # read the entire content of the file via the file access object
    fin.close()
    print(received)


if __name__ == '__main__':
    main()
    my_read()