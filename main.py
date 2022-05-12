import snap7
import time

IP = '192.168.0.18' #Adress PLC
RACK = 0
SLOT = 2

DB_NUMBER = 1 #Which DB I need to read
START_ADRESS = 0
SIZE = 259

plc = snap7.client.Client() # Instance PLC
plc.connect(IP, RACK, SLOT)

plc_info = plc.get_cpu_info() #Info about CPU
print(f'Module Type: {plc_info.ModuleTypeName}')

state = plc.get_cpu_state()#Info about CPU's status
print(f'State: {state}')

while True:
    db = plc.db_read(DB_NUMBER, START_ADRESS, SIZE) #Reading info from PLC
    product_name = db [2:256].decode('UTF-8').strip('\x00') #Decode info 'String'
    NumberDB = int.from_bytes(db[256:258], byteorder='big') #Decode info 'Int'
    StatusDB = bool(db[258]) #Decode info 'Bool'
    print(product_name)
    print(NumberDB)
    print(StatusDB)
    time.sleep(5)

#plc.disconnect() #Disconnect PLC

