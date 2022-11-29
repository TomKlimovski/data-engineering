from faker import Faker
import os
import json

fake = Faker()

DEFAULT_NUMBER_OF_FILES = 10

K, M, G = 1024, 1024, 1024

# 1 megabyte
DEFAULT_MAXIMUM_FILE_SIZE = 1 * K * M

# Faker.seed(0)
fake_json_list = []

# print(fake_json_list)
with open("data.json", "w") as f:
    while(os.stat("data.json").st_size < 64):
        fake_json_list.append(fake.json(data_columns={'ID': 'pyint',
                                        'Details': {'Name': 'name', 'Address': 'address'}}, num_rows=1))
        # strip brackets from list
        data = fake_json_list[1:-1]
        print(type(data))
        f.write(''.join(fake_json_list))


f.close()

print((os.stat("data.json").st_size)/DEFAULT_MAXIMUM_FILE_SIZE, "MB")
