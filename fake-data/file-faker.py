from faker import Faker
import os

fake = Faker()

DEFAULT_NUMBER_OF_FILES = 10

K, M, G = 1024, 1024, 1024

# 1 megabyte
DEFAULT_MAXIMUM_FILE_SIZE = 1 * K * M

# Faker.seed(0)
# fake_json_list = []

# print(fake_json_list)
with open("data.json", "w") as f:
    while(os.stat("data.json").st_size < DEFAULT_MAXIMUM_FILE_SIZE):
        fake_json_list = (fake.json(data_columns={'ID': 'pyint',
                                        'Details': {'Name': 'name', 'Address': 'address'}}, num_rows=1))

        string_data = ''.join(fake_json_list)

        f.write(string_data + ",")

f.close()

# we need to strip the last comma from the file
with open("data.json", "rb+") as f:
    f.seek(-1, os.SEEK_END)
    f.truncate()

# now i have a file with a number of json objects in it that meets
# the DEFAULT_MAXIMUM_FILE_SIZE requirement.
# however, it's not valid json. it's missing square brackets at the beginning and end.
with open("data.json", "r+") as f:
    content = f.read()
    f.seek(0, 0)
    f.write("[" + content + "]")

print((os.stat("data.json").st_size)/DEFAULT_MAXIMUM_FILE_SIZE, "MB")
