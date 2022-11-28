# generate files of size 1 megabyte each

import os

DEFAULT_NUMBER_OF_FILES = 1000

K, M, G = 1024, 1024, 1024

# 1 megabyte
DEFAULT_MAXIMUM_FILE_SIZE = 1 * K * M
DEFAULT_CHUNK_SIZE = 100000

f = open("data.txt", "wb")
# for i in range(0, DEFAULT_NUMBER_OF_FILES):
f.seek(DEFAULT_MAXIMUM_FILE_SIZE - 1)
f.write(b"\0")

f.close()

# print size of file
print((os.stat("data.txt").st_size)/DEFAULT_MAXIMUM_FILE_SIZE, "MB")