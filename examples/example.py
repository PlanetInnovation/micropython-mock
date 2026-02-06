# -*- coding: utf-8 -*-
#
# PI Background IP
# Copyright (c) 2025, Planet Innovation Pty Ltd
# 436 Elgar Rd, Box Hill, 3128, VIC, Australia
# Phone: +61 3 9945 7510
#
# The copyright to the computer program(s) herein is the property of
# Planet Innovation, Australia.
# The program(s) may be used and/or copied only with the written permission
# of Planet Innovation or in accordance with the terms and conditions
# stipulated in the agreement/contract under which the program(s) have been
# supplied.


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
