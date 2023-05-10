def calcular_edad(an):
    e = 2023 - an
    return e

def mayor_de_edad(e):
    m = False
    if e >= 18:
        m = "Mayor de edad"
    else:
        m = "menor de edad"
    return m
def generar_correo(n,a,p):
    for x in a:
        p += remplazar_caracteres(x)
        a = p


    n = n.strip()
    a = a.strip()
    correo = remplazar_caracteres(n[0].lower())
    x =  a.split()
    #primer apellido
    correo += x[0].lower()
    #primera letra del segundo apellido
    correo += remplazar_caracteres(x[1][0].lower())
    correo += "@unemi.edu.ec"
    return correo


def remplazar_caracteres(l):
    r = l
    if l == "ñ":
        r = "n"
    elif l =="à":
        r = "a"
    elif l == "è":
        r = "e"
    elif l == "ì":
        r = "i"
    elif l == "ò":
        r = "o"
    elif l == "ù":
        r = "u"
    return r

#def generar_contrasena():
    #pass
def run():
    nombres = input("ingrese sus nombres: ")
    apellidos = input("ingrese sus apellidos : ")
    anio_nacimiento = int(input("Imgrese su año de nacimiento"))
    edad = calcular_edad(anio_nacimiento)
    tipo_edad = mayor_de_edad(edad)
    correo = generar_correo(nombres,apellidos)
    #contrasena =  generar_contrasena()


    print(f"La edad de {nombres} es {edad}, es una persona {tipo_edad} su cuenta de correo generado es: {correo}")



#if_name== "__main_":

run()
