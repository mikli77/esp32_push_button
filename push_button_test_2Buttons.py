from machine import Pin#,Timer
from utime import sleep
import uasyncio
import queue
import push_button
import micropython

micropython.alloc_emergency_exception_buf(100)
# Button
pButton1=27
pButton2=23

def myFunc1_1():
    global b1
    b1.put(11)
    print('Ich bin hier 1_1')
    
    
def myFunc1_2():
    global b1
    b1.put_nowait(12)
    print('Ich bin hier 1_2')

def myFunc1_3():
    global b1
    b1.put_nowait(13)
    print('Ich bin hier 1_3')
    
def myFunc2_1():
    global b1
    b1.put_nowait(21)
    print('Ich bin hier 2_1')
    
def myFunc2_2():
    global b1
    b1.put_nowait(22)
    print('Ich bin hier 2_2')

def myFunc2_3():
    global b1
    b1.put_nowait(23)
    print('Ich bin hier 2_3')

button1=Pin(pButton1, Pin.IN, Pin.PULL_UP)
button2=Pin(pButton2, Pin.IN, Pin.PULL_UP)

pButton1=push_button.push_button(button1,myFunc1_1,myFunc1_3,myFunc1_2)
pButton2=push_button.push_button(button2,myFunc2_1,myFunc2_3,myFunc2_2)


async def main():
    global b1
    print('Hier')

    value=0

    while True:
        if not b1.empty():
            
            x=await b1.get()
            print(x)  

            if x==21:
                value+=1 
            elif x==22:
                value+=10 
            elif x==23:
                value=0
            value=value%100
            print('Wert: ',value)
            
        await uasyncio.sleep(0.1)

b1=queue.Queue()
uasyncio.run(main())
