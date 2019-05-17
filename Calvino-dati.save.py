
import paho.mqtt.client as mqtt
import subprocess
import threading
import time
temperatura=''
pressione=''
altitudine=''
luce=''
flag=1
def ricevi_dati():
	while True:
                lines=[]
                cont = 0
                righe = 0
                temperatura=''
                pressione=''
                altitudine=''
                luce=''
                global flag
                with open('trash.txt','w') as file:
                        subprocess.call(['mosquitto_sub','-t','/calvino-05/#','-h','broker.shiftr.io','-u','calvino00','-P','0123456789','-d','-C','4'],stdout=file)
                with open('trash.txt', 'r') as file:
                        for item in file:
                                cont += 1
                                if cont == 7:
                                        temperatura = item.strip()
                                elif cont == 9:
                                        pressione = item.strip()
                                elif cont == 11:
                                        altitudine = item.strip()
                                elif cont == 13:
                                        luce = item.strip()
                with open('salvadati.txt','r+') as file:
                        lines=file.readlines()
                        i=0
                        righe=len(lines)
                if righe==240:
                    del lines[0:4]
                    with open('salvadati.txt','w') as file:
                        for i in lines:
                            file.write(i)
                with open('salvadati.txt','a') as file:
                         file.write(temperatura+'\n')
                         file.write(pressione+'\n')
                         file.write(altitudine+'\n')
                         file.write(luce+'\n')
                time.sleep(60)

if __name__ == "__main__":
    subprocess.call(['rm','salvadati.txt'])
    subprocess.call(['touch','salvadati.txt'])
    t1=threading.Thread(target=ricevi_dati,daemon = True)
    t1.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        subprocess.call(['rm','trash.txt'])
        print('Arrivederci da Toni e Costa')
