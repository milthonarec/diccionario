def mostrar_menu():
    """
    Muestra el menú interactivo del diccionario informático.
    """
    print("\n*** Diccionario Informático  ***")
    print("1. Buscar término")
    print("2. Agregar término")
    print("3. Eliminar término")
    print("4. Ver todos los términos")
    print("5. Salir")

def buscar_termino(diccionario, termino):
    """
    Busca un término en el diccionario informático.

    Parámetros:
    diccionario (dict): Diccionario que contiene los términos y sus definiciones.
    termino (str): Término a buscar.

    Retorna:
    str: Definición del término o un mensaje indicando que no se encontró.
    """
    try:
        return diccionario[termino.lower()]
    except KeyError:
        return f"El término '{termino}' no se encuentra en el diccionario."

def agregar_termino(diccionario, termino, definicion):
    """
    Agrega un nuevo término y su definición al diccionario informático.

    Parámetros:
    diccionario (dict): Diccionario que contiene los términos y sus definiciones.
    termino (str): Término a agregar.
    definicion (str): Definición del término.

    Retorna:
    str: Mensaje confirmando que el término fue agregado.
    """
    diccionario[termino.lower()] = definicion
    return f"El término '{termino}' ha sido agregado exitosamente."

def eliminar_termino(diccionario, termino):
    """
    Elimina un término del diccionario informático.

    Parámetros:
    diccionario (dict): Diccionario que contiene los términos y sus definiciones.
    termino (str): Término a eliminar.

    Retorna:
    str: Mensaje confirmando que el término fue eliminado o indicando que no se encontró.
    """
    try:
        del diccionario[termino.lower()]
        return f"El término '{termino}' ha sido eliminado exitosamente."
    except KeyError:
        return f"El término '{termino}' no se encuentra en el diccionario."

def ver_todos_terminos(diccionario):
    """
    Muestra todos los términos y definiciones del diccionario informático.

    Parámetros:
    diccionario (dict): Diccionario que contiene los términos y sus definiciones.

    Retorna:
    str: Términos y definiciones en formato de lista.
    """
    if not diccionario:
        return "El diccionario está vacío."
    return "\n".join([f"{term}: {definition}" for term, definition in diccionario.items()])

def main():
    """
    Función principal que ejecuta el menú interactivo del diccionario informático.
    """
    diccionario = {
        "algorithm": "Conjunto de instrucciones paso a paso para realizar una tarea o resolver un problema.",
        "api": "Interfaz de programación de aplicaciones que permite la comunicación entre diferentes software.",
        "array": "Estructura de datos que almacena una colección de elementos en un orden específico.",
        "bandwidth": "Capacidad de transmisión de datos de una red en un tiempo determinado.",
        "bit": "La unidad más pequeña de datos en un ordenador, representada como 0 o 1.",
        "byte": "Unidad de información digital que generalmente consta de 8 bits.",
        "cache": "Almacenamiento temporal de datos de alta velocidad que permite un acceso más rápido a la información.",
        "cloud computing": "Distribución de servicios informáticos a través de internet, incluyendo servidores, almacenamiento y bases de datos.",
        "compiler": "Programa que traduce código fuente escrito en un lenguaje de programación a código máquina.",
        "cookie": "Pequeño archivo que se almacena en el navegador del usuario para rastrear información sobre su actividad en la web.",
        "cybersecurity": "Práctica de proteger sistemas, redes y programas de ataques digitales.",
        "database": "Colección organizada de datos que se puede acceder, gestionar y actualizar.",
        "debugging": "Proceso de encontrar y corregir errores en el código de un programa.",
        "encryption": "Método para proteger información convirtiéndola en un formato que solo puede ser leído por personas autorizadas.",
        "firewall": "Sistema de seguridad de red que controla y filtra el tráfico de entrada y salida.",
        "firmware": "Software que está permanentemente incrustado en un hardware.",
        "frontend": "Parte de un sitio web o aplicación que interactúa directamente con el usuario.",
        "gigabyte": "Unidad de almacenamiento digital equivalente a 1,024 megabytes.",
        "hacker": "Persona que utiliza sus habilidades informáticas para explorar, manipular o acceder a sistemas de manera no autorizada.",
        "html": "Lenguaje de marcado utilizado para crear y estructurar páginas web.",
        "http": "Protocolo de transferencia de hipertexto utilizado en la comunicación en la web.",
        "https": "Versión segura del protocolo HTTP, que cifra los datos enviados entre el navegador y el servidor.",
        "ip address": "Dirección única que identifica a un dispositivo en una red.",
        "iteration": "Repetición de un proceso en un bucle hasta que se cumpla una condición específica.",
        "json": "Formato de intercambio de datos basado en texto, utilizado para transmitir datos entre un servidor y una aplicación web.",
        "kernel": "Núcleo del sistema operativo que gestiona las operaciones básicas de hardware y software.",
        "latency": "Tiempo que tarda un paquete de datos en viajar desde el origen hasta el destino.",
        "machine learning": "Rama de la inteligencia artificial que permite a las máquinas aprender de los datos y mejorar sus tareas sin ser programadas explícitamente.",
        "malware": "Software malicioso diseñado para dañar o comprometer la seguridad de un sistema.",
        "megabyte": "Unidad de almacenamiento digital equivalente a 1,024 kilobytes.",
        "middleware": "Software que actúa como intermediario entre diferentes aplicaciones o servicios.",
        "multithreading": "Capacidad de un procesador para ejecutar múltiples hilos de ejecución simultáneamente.",
        "network": "Conjunto de computadoras y dispositivos interconectados que pueden compartir recursos e información.",
        "node": "Punto de conexión en una red que puede enviar, recibir o reenviar datos.",
        "open source": "Software cuyo código fuente está disponible para el público y puede ser modificado y distribuido por cualquier persona.",
        "packet": "Unidad de datos que se transmite a través de una red.",
        "pixel": "Unidad más pequeña de una imagen digital, que forma parte de la visualización de una pantalla.",
        "protocol": "Conjunto de reglas que determinan cómo se transmite y recibe información en una red.",
        "python": "Lenguaje de programación interpretado, de alto nivel y de propósito general, conocido por su simplicidad y legibilidad.",
        "query": "Solicitud de información de una base de datos.",
        "ram": "Memoria de acceso aleatorio utilizada por el sistema operativo y las aplicaciones para almacenar temporalmente datos y ejecutar procesos.",
        "runtime": "Período durante el cual un programa se está ejecutando.",
        "script": "Archivo de código que se ejecuta de forma automatizada para realizar una serie de tareas.",
        "seo": "Optimización de motores de búsqueda, proceso de mejorar la visibilidad de un sitio web en los resultados de búsqueda.",
        "server": "Computadora o sistema que proporciona recursos, datos o servicios a otros dispositivos en una red.",
        "software": "Conjunto de instrucciones y datos que indican a un ordenador cómo realizar tareas específicas.",
        "sql": "Lenguaje de consulta estructurado utilizado para gestionar y manipular bases de datos relacionales.",
        "ssl": "Protocolo de seguridad que cifra los datos transferidos entre un servidor y un cliente.",
        "syntax": "Conjunto de reglas que definen cómo se deben escribir los programas en un lenguaje de programación.",
        "tcp/ip": "Conjunto de protocolos que permite la comunicación entre computadoras en una red.",
        "thread": "Secuencia de ejecución dentro de un proceso que puede ejecutarse de manera concurrente con otros hilos.",
        "ui": "Interfaz de usuario, parte de una aplicación o sistema con la que el usuario interactúa.",
        "url": "Localizador uniforme de recursos, dirección utilizada para acceder a recursos en la web.",
        "username": "Nombre que un usuario elige o se le asigna para identificarse en un sistema.",
        "virtual machine": "Software que emula un sistema operativo dentro de otro sistema operativo.",
        "virus": "Programa malicioso que se replica a sí mismo y puede infectar otros archivos y sistemas.",
        "vpn": "Red privada virtual, tecnología que crea una conexión segura y cifrada a través de una red pública.",
        "web browser": "Aplicación utilizada para acceder a sitios web y navegar por la internet.",
        "xml": "Lenguaje de marcado extensible utilizado para almacenar y transportar datos de manera estructurada.",
        "bandwidth": "Cantidad de datos que se pueden transmitir a través de una conexión de red en un tiempo específico.",
        "bluetooth": "Estándar de tecnología inalámbrica para intercambiar datos a corta distancia.",
        "boot": "Proceso de iniciar un sistema operativo en un ordenador.",
        "cd-rom": "Disco compacto de memoria de solo lectura utilizado para almacenar datos.",
        "chip": "Circuito integrado que contiene los componentes electrónicos necesarios para ejecutar tareas computacionales.",
        "dns": "Sistema de nombres de dominio que traduce nombres de dominio a direcciones IP.",
        "ethernet": "Tecnología de red cableada utilizada para conectar dispositivos en una red local.",
        "gigahertz": "Unidad de frecuencia equivalente a mil millones de ciclos por segundo, utilizada para medir la velocidad de los procesadores.",
        "input": "Datos o información que se ingresan en un sistema o dispositivo.",
        "ip": "Protocolo de internet, conjunto de reglas para el enrutamiento y direccionamiento de paquetes de datos en una red.",
        "jpeg": "Formato de compresión de imágenes utilizado para reducir el tamaño de archivos gráficos.",
        "motherboard": "Placa base que contiene los componentes principales de un ordenador, incluidos el procesador, la memoria y los puertos de expansión.",
        "router": "Dispositivo que dirige el tráfico de datos entre diferentes redes, permitiendo la comunicación entre dispositivos en una red."

    }

    while True:
        mostrar_menu()
        try:
            opcion = int(input("***  Selecciona una opción:  ***"))
            if opcion == 1:
                termino = input("Ingresa el término a buscar: ")
                print(buscar_termino(diccionario, termino))
            elif opcion == 2:
                termino = input("Ingresa el nuevo término: ")
                definicion = input("Ingresa la definición del término: ")
                print(agregar_termino(diccionario, termino, definicion))
            elif opcion == 3:
                termino = input("Ingresa el término a eliminar: ")
                print(eliminar_termino(diccionario, termino))
            elif opcion == 4:
                print(ver_todos_terminos(diccionario))
            elif opcion == 5:
                print("Saliendo del diccionario. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

if __name__ == "__main__":
    main()
