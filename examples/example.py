# MIT license; Copyright (c) 2025, Planet Innovation
# 436 Elgar Road, Box Hill, 3128, VIC, Australia
# Phone: +61 3 9945 7510
#


from micropython_mock import Mock


spi = Mock()
spi.send.return_value = 1

print(spi.send(0x00))  # 1

spi.send.assert_called_with(0x00)

print(spi.send(0x01))  # 1

try:
    spi.send.assert_called_with(0x00)
except AssertionError:
    print("AssertionError")

spi.recv.side_effect = [3, 4, 5]

print(spi.recv())  # 3
print(spi.recv())  # 4
print(spi.recv())  # 5

spi.reset()

print(spi.recv())  # 3
print(spi.recv())  # 4
