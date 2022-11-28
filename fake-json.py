
from jsf import JSF
import json
import os

DEFAULT_NUMBER_OF_FILES = 10

K, M, G = 1024, 1024, 1024

# 1 megabyte
DEFAULT_MAXIMUM_FILE_SIZE = 1 * K * M

faker = JSF(
    {
        "type": "object",
        "properties": {
            "id": {"type": "string", "$provider": "faker.uuid"},
            "name": {"type": "string", "$provider": "faker.name"},
            "email": {"type": "string", "$provider": "faker.email"},
            "description": {"type": "string", "$provider": "faker.text"}
        },
        "required": ["id", "name", "email", "description"],
    }
)

# write list to file in json format

with open("data.json", "w") as f:
    fake_json_list = [faker.generate() for _ in range(DEFAULT_NUMBER_OF_FILES)]

    f.write(''.join(json.dumps(fake_json_list, indent=4)))
f.close()

print((os.stat("data.json").st_size)/DEFAULT_MAXIMUM_FILE_SIZE, "MB")
