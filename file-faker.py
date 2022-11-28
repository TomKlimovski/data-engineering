from faker import Faker
import os

fake = Faker()

DEFAULT_NUMBER_OF_FILES = 10

K, M, G = 1024, 1024, 1024

# 1 megabyte
DEFAULT_MAXIMUM_FILE_SIZE = 1 * K * M

Faker.seed(0)
fake_json_list = []
for _ in range(5):
    fake_json_list.append(fake.json(data_columns={'ID': 'pyint',
                                                  'Details': {'Name': 'name', 'Address': 'address'}}, num_rows=2))

# print(fake_json_list)
with open("data.json", "w") as f:
    f.write(''.join(fake_json_list))

f.close()

print((os.stat("data.json").st_size)/DEFAULT_MAXIMUM_FILE_SIZE, "MB")
