from enum import Enum

class Role(Enum):
    ADMIN =1
    USER=2

print(Role.ADMIN.value)