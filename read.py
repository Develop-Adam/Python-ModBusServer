from pyModbusTCP.client import ModbusClient

# init modbus client
c = ModbusClient(host='localhost', port=12346, auto_open=True, debug=False)

# Create a list of coil states to write
coils = [True, True, True, True, True, False, False, False, False, False]

# Write the coils starting from address 0
address = 0
c.write_multiple_coils(address, coils)

# Read the coils to verify the write operation
read_coils = c.read_coils(address, len(coils))
print(read_coils)

# Specify the address of the register to write
register_address = 0

# Specify the value to write to the register
register_value = 123

# Write the value to the register
c.write_single_register(register_address, register_value)

reg_0 = c.read_holding_registers(register_address, 1)

print(reg_0)