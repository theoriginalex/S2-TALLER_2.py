


nombres = input("Ingrese sus nombres y apellidos ")
cargo = input("Ingrese su cargo")
bono = input("Ingrese la categoria del bono")
pago = input("Ingrese el tipo de mecanismo de pago")
print(f"sus nombres son: {nombres}")

# 1-------------------------------------------------------------------

if cargo == "director":
    sueldo = 2500
    print(f"el sueldo es {sueldo}")
    if bono == "categoria1":
        de = 0.09
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 9% es :{bon} ")
    if bono == "categoria2":
        de = 0.06
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 6% es :{bon} ")
    if bono == "categoria3":
        de = 0.03
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 3% es :{bon} ")
    if sueldo > 1300:
        de = 0.08
        desc = de * sueldo
        sueldo = sueldo - desc
        print(f"el descuento del 8% es: {desc} ")
    if pago == "transferencia":
        de = 0.01
        desc = de * sueldo
        sueldo = sueldo - desc
        print(f"el descuento por transferencia es de: {desc} ")

    print(f"el sueldo total es: {sueldo}")

# 2-------------------------------------------------------------------

if cargo == "especialista":
    sueldo = 1800
    print(f"el sueldo es: {sueldo}")

    if bono == "categoria1":
        de = 0.09
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 9% es :{bon}")

    if bono == "categoria2":
        de = 0.06
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 6% es :{bon} ")

    if bono == "categoria3":
        de = 0.03
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 3% es :{bon}")

    if sueldo > 1300:
        de = 0.08
        desc = de * sueldo
        sueldo = sueldo - desc
        print(f"el descuento del 8% es: {desc}")

    if pago == "transferencia":
        de = 0.01
        desc = de * sueldo
        sueldo = sueldo - desc

    print(f"el sueldo total es: {sueldo}")

# 3----------------------------------------------------------------------

if cargo == "analista":
    sueldo = 1200
    print(f"el sueldo es: {sueldo}")

    if bono == "categoria1":
        de = 0.09
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 9% es :{bon} ")

    if bono == "categoria2":
        de = 0.06
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 6% es :{bon} ")

    if bono == "categoria3":
        de = 0.03
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 3% es :{bon}")

    if sueldo > 1300:
        de = 0.08
        desc = de * sueldo
        sueldo = sueldo - desc
        print(f"el descuento del 8% es: {desc}")

    if pago == "transferencia":
        de = 0.01
        desc = de * sueldo
        sueldo = sueldo - desc

    print(f"el sueldo total es: ${sueldo}")

# 4-------------------------------------------------------------------


if cargo == "asistente":
    sueldo = 900
    print(f"el sueldo es: ${sueldo}")

    if bono == "categoria1":
        de = 0.09
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 9% es :{bon}")

    if bono == "categoria2":
        de = 0.06
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 6% es :{bon}")

    if bono == "categoria3":
        de = 0.03
        bon = de * sueldo
        sueldo = bon + sueldo
        print(f"el bono del 3% es :{bon} ")

    if sueldo > 1300:
        de = 0.08
        desc = de * sueldo
        sueldo = sueldo - desc
        print(f"el descuento del 8% es: ${desc}")

    if pago == "transferencia":
        de = 0.01
        desc = de * sueldo
        sueldo = sueldo - desc

    print(f"el sueldo total es: ${sueldo}")