from enum import Enum

class TrafficSignal(Enum):
    RED = 1
    GREEN =2
    YELLOW =3

print(TrafficSignal.GREEN.value)
print(TrafficSignal.RED.value)
print(TrafficSignal.YELLOW.value)