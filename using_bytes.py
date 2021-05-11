# handling byte files
b = bytes( range(0, 256) ) # start at 0 stop before 256
# \x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b...
print(b)
fout = open('bfile', 'wb') # 'wb' to (over)write bytes
fout.write(b)
fout.close()

# read them back
fin = open('bfile', 'rb')
retrieved_b = fin.read()
fin.close()
print(retrieved_b)

# we really should be using try-except when handling files
try:
    fout = open('bfile', 'xb') # 'x' for exclusive - fails if the file already exists
    size = len(b)
    offset=0
    chunk=24
    #loop over the bytes, writing a chunk at a time
    while True:
        if offset > size:
            break
        else:
            fout.write(b[offset:offset+chunk])
            offset += chunk
except FileExistsError as err:
    print('the file already exists', err.errno)
except Exception as err:
    print('Some other exception occured', err)
finally:
    print('this block runs whether or not we had an exception')