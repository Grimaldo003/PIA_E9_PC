#!/usr/bin/env python3
#_*_ coding: utf-8 _*_
#EQUIPO3
#importaciones
import main_python, logging
import scapy.all as scapy
from scapy.layers import http

# Configurar el logging para que se guarde en un archivo.log
logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(message)s',
filename='w.cibersecurity.log',
filemode='a')
#Inicion de la función traffic

logging.debug('NO USAR CABLE ETHERNET')
logging.debug('INSTALAR npcap antes de ejecutar ')

#Inicio de la función sniif
def sniif(interface):
    logging.debug("Entramos a la función sniif")
    #Extre datos del http
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet)
#Inicio de la función sniffed packet
def sniffed_packet(packet):
    logging.debug("Entramos a la función sniffed_packet")
    if packet.haslayer(http.HTTPRequest): #condición para que reconosca solo paginas http
        logging.info('La condicion cumple')
        print(f"""

            """)
        print("*"*100)
        print(packet.show())#Muestra los datos de esta pagina
        print("*"* 100)
    pass#En caso de error lo ignora y continua la ejecución

    #Inicio de la función  main 
def main():
    logging.debug("Entramos a la función main")
    while True: #condicón para que el usurio pueda salir o seguir consultando
        logging.debug("Entramos a la condición while True")
        print(f"""
            1. Iniciar o Continuar\n
            2. Detener captura
            """)

        choice = input("Introduzca su elección (1/2):       ")
        if choice == "1":
            logging.debug("Cumpliendo a la condición")
            sniif("Wi-Fi")
        elif choice == "2":
            logging.debug("Saliendo del main")
            print(f"\nDeteniendo captura...\n")
            main_python.main()
            
        else:
            logging.warning("Elección inválida")
            print("Elección inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    
    main()#Llamado de la función main 
