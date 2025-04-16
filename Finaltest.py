def validar_email(email):
    if len(email) > 25:
        print("El email no puede contener más de 25 caracteres")
        return False
    if '@' not in email:
        print("El email debe contener el signo de @")
        return False
    partes = email.split('@')
    if len(partes) != 2 or partes[0] == '' or partes[1] == '':
        print("El email debe contener un nombre de usuario y un dominio")
        return False
    if partes[0] == '':
        print("El email debe contener un nombre de usuario")
        return False
    if partes[1] == '':
        print("El email debe contener un dominio")
        return False
    return True
def main():
    while True:
        email = input("Ingrese su email: ")
        
        if validar_email(email):
            print("Gracias por ingresar correctamente su email.")
            break
if __name__ == "__main__":
    main()