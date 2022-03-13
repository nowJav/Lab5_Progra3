#lAB 5
'''import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

while True:
    board.digital[4].write(1)
    time.sleep(1)
    board.digital[4].write(0)
    time.sleep(1)'''


import pyfirmata
import time 
board = pyfirmata.Arduino('COM3')

while True:
    #ROJOS
    board.digital[5].write(1)
    board.digital[11].write(1)
    time.sleep(.5)
    board.digital[5].write(0)
    board.digital[11].write(0)

    #AMARILLOS
    board.digital[12].write(1)
    board.digital[6].write(1)
    time.sleep(.5)
    board.digital[12].write(0)
    board.digital[6].write(0)

    #VERDES
    board.digital[13].write(1)
    board.digital[7].write(1)
    time.sleep(.5)
    board.digital[13].write(0)
    board.digital[7].write(0)