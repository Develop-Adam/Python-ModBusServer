"""
This module reads the coil state from a Modbus server.

Author: Adam
Date: May 30, 2023
"""

from pyModbusTCP.client import ModbusClient


# init modbus client
C = ModbusClient(host='localhost', port=12345, auto_open=True, debug=False)

# Create a list of coil states to write
COILS = [True]

# Write the coils starting from address 0
ADDRESS = 0
C.write_multiple_coils(ADDRESS, COILS)

# Read the coils to verify the write operation
READ_COILS = C.read_coils(ADDRESS, len(COILS))
print(READ_COILS)

# Specify the address of the register to write
REGISTER_ADDRESS = 0

# Specify the value to write to the register [ Min: 0 | Max: 65535 ]
REGISER_VALUE = 65535

# Write the value to the register
C.write_single_register(REGISTER_ADDRESS, REGISER_VALUE)

REG_0 = C.read_holding_registers(REGISTER_ADDRESS, 1)

print(REG_0)

# End of file