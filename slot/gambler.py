import extract
import captura
import movimiento
import time

i = 0

while i <= 100:
    movimiento.to_bet()
    time.sleep(1.5)
    captura.captura()
    time.sleep(2)
    actual_val = extract.extractnum()
    print (actual_val)
    i= i+1



if actual_val > 75:
    movimiento.prob_75()
    movimiento.to_bet()

