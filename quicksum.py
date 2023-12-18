import re

def quicksum(packet):
    result = 1
    packet_by_2 = []
    if packet.isupper() == False:
        return 0
    for i, elem in enumerate(packet):
        if i == len(packet) - 1:
            packet_by_2.append(elem)
        elif elem:
            packet_by_2.append((elem, packet[i+1]))
    print(packet_by_2)
    return 0

print(quicksum("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"))