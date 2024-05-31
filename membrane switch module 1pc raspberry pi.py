from machine import Pin
import utime
import _thread


R1 = machine.Pin(14,machine.Pin.OUT)
R2 = machine.Pin(12,machine.Pin.OUT)
R3 = machine.Pin(10,machine.Pin.OUT)
R4 = machine.Pin(8,machine.Pin.OUT)
C1 = machine.Pin(6,machine.Pin.IN,machine.Pin.PULL_DOWN)
C2 = machine.Pin(4,machine.Pin.IN,machine.Pin.PULL_DOWN)
C3 = machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_DOWN)
C4 = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_DOWN)

User_Key = "null"        

def Keyboard_Scanner():  
    global User_Key
    Lock = "UNLOCKED"    
    
    while True:                 
        Key_Pressed = "null"    
        
        
        R1.value(1)             
        R2.value(0)
        R3.value(0)
        R4.value(0)    
        if C1.value() == True: Key_Pressed = "1" 
        if C2.value() == True: Key_Pressed = "2"
        if C3.value() == True: Key_Pressed = "3"
        if C4.value() == True: Key_Pressed = "A"
                  
        R1.value(0)           
        R2.value(1)
        R3.value(0)
        R4.value(0)    
        if C1.value() == True: Key_Pressed = "4"
        if C2.value() == True: Key_Pressed = "5"
        if C3.value() == True: Key_Pressed = "6"
        if C4.value() == True: Key_Pressed = "B"
            
        R1.value(0)             
        R2.value(0)
        R3.value(1)
        R4.value(0)    
        if C1.value() == True: Key_Pressed = "7"
        if C2.value() == True: Key_Pressed = "8"
        if C3.value() == True: Key_Pressed = "9"
        if C4.value() == True: Key_Pressed = "C"
            
        R1.value(0)             
        R2.value(0)
        R3.value(0)
        R4.value(1)    
        if C1.value() == True: Key_Pressed = "*"
        if C2.value() == True: Key_Pressed = "0"
        if C3.value() == True: Key_Pressed = "#"
        if C4.value() == True: Key_Pressed = "D"
 
       
        if (Lock == "LOCKED") and (Key_Pressed == "null"):
            Lock = "UNLOCKED"
            
      
        if (Lock == "UNLOCKED") and (Key_Pressed != "null"):
            Lock = "LOCKED"
            User_Key = Key_Pressed
        
        utime.sleep(.02) 

_thread.start_new_thread(Keyboard_Scanner,())  



while True:
    if User_Key != "null":              
        Key_Code = User_Key           
        User_Key = "null"              
        print("Key Code =",Key_Code)
    
    utime.sleep(.1)  
        