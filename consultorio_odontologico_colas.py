# Universidad de Manizales
# Materia: Programación II
# Taller No. 2: Estructuras de datos - Colas
# Profesor: Ing. Jose Ubaldo Carvajal
# Estudiante: Margarita María Arango Vélez
# Fecha: 09/10/2026


from collections import deque
from datetime import date

#Clase Cliente que representa a un cliente del consultorio odontológico, con sus datos básicos de registro.
class Cliente:
    def __init__(self, cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha_cita):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha_cita = fecha_cita
        self.valor_total = 0  # El valor total por cliente se calcula más adelante con la función de precios.

    def __repr__(self):
        return (
            f"Cliente(cedula={self.cedula}, nombre={self.nombre}, "
            f"telefono={self.telefono}, tipo_cliente={self.tipo_cliente}, "
            f"tipo_atencion={self.tipo_atencion}, cantidad={self.cantidad}, "
            f"prioridad={self.prioridad}, fecha_cita={self.fecha_cita}, "
            f"valor_total={self.valor_total})"
        )
    
# El programa le pide al usuario ingresar la cédula por teclado y se repite el ciclo hasta que el dato ingresado sea válido.
def validar_cedula():
    while True:
        cedula = input("Ingrese la cédula del cliente (solo números, sin puntos): ")

        if cedula.isdigit() and cedula[0] != "0" and 7 <= len(cedula) <= 10:
            return cedula

        print()
        print("Dato inválido. La cédula debe contener solo números, tener entre 7 y 10 dígitos, y no puede empezar en 0. Por favor ingrese nuevamente el número de cédula del cliente.")

# Se pide ingresar el nombre del cliente por teclado y se repite el ciclo hasta que el dato ingresado sea válido.
def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre completo del cliente (nombres y apellidos): ")
        nombre_sin_espacios = nombre.replace(" ", "")

        if nombre_sin_espacios != "" and nombre_sin_espacios.isalpha():
            return nombre

        print()
        print("Dato inválido. El nombre debe contener solo letras y espacios, sin números ni símbolos. Por favor ingrese nuevamente el nombre del cliente.")

# Se pide ingresar el número telefónico de contacto por teclado y se repite el ciclo hasta que el dato ingresado sea válido.
# Este dato se guarda como texto para no perder un posible 0 inicial en prefijos internacionales o por si cambian los indicativos locales.
def validar_telefono():
    while True:
        telefono = input("Ingrese el teléfono de contacto del cliente: ")

        if telefono.isdigit() and 7 <= len(telefono) <= 15:
            return telefono

        print()
        print("Dato inválido. El teléfono debe contener solo números, entre 7 y 15 dígitos. Por favor ingrese nuevamente el teléfono de contacto del cliente.")

# Muestra un menú para que el usuario seleccione el tipo de cliente y el ciclo se repite hasta que la opción ingresada sea válida.
def validar_tipo_cliente():
    while True:
        print("Seleccione el tipo de cliente:")
        print("1. Particular")
        print("2. EPS")
        print("3. Prepagada")
        print()
        opcion = input("Opción: ")

        if opcion == "1" or opcion == "2" or opcion == "3":
            return opcion

        print()
        print("La opción ingresada no es válida. Por favor seleccione una opción entre 1 y 3.")

# Muestra el menú con los tipos de atención disponibles y el ciclo se repite hasta que la opción ingresada sea válida.
def validar_tipo_atencion():
    while True:
        print("Seleccione el tipo de atención:")
        print("1. Limpieza")
        print("2. Calzas")
        print("3. Extracción")
        print("4. Diagnóstico")
        print()
        opcion = input("Opción: ")

        if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
            return opcion

        print()
        print("La opción ingresada no es válida. Por favor seleccione una opción entre 1 y 4.")

# Se pide ingresar la cantidad del tipo de servicio ingresado por teclado, aplicando las reglas indicadas para cada tipo de atención.
def validar_cantidad(tipo_atencion):
    while True:
        if tipo_atencion == "1":
            cantidad_texto = input("Ingrese la cantidad (El máximo permitido para Limpieza es 1): ")
        else:
            if tipo_atencion == "4":
                cantidad_texto = input("Ingrese la cantidad (El máximo permitido para Diagnóstico es 1): ")
            else:
                cantidad_texto = input("Ingrese la cantidad (El máximo permitido para Calzas y Extracción es 32): ") # Se limita la cantidad a un máximo de 32 ya que es el número máximo de dientes que puede tener un cliente.

        if cantidad_texto.isdigit() and cantidad_texto[0] != "0":
            cantidad = int(cantidad_texto)

            if tipo_atencion == "1" or tipo_atencion == "4":
                if cantidad == 1:
                    return cantidad

            if tipo_atencion == "2" or tipo_atencion == "3":
                if cantidad >= 1 and cantidad <= 32:
                    return cantidad

        print()
        print("El dato ingresado no es válido. Verifique la cantidad según el tipo de atención seleccionado. Por favor ingrese nuevamente la cantidad.")

# Muestra un menú para asignar el nivel de prioridad del cliente y el ciclo se repite hasta que la opción ingresada sea válida.
def validar_prioridad():
    while True:
        print("Seleccione la prioridad de atención para el cliente ingresado:")
        print("1. Normal")
        print("2. Urgente")
        print()
        opcion = input("Opción: ")

        if opcion == "1" or opcion == "2":
            return opcion

        print()
        print("La opción ingresada no es válida. Por favor seleccione una opción entre 1 y 2.")

# Para validar la fecha ingresada para la cita, debemos determinar si el año ingresado es bisiesto (determinar si febrero tiene 28 o 29 días).
def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Devuelve la cantidad de días que tiene un mes específico, considerando el año (para febrero).
def dias_en_mes(mes, anio):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31

    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30

    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28

    return 0

# Se le pide al usuario que ingrese la fecha asignada para la cita por teclado y el ciclo se repite hasta que la fecha ingresada sea válida.
def validar_fecha():
    while True:
        fecha_texto = input("Ingrese la fecha asignada para la cita (formato DD/MM/AAAA): ")
        partes = fecha_texto.split("/")

        if len(partes) == 3:
            dia_texto = partes[0]
            mes_texto = partes[1]
            anio_texto = partes[2]

            if dia_texto.isdigit() and mes_texto.isdigit() and anio_texto.isdigit():
                dia = int(dia_texto)
                mes = int(mes_texto)
                anio = int(anio_texto)

                if mes >= 1 and mes <= 12:
                    if dia >= 1 and dia <= dias_en_mes(mes, anio):
                        fecha_ingresada = date(anio, mes, dia)
                        fecha_hoy = date.today()

                        # Para este punto tuve que buscar documentación en línea. Encontré que Python permite comparar fechas directamente con >= para saber si es hoy o una fecha futura. Esto con el fin de evitar que el usuario ingrese una fecha anterior a la fecha actual.
                        # Nota: Soy consciente de que esta validación permite fechas muy lejanas en el futuro (por ejemplo, años 2500 en adelante).
                        # Decidí no agregar un límite superior porque implicaría incluir una funcionalidad adicional no solicitada en el enunciado del taller.

                        if fecha_ingresada >= fecha_hoy:
                            return fecha_texto

        print()
        print("La fecha ingresada no es válida. Debe tener el formato DD/MM/AAAA, ser una fecha real, y no puede ser anterior al día de hoy. Por favor ingrese nuevamente la fecha asignada para la cita.")

# se crea la función que calcula el valor total a pagar por el cliente según el tipo de cliente, tipo de atención y cantidad.
def calcular_valor_total(tipo_cliente, tipo_atencion, cantidad):
    if tipo_cliente == "1":  # Particular
        valor_cita = 80000

        if tipo_atencion == "1":  # Limpieza
            valor_atencion = 60000
        else:
            if tipo_atencion == "2":  # Calzas
                valor_atencion = 80000
            else:
                if tipo_atencion == "3":  # Extracción
                    valor_atencion = 100000
                else:
                    valor_atencion = 50000  # Diagnóstico

    else:
        if tipo_cliente == "2":  # EPS
            valor_cita = 5000

            if tipo_atencion == "1":  # Limpieza
                valor_atencion = 0
            else:
                if tipo_atencion == "2":  # Calzas
                    valor_atencion = 40000
                else:
                    if tipo_atencion == "3":  # Extracción
                        valor_atencion = 40000
                    else:
                        valor_atencion = 0  # Diagnóstico

        else:  # Prepagada
            valor_cita = 30000

            if tipo_atencion == "1":  # Limpieza
                valor_atencion = 0
            else:
                if tipo_atencion == "2":  # Calzas
                    valor_atencion = 10000
                else:
                    if tipo_atencion == "3":  # Extracción
                        valor_atencion = 10000
                    else:
                        valor_atencion = 0  # Diagnóstico

    valor_total = valor_cita + (valor_atencion * cantidad)
    return valor_total

# Traduce el número de tipo de cliente a su nombre correspondiente.
def texto_tipo_cliente(tipo_cliente):
    if tipo_cliente == "1":
        return "Particular"
    else:
        if tipo_cliente == "2":
            return "EPS"
        else:
            return "Prepagada"

# Traduce el número de tipo de atención a su nombre correspondiente.
def texto_tipo_atencion(tipo_atencion):
    if tipo_atencion == "1":
        return "Limpieza"
    else:
        if tipo_atencion == "2":
            return "Calzas"
        else:
            if tipo_atencion == "3":
                return "Extracción"
            else:
                return "Diagnóstico"

# Traduce el número de prioridad a su nombre correspondiente.
def texto_prioridad(prioridad):
    if prioridad == "1":
        return "Normal"
    else:
        return "Urgente"

# Convierte la fecha de texto DD/MM/AAAA en un número AAAAMMDD para poder compararla.
def clave_fecha(fecha):
    # El texto DD/MM/AAAA no se ordena bien como texto ("10/01" < "02/12").
    # Se convierte a un número AAAAMMDD para poder comparar fechas.
    partes = fecha.split("/")
    return int(partes[2]) * 10000 + int(partes[1]) * 100 + int(partes[0])


# Ancho de las líneas que separan visualmente cada pantalla del menú.
ANCHO_LINEA = 60


# Muestra un título entre dos líneas de "=" para que cada resultado se distinga del anterior.
def imprimir_titulo(texto):
    print()
    print("=" * ANCHO_LINEA)
    print(texto)
    print("=" * ANCHO_LINEA)


# Línea de cierre al final de cada resultado.
def imprimir_cierre():
    print("=" * ANCHO_LINEA)


# Muestra todos los datos de un cliente, uno por línea y con las etiquetas alineadas.
def mostrar_cliente(cliente):
    print(f"  Nombre:            {cliente.nombre}")
    print(f"  Cédula:            {cliente.cedula}")
    print(f"  Teléfono:          {cliente.telefono}")
    print(f"  Tipo de cliente:   {texto_tipo_cliente(cliente.tipo_cliente)}")
    print(f"  Atención:          {texto_tipo_atencion(cliente.tipo_atencion)} (cantidad: {cliente.cantidad})")
    print(f"  Prioridad:         {texto_prioridad(cliente.prioridad)}")
    print(f"  Fecha de la cita:  {cliente.fecha_cita}")
    print(f"  Valor total:       ${cliente.valor_total:,.0f} pesos mcte.")


# Muestra un cliente en dos líneas (nombre y detalle) para las listas.
def mostrar_fila(posicion, cliente):
    print(f"{posicion}. {cliente.nombre}")
    print(f"   Cédula: {cliente.cedula}  |  {texto_tipo_atencion(cliente.tipo_atencion)}  |  Cita: {cliente.fecha_cita}  |  Valor total: ${cliente.valor_total:,.0f} pesos mcte.")
    print()



# SECCIÓN 5: CLASE CONSULTORIO (LAS COLAS)

class Consultorio:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_agenda = deque()     # Clientes agendados que no son extracción urgente
        self.cola_urgentes = deque()   # Extracciones urgentes

    def insertar_ordenado(self, cola, cliente):
        # Mete al cliente en la cola según la fecha asignada (la más cercana primero). Si hay empate de fecha, el nuevo queda después (se respeta el orden de llegada).
        auxiliar = []
        while cola:
            auxiliar.append(cola.popleft())

        clave_nueva = clave_fecha(cliente.fecha_cita)
        insertado = False
        for existente in auxiliar:
            if not insertado and clave_fecha(existente.fecha_cita) > clave_nueva:
                cola.append(cliente)
                insertado = True
            cola.append(existente)
        if not insertado:
            cola.append(cliente)

    def registrar_cliente(self, cliente):
        # Cada cliente vive en una sola cola.
        print()
        if cliente.tipo_atencion == "3" and cliente.prioridad == "2":
            self.insertar_ordenado(self.cola_urgentes, cliente)
            print("Cliente registrado en la cola de urgentes por extracción.")
        else:
            self.insertar_ordenado(self.cola_agenda, cliente)
            print("Cliente registrado en la agenda diaria.")

    # ---------- Agenda diaria ----------

    def atender_siguiente_agenda(self):
        if self.cola_agenda:
            cliente = self.cola_agenda.popleft()
            imprimir_titulo("ATENDIENDO AL SIGUIENTE CLIENTE (AGENDA DIARIA)")
            mostrar_cliente(cliente)
        else:
            imprimir_titulo("ATENDER SIGUIENTE CLIENTE (AGENDA DIARIA)")
            print("No hay clientes en la agenda.")
        imprimir_cierre()

    def consultar_siguiente_agenda(self):
        if self.cola_agenda:
            imprimir_titulo("SIGUIENTE CLIENTE (AGENDA DIARIA)")
            mostrar_cliente(self.cola_agenda[0])
        else:
            imprimir_titulo("SIGUIENTE CLIENTE (AGENDA DIARIA)")
            print("No hay clientes en la agenda.")
        imprimir_cierre()

    def listar_agenda(self):
        imprimir_titulo("AGENDA DIARIA")
        if not self.cola_agenda:
            print("No hay clientes en la agenda.")
            imprimir_cierre()
            return
        print()
        posicion = 0
        total_a_cobrar = 0
        for cliente in self.cola_agenda:
            posicion += 1
            total_a_cobrar = total_a_cobrar + cliente.valor_total
            mostrar_fila(posicion, cliente)
        print(f"Total de clientes en la agenda: {posicion}")
        print(f"Total a cobrar: ${total_a_cobrar:,.0f} pesos mcte.")
        imprimir_cierre()

    # ---------- Urgentes por extracción ----------

    def atender_siguiente_urgente(self):
        if self.cola_urgentes:
            cliente = self.cola_urgentes.popleft()
            imprimir_titulo("ATENDIENDO AL SIGUIENTE CLIENTE (URGENTE POR EXTRACCIÓN)")
            mostrar_cliente(cliente)
        else:
            imprimir_titulo("ATENDER SIGUIENTE CLIENTE (URGENTE POR EXTRACCIÓN)")
            print("No hay clientes urgentes por extracción.")
        imprimir_cierre()

    def consultar_siguiente_urgente(self):
        imprimir_titulo("SIGUIENTE CLIENTE (URGENTE POR EXTRACCIÓN)")
        if self.cola_urgentes:
            mostrar_cliente(self.cola_urgentes[0])
        else:
            print("No hay clientes urgentes por extracción.")
        imprimir_cierre()

    def reporte_urgentes(self):
        imprimir_titulo("REPORTE DE URGENTES POR EXTRACCIÓN (ordenados por fecha de cita)")
        if not self.cola_urgentes:
            print("No hay clientes urgentes por extracción.")
            imprimir_cierre()
            return
        print()
        total_clientes = 0
        total_a_cobrar = 0
        for cliente in self.cola_urgentes:
            total_clientes += 1
            total_a_cobrar = total_a_cobrar + cliente.valor_total
            print(f"{total_clientes}. {cliente.nombre}")
            print(f"   Cédula: {cliente.cedula}  |  Cita: {cliente.fecha_cita}  |  Valor total: ${cliente.valor_total:,.0f} pesos mcte.")
            print()
        print(f"Total de urgentes: {total_clientes}")
        print(f"Total a cobrar: ${total_a_cobrar:,.0f} pesos mcte.")
        imprimir_cierre()

    # ---------- Todos los clientes ----------

    def listar_todos(self):
        # Solo recorre las dos colas para mostrarlas; no mueve a nadie de lugar.
        imprimir_titulo("CLIENTES EN ESPERA")
        if not self.cola_urgentes and not self.cola_agenda:
            print("No hay clientes en espera.")
            imprimir_cierre()
            return
        total = 0
        total_a_cobrar = 0

        print()
        print("URGENTES POR EXTRACCIÓN")
        print("-" * ANCHO_LINEA)
        if not self.cola_urgentes:
            print("(ninguno)")
            print()
        for cliente in self.cola_urgentes:
            total += 1
            total_a_cobrar = total_a_cobrar + cliente.valor_total
            mostrar_fila(total, cliente)

        print("AGENDA DIARIA")
        print("-" * ANCHO_LINEA)
        if not self.cola_agenda:
            print("(ninguno)")
            print()
        for cliente in self.cola_agenda:
            total += 1
            total_a_cobrar = total_a_cobrar + cliente.valor_total
            mostrar_fila(total, cliente)

        print(f"Total de clientes en espera: {total}")
        print(f"Total a cobrar: ${total_a_cobrar:,.0f} pesos mcte.")
        imprimir_cierre()


# Registra un cliente desde el menú de control de citas y lo manda a la cola que le corresponde.
# Después de cada cliente pregunta si se desea registrar otro (S/N); con N se vuelve al menú de control de citas.
def registrar_cliente_desde_menu(consultorio):
    contador = 1
    seguir = True

    while seguir:
        imprimir_titulo(f"REGISTRO DE CLIENTE {contador}")
        print()

        cedula = validar_cedula()
        nombre = validar_nombre()
        telefono = validar_telefono()
        tipo_cliente = validar_tipo_cliente()
        tipo_atencion = validar_tipo_atencion()
        cantidad = validar_cantidad(tipo_atencion)
        prioridad = validar_prioridad()
        fecha_cita = validar_fecha()

        cliente_nuevo = Cliente(cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha_cita)
        cliente_nuevo.valor_total = calcular_valor_total(tipo_cliente, tipo_atencion, cantidad)
        consultorio.registrar_cliente(cliente_nuevo)
        contador = contador + 1

        respuesta_valida = False
        while respuesta_valida == False:
            print()
            respuesta = input("¿Desea registrar otro cliente? (S/N): ")

            if respuesta == "S" or respuesta == "s":
                respuesta_valida = True
                continuar = "S"
            else:
                if respuesta == "N" or respuesta == "n":
                    respuesta_valida = True
                    continuar = "N"
                else:
                    print("Respuesta inválida. Por favor responda S (sí) o N (no).")

        if continuar == "N":
            seguir = False


# Menú de control de citas: es lo primero que ve el usuario al iniciar el programa.
def leer_opcion():
    while True:
        opcion = input("Ingrese una opción (1-9): ")
        if opcion.isdigit() and 1 <= int(opcion) <= 9:
            return int(opcion)
        print("Opción inválida. Por favor ingrese un número entre 1 y 9.")


def menu_colas(consultorio):
    while True:
        print()
        print()
        print("=" * ANCHO_LINEA)
        print("CONTROL DE CITAS CONSULTORIO ODONTOLÓGICO")
        print("=" * ANCHO_LINEA)
        print("  1. Registrar cliente")
        print("  2. Listar todos los clientes (urgentes y agenda diaria)")
        print("  3. Reporte de urgentes por extracción")
        print("  4. Consultar siguiente cliente (urgente por extracción)")
        print("  5. Atender siguiente cliente (urgente por extracción)")
        print("  6. Listar agenda diaria")
        print("  7. Consultar siguiente cliente (agenda diaria)")
        print("  8. Atender siguiente cliente (agenda diaria)")
        print("  9. Salir")
        print("-" * ANCHO_LINEA)

        opcion = leer_opcion()

        if opcion == 1:
            registrar_cliente_desde_menu(consultorio)
        elif opcion == 2:
            consultorio.listar_todos()
        elif opcion == 3:
            consultorio.reporte_urgentes()
        elif opcion == 4:
            consultorio.consultar_siguiente_urgente()
        elif opcion == 5:
            consultorio.atender_siguiente_urgente()
        elif opcion == 6:
            consultorio.listar_agenda()
        elif opcion == 7:
            consultorio.consultar_siguiente_agenda()
        elif opcion == 8:
            consultorio.atender_siguiente_agenda()
        else:
            print()
            print("Programa finalizado.")
            break


# Programa principal: crea el consultorio y abre directamente el menú de control de citas.
if __name__ == "__main__":
    consultorio = Consultorio("Consultorio Odontológico")
    menu_colas(consultorio)