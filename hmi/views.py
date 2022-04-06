from cgi import print_arguments
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import binascii
import time
import serial
import socket
import time
import os
import threading
import datetime
from time import gmtime, strftime
import minimalmodbus
import serial       
import time  

class Atlas:
    def __init__(self):
        # Atlas modbus table
        self.count = 0
        self.atlas_table = {
            # Operations
            'operation': {
                'Gen 1 Start': {'plc address': 'C700', 'modbus address': 3521},
                'Gen 1 Stop': {'plc address': 'C701', 'modbus address': 3522},
                'Gen 2 Start': {'plc address': 'C702', 'modbus address': 3523},
                'Gen 2 Stop': {'plc address': 'C703', 'modbus address': 3524},
                'Shorpower Start': {'plc address': 'C704', 'modbus address': 3525},
                'Shorpower Stop': {'plc address': 'C705', 'modbus address': 3526},
                'Stand-By Gen 1': {'plc address': 'C706', 'modbus address': 3527},
                'Stand-By Gen 2': {'plc address': 'C707', 'modbus address': 3528},
                'Transfer load to Gen 1': {'plc address': 'C711', 'modbus address': 3530},
                'Transfer load to Gen 2': {'plc address': 'C712', 'modbus address': 3531},
                'Transfer load to Shorpower': {'plc address': 'C713', 'modbus address': 3532},
                'Alarm Silence': {'plc address': 'C714', 'modbus address': 3533},
                'Fault Reset': {'plc address': 'C715', 'modbus address': 3534},
                },
            # Status
            'status': {
                'Gen 1 Run': {'plc address': 'C474', 'modbus address': 3389},
                'Gen 2 Run': {'plc address': 'C475', 'modbus address': 3390},
                'Gen 1 Available': {'plc address': 'C476', 'modbus address': 3391},
                'Gen 2 Available': {'plc address': 'C477', 'modbus address': 3392},
                'Gen 1 Cool Down': {'plc address': 'C503', 'modbus address': 3396},
                'Gen 2 Cool Down': {'plc address': 'C504', 'modbus address': 3397},
                'Gen 1 Starting': {'plc address': 'C511', 'modbus address': 3402},
                'Gen 2 Starting': {'plc address': 'C513', 'modbus address': 3404},
                'Shore Power Starting': {'plc address': 'C516', 'modbus address': 3407},
                'Gen 1 synchronizing': {'plc address': 'C517', 'modbus address': 3408},
                'Gen 2 synchronizing': {'plc address': 'C520', 'modbus address': 3409},
                'Shorpower synchronizing': {'plc address': 'C522', 'modbus address': 3411},
                'Transfer to Shorpower inhibit load high': {'plc address': 'C523', 'modbus address': 3412},
                'Warning Load high': {'plc address': 'C524', 'modbus address': 3413},
                'Gen 1 On line': {'plc address': 'C531', 'modbus address': 3418},
                'Gen 2 On line': {'plc address': 'C532', 'modbus address': 3419},
                'Shorpower On Line': {'plc address': 'C534', 'modbus address': 3421},
                'Gen 1 Standby': {'plc address': 'C535', 'modbus address': 3422},
                'Gen 2 Standby': {'plc address': 'C536', 'modbus address': 3423},
                'Load Shed 1 Active': {'plc address': 'C537', 'modbus address': 3424},
                'Load Shed 2 Active': {'plc address': 'C540', 'modbus address': 3425},
                'Load Shed 3 Active': {'plc address': 'C541', 'modbus address': 3426},
            },
            # Faults
            'faults': {
                'Gen 1 CB Tripped': {'plc address': 'C1000', 'modbus address': 3585},
                'Gen 2 CB Tripped': {'plc address': 'C1001', 'modbus address': 3586},
                'Shorpower CB Tripped': {'plc address': 'C1003', 'modbus address': 3588},
                'Gen 1 CB Fail to Open': {'plc address': 'C1004', 'modbus address': 3589},
                'Gen 2 CB Fail to Open': {'plc address': 'C1005', 'modbus address': 3590},
                'Shorpower CB Fail to Open': {'plc address': 'C1007', 'modbus address': 3592},
                'Gen 1 CB Fail to Close': {'plc address': 'C1010', 'modbus address': 3593},
                'Gen 2 CB Fail to Close': {'plc address': 'C1011', 'modbus address': 3594},
                'Shorpower CB Fail to Close': {'plc address': 'C1013', 'modbus address': 3596},
                'SP Output Under Volts': {'plc address': 'C1014', 'modbus address': 3597},
                'SP Input OUV': {'plc address': 'C1015', 'modbus address': 3598},
                'SP Output Over Volts': {'plc address': 'C1016', 'modbus address': 3599}, 
                'G1 High Water Temp': {'plc address': 'C1024', 'modbus address': 3605},
                'G2 High Water Temp': {'plc address': 'C1025', 'modbus address': 3606},
                'G1 Reverse Power':  {'plc address': 'C1026', 'modbus address': 3607},
                'G1 Low Oil Pressure': {'plc address': 'C1027', 'modbus address': 3608},
                'G2 Low Oil Pressure': {'plc address': 'C1030', 'modbus address': 3609},
                'G2 Reverse Power': {'plc address': 'C1031', 'modbus address': 3610},
                'G1 Engine Alarm from ECU': {'plc address': 'C1032', 'modbus address': 3611},
                'G2 Engine Alarm from ECU': {'plc address': 'C1033', 'modbus address': 3612},
                'G1 120v Relay fault': {'plc address': 'C1035', 'modbus address': 3614},
                'G2 120v Relay fault': {'plc address': 'C1036', 'modbus address': 3615},
                'SP Output Overload': {'plc address': 'C1061', 'modbus address': 3634},
                'Gen 1 Under Volts': {'plc address': 'C1062', 'modbus address': 3635},
                'Gen 1 Over Volts': {'plc address': 'C1063', 'modbus address': 3636},
                'Gen 2 Under Volts': {'plc address': 'C1064', 'modbus address': 3637},
                'Gen 2 Over Volts': {'plc address': 'C1065', 'modbus address': 3638},
                'SP EPO Pushed': {'plc address': 'C1066', 'modbus address': 3639},
                'G1 Low Coolant Level': {'plc address': 'C1067', 'modbus address': 3640},
                'G2 Low Coolant Level': {'plc address': 'C1070', 'modbus address': 3641},
                'G1 Exh Gas Temp High': {'plc address': 'C1071', 'modbus address': 3642},
                'G2 Exh Gas Temp High': {'plc address': 'C1072', 'modbus address': 3643},
                'SP Input Phase Loss': {'plc address': 'C1073', 'modbus address': 3644},
                'G1 Low Oil Level': {'plc address': 'C1077', 'modbus address': 3648},
                'G2 Low Oil Level': {'plc address': 'C1100', 'modbus address': 3649},
                'G1 High Frequency': {'plc address': 'C1101', 'modbus address': 3650},
                'G1 Low Frequency': {'plc address': 'C1102', 'modbus address': 3651},
                'G2 High Frequency': {'plc address': 'C1103', 'modbus address': 3652},
                'G2 Low Frequency': {'plc address': 'C1104', 'modbus address': 3653},
                'High Ground Current': {'plc address': 'C1106', 'modbus address': 3655},
                'G1 Crank Fail': {'plc address': 'C1107', 'modbus address': 3656},
                'G1 Overspeed': {'plc address': 'C1110', 'modbus address': 3657},
                'G1 Low Battery Volts': {'plc address': 'C1111', 'modbus address': 3658},
                'G1 High Battery Volts': {'plc address': 'C1112', 'modbus address': 3659},
                'G2 Crank Fail': {'plc address': 'C1113', 'modbus address': 3660},
                'G2 Overspeed': {'plc address': 'C1114', 'modbus address': 3661},
                'G2 Low Battery Volts': {'plc address': 'C1115', 'modbus address': 3662},
                'G2 High Battery Volts': {'plc address': 'C1116', 'modbus address': 3663}        
            },
            # Gen 1 data
            'Gen 1 digital meter': {  
                'L1-N Volts': {'plc address': '1921', 'modbus address': 3600},
                'L2-N Volts': {'plc address': '1923', 'modbus address': 3602},
                'L3-N Volts': {'plc address': '1925', 'modbus address': 3604},
                'Line 1-Line 2 Volts': {'plc address': '1927', 'modbus address': 3606},
                'Line 1-Line 3 Volts': {'plc address': '1929', 'modbus address': 3610},
                'Line 2-Line 3 Volts': {'plc address': '1931', 'modbus address': 3612},
                'Line 1 Amps': {'plc address': '1933', 'modbus address': 3614},
                'Line 2 Amps': {'plc address': '1935', 'modbus address': 3616},
                'Line 3 Amps': {'plc address': '1937', 'modbus address': 3620},
                'Total KW': {'plc address': '1939', 'modbus address': 3622},
                'Average PF': {'plc address': '1941', 'modbus address': 3624},
                'Frequency': {'plc address': '1943', 'modbus address': 3626}, 
                'Total kVA': {'plc address': '1945', 'modbus address': 3630}, 
            },
            # Gen 2 data
            'Gen 2 digital meter': {
                'L1-N Volts': {'plc address': '1949', 'modbus address': 3634}, 
                'L2-N Volts': {'plc address': '1951', 'modbus address': 3636},
                'L3-N Volts': {'plc address': '1953', 'modbus address': 3640},
                'Line 1-Line 2 Volts': {'plc address': '1955', 'modbus address': 3642},
                'Line 1-Line 3 Volts': {'plc address': '1957', 'modbus address': 3644},
                'Line 2-Line 3 Volts': {'plc address': '1959', 'modbus address': 3646},
                'Line 1 Amps': {'plc address': '1961', 'modbus address': 3650},
                'Line 2 Amps': {'plc address': '1963', 'modbus address': 3652},
                'Line 2 Amps': {'plc address': '1963', 'modbus address': 3652},
                'Line 3 Amps': {'plc address': '1965', 'modbus address': 3654},
                'Total KW': {'plc address': '1967', 'modbus address': 3656},
                'Average PF': {'plc address': '1969', 'modbus address': 3660},        
                'Frequency': {'plc address': '1971', 'modbus address': 3662}, 
                'Total kVA': {'plc address': '1973', 'modbus address': 3664},
            },
            #Shore power data
            'Shore Converter Output digital meter': {
                'L1 Amps': {'plc address': '2300', 'modbus address': 1217},
                'L2 Amps': {'plc address': '2302', 'modbus address': 1219},
                'L3 Amps': {'plc address': '2304', 'modbus address': 1221},
                'Total KW': {'plc address': '2306', 'modbus address': 1223},
                'Line 1-Line 2 Volts': {'plc address': '2310', 'modbus address': 1225},
                'Line 1-Line 3 Volts': {'plc address': '2312', 'modbus address': 1227},
                'Line 2-Line 3 Volts': {'plc address': '2314', 'modbus address': 1229},
                'Frequency': {'plc address': '2316', 'modbus address': 1231},
                'Total KVA': {'plc address': '2320', 'modbus address': 1233},
                'Average PF': {'plc address': '2324', 'modbus address': 1237},
                'L1-N Volts': {'plc address': '2326', 'modbus address': 1239},
                'L2-N Volts': {'plc address': '2330', 'modbus address': 1241},
                'L3-N Volts': {'plc address': '2332', 'modbus address': 1243},
            }  
        }
        # Placeholder for commands
        self.ops = []
        # Status of the system
        self.status = {}
        # Connection to PLC 
        self.connected = False
        self.rtu_connected = True
        self.atlas_link = None
        self.atlas_rtu_link = None
        # Constants
        self.TCP = 'tcp'
        self.RTU = 'rtu'
        self.READ = 'read'
        self.WRITE = 'write'
        self.COIL = 'coil'
        self.REGISTER = 'register'
        threading.Thread(target=self.start_atlas).start()
        
        
    
    def start_atlas(self):
        print(f"Atlas connected? : {self.connected}")
        while not self.connected:
            self.status['connected'] = False
            self.connect()

        while True:
            if self.connected:
                self.status['connected'] = True
                self.getStatus()
                self.getFaults()
                self.getAnalogValues()
            else:
                self.connected = False
              
    
    def plc_request(self, op, address, op_type, value=False, via='tcp'):
        success = False

        time.sleep(0.1)
        if op == self.READ:
            if op_type == self.COIL:
                try:
                    return self.atlas_link.read_bit(address)
                except:
                    return None

        if op == self.READ:
            if op_type == self.REGISTER:
                if via == self.TCP:
                    try:
                       while not success:
                           value = self.atlas_link.read_long(address)
                           success = True
                        
                       return value
                        
                        
                    except:
                        self.connected = False
                        return 0
                    
                if via == self.RTU:
                    try:
                        value = self.atlas_rtu_link.read_holding_register(address)
                        if value:
                            return value
                        else:
                            return False
                    except:
                        self.connected = False 
                        return None
                
        if op == self.WRITE:
            if op_type == self.COIL:
                try:
                    self.atlas_link.write_coil(address, value)
                    return True
                except:
                    return False    
                
        if op == self.WRITE:
            if op_type == self.REGISTER:
                try:
                    self.atlas_link.write_holding_register(address, value)
                    return True
                except:
                    return False                
                
    def connect(self):
        while not self.connected:
            time.sleep(1)
            try:
                print('trying to connect')
                self.atlas_link = minimalmodbus.Instrument('COM5', 1)
                self.atlas_link.mode = minimalmodbus.MODE_RTU   
                self.atlas_link.clear_buffers_before_each_transaction = True
                self.atlas_link.serial.baudrate = 9600        
                self.atlas_link.serial.bytesize = 8
                self.atlas_link.serial.parity = serial.PARITY_ODD
                self.atlas_link.serial.stopbits = 1
                self.atlas_link.serial.timeout  = 0.05
                
                for address in range(1931, 1940):
                    try: 
                        val = self.atlas_link.read_long(address)
                        self.connected = True
                        break
                    except:
                        continue    
                
            except:
                print('Cant connect to plc')
    
    def getStatus(self):
        if self.connected:
            try:
                self.status['state'] = [[{op: self.plc_request(self.READ, value['modbus address'], self.COIL)} for op, value in self.atlas_table[key].items()] for key, value in self.atlas_table.items() if key == 'status'][0] 
                return self.status        
            except:
                print('getStatus fail') 
        else:
            return 0       
        
    def getFaults(self):
        if self.connected:
            self.status['faults'] = [[{op: self.plc_request(self.READ, value['modbus address'], self.COIL)} for op, value in self.atlas_table[key].items()] for key, value in self.atlas_table.items() if key == 'faults'][0]
            return self.status['faults']  

    def getAnalogValues(self):

        if self.connected:
            for analog in ['Shore Converter Output digital meter', 'Gen 2 digital meter', 'Gen 1 digital meter']:
                self.status[f"{analog}"] = [[{op: self.plc_request(self.READ, value['modbus address'] -2, self.REGISTER, self.RTU), 'address': value['modbus address']} for op, value in self.atlas_table[key].items()] for key, value in self.atlas_table.items() if key == analog][0]
                time.sleep(0.5)

            return self.status

    def commit_op(self):
        for cmd in self.ops:
            time.sleep(3)
            try:
                # Find modbus address for the command
                address = [[value['modbus address'] for key, value in op_address.items() if key == cmd] for op, op_address in self.atlas_table.items() if op == 'operation'][0][0]
                print(f"Command: {cmd}, Address: {address}")
                #self.plc_request(self.WRITE, address, self.COIL, True)
            except:
                return False
        return True


            
        
    
    def get_status(self):
        succed = False
        while not succed:
            try:
                val = self.conn.read_coils(8192, 6)
                if len(val) > 1:
                    succed = True
                    return val
            except:
                print('plc not responding')
                time.sleep(0.5)
                self.connect()
                continue
          
    def setCoil(self, coil, value):
        try:
            self.conn.write_single_coil(coil, value)
        except:
            pass    
plc = Atlas()


def index(request):
    return render(request, 'pages/index.html')

@csrf_exempt
def status(request):
    global plc
    res = plc.status
    
    return JsonResponse({'request': res})

@csrf_exempt
def setCoil(request):   
    global plc
    
    if request.method == 'POST':
        data = json.loads(request.body)
        coil = data['coil']
        value = data['value']
        plc.setCoil(coil, value)
    
    return JsonResponse({'operations': ''})


