from flask import Flask, render_template
from threading import Thread
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusServerContext

# Define the number of registers and coils to simulate
num_registers = 10  # Number of registers to simulate
num_coils = 8  # Number of coils to simulate

# Create data blocks for registers and coils
registers_block = ModbusSequentialDataBlock(0, [0] * num_registers)
coils_block = ModbusSparseDataBlock({i: False for i in range(num_coils)})

# Create Modbus server context and add data blocks
store = ModbusServerContext(slaves={
    0x01: registers_block,
    0x02: coils_block
}, single=True)

# Define server address and port
server_address = 'localhost'  # Server address
server_port = 5022  # Server port (above 1024)

# Start Modbus TCP server in a separate thread
server_thread = Thread(target=StartTcpServer, args=(store, ), daemon=True)
server_thread.start()

# Create Flask app
app = Flask(__name__)

# Define route for the registers page
@app.route('/')
def registers_page():
    registers = registers_block.getValues(0, num_registers)
    return render_template('registers.html', registers=registers)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)