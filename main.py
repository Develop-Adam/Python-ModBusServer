from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep

# Constants
HOST = "127.0.0.1"
PORT = 12346
NUM_REGISTERS = 1000
NUM_COILS = 1000

# Create an instance of ModbusServer
server = ModbusServer(HOST, PORT, no_block=True)
data_bank = DataBank(NUM_REGISTERS, NUM_COILS)

# Initialize the initial states for coils and registers
coil_state = [False] * NUM_COILS
register_state = [0] * NUM_REGISTERS

try:
    print("Start server...")
    server.start()
    print("Server is online")

    while True:
        # Check if any coils have changed
        new_coil_state = data_bank.get_discrete_inputs(0, NUM_COILS)
        for i in range(NUM_COILS):
            if coil_state[i] != new_coil_state[i]:
                coil_state[i] = new_coil_state[i]
                print(f"Coil {i} has changed to {coil_state[i]}")

        # Check if any registers have changed
        new_register_state = data_bank.get_holding_registers(0, NUM_REGISTERS)
        for i in range(NUM_REGISTERS):
            if register_state[i] != new_register_state[i]:
                register_state[i] = new_register_state[i]
                print(f"Register {i} has changed to {register_state[i]}")

        sleep(0.5)

except:
    print("Shutdown server...")
    server.stop()
    print("Server is offline")
