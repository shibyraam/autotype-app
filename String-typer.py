import keyboard as kb
import time
import string
x = int(input("How many serail in alphabet : "))
y = input("Supplier Peice Ref No. : ")
time.sleep(3)
for i in range (0,x):
    kb.write(string.ascii_uppercase[i]+"-"+y)
    kb.press_and_release('enter')
    time.sleep(0.2)
    #print(string.ascii_uppercase[i]+"-"+y)
