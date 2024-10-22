"""
Puedes usar esta API para buscar dispositivos conectados a Internet, 
recopilar información sobre estos dispositivos y buscar vulnerabilidades.
api_key == tJ73IRabIRVFSNLWZCPjzevcwswBrdt3
"""
 
#EQUIPO 3
#Importaciones
import shodan, logging, main_python
from shodan import Shodan
#configuración para los logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(message)s',
    filename='api_shodan.log',
    filemode='a')

#api_key = 'tJ73IRabIRVFSNLWZCPjzevcwswBrdt3'
#fucnión para validar key
def get_api_key():
    logging.debug('Entramos a la función get_api_key')
    while True:
        api_key = input("Ingrese su clave API de Shodan: ")
        try:
            # Intenta crear un cliente Shodan con la clave proporcionada
            shodan_api = Shodan(api_key)
            # Si no se produce ninguna excepción, la clave es válida y se retorna
            return shodan_api
        except shodan.APIError as e:
            logging.warning('La clave API es inválida')
            print(f"La clave API es inválida: {e}")
            
#Función para consultar la api de shodan
def api_shodan():
    logging.debug('Entramos a la función api_shodan')
    shodan_api = get_api_key()
    while True: #ciclo para revalidar ip y key
    
        """
        api_key == tJ73IRabIRVFSNLWZCPjzevcwswBrdt3
        Ejemplos de ip:
        76.223.26.96
        172.67.151.253
        188.216.32.202
        111.132.32.25
        """
        ip = input(f"""
                
                Ingrese la ip que desea busacar
                o presione 1 si desea salir

                Ingrese aquí:    """) # elección para que el usurio ingrese la ip o la salida
        print(f"\n")
        if ip == '1' and ip !=None and ip != str and ip != float: #condición para salir de la función
            logging.debug('Saliendo de la función')
            main_python.main()

        try:

            # Search for the specified IP
            try:
                host = shodan_api.host(ip)
            except shodan.APIError as e:
                print(f"Error de la API de Shodan para la IP {ip}: {e}")
                print(f"""
                    
                    ¡INTENTELO DE NUEVO!

                    """)
                logging.warning('Error la ip no la reconoce')
                get_api_key()#retorna a la key si la ip no se reconoce

                continue  # Saltar a la siguiente iteración si hay un error

            # Información acerca de la ip
            print(f"Información del dispositivo {ip}:")
            print(f"Hostname: {host.get('hostname', 'N/A')}")
            print(f"Sistema operativo: {host.get('os', 'N/A')}")
            print(f"Puertos abiertos: {host.get('ports', 'N/A')}")
            print(f"País: {host.get('country_name', 'N/A')}")
            print(f"Ciudad: {host.get('city', 'N/A')}")

            device_details = shodan_api.host(ip)

            # nombres de los documentos donde estan registrados las vulnerabilidades de la ip
            print('Vulnerabilities:')
            if 'vulns' in device_details:
                if isinstance(device_details['vulns'], dict):
                    # Si es un diccionario, usa items()
                    for vulnerability, details in device_details['vulns'].items():
                        print(f'- {vulnerability}: {details}')
                elif isinstance(device_details['vulns'], list):
                    # Si es una lista, itera directamente
                    for vulnerability in device_details['vulns']:
                        print(f'- {vulnerability}')
                else:
                    print("Tipo de dato de 'vulns' inesperado")
            else:
                print('No se encontró vulnerabilidades.')

        except KeyError as e:
            logging.debug('Error de clave') #excepciones en caso de algun error no previsto
            print(f"Error de clave: {e}")
        except shodan.APIError as e:
            logging.warning('Error en la API de Shodan')
            print(f"Error de la API de Shodan: {e}")
        except Exception as e:
            logging.error('Error inesperado')
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    #'tJ73IRabIRVFSNLWZCPjzevcwswBrdt3'  Reemplaza con tu propia API key 
    api_shodan() #Llamada de la función 

