usuarios = {}


def registrar_usuario():
    nombreUsuario = input ("Ingrse un nombre de usuario: ")
    if nombreUsuario in usuarios:
        print ("El usuario ya existe. Intente con otro nombre de usuario. ")
    else: 
        contraseña = input ("Ingrese una contraseña: ")
        usuarios[nombreUsuario] = contraseña
        print ("Usuario registrado con exito!")

def iniciar_sesion(): 
    nombreUsuario = input ("ingrese su nombre su nombre de usuario: ")
    contraseña =  input("Ingrese su contraseña: ")

    if nombreUsuario in usuarios and usuarios [nombreUsuario] == contraseña:
        print("Inicio de sesion exitoso. ¡Bienvenido", nombreUsuario "!")

    else: 
        print("Credenciales incorrectas. Intente nuevamente.")

def menu():
    '''
==================================================
================== BIENVENIDO ====================
=            1. Registrarse                      =
=            2. Iniciar Sesion                   =
=            3. Salir                            =
==================================================
    '''
while True: 
    menu()

    opcion = input("Seleccione una opcion: ")

    if opcion == 1:
        registrar_usuario()

    elif opcion == 2:
        iniciar_sesion()
    
    elif opcion == 3:
        break
    else: 
        print("Opcion invalida, por favor intente nuevamente")