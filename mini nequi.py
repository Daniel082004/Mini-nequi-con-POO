
class nequi:
    
    def registro(self):
        
        print("<<<REGISTRESE>>>")
        
        self.nombres = str(input("Escriba su nombre: "))
        self.apellidos = str(input("Escriba su apellido: "))
        self.telefono = int(input("Escriba su numero de telefono: "))
        self.edad = int(input("Escriba su edad: "))
        self.contraseña = int(input("Cree una contraseña: "))
        
        if self.edad < 18:
            print("Lo siento, debe de ser mayor de edad para poderse registrarse ")
            exit()
        else:
            print("<<Registro Exitoso>> ")

class entrar:
    
    def ingreso(self):
        
        print("---------------------------")
        print("<<BIENVENIDO>>")
        print("   INGRESE ")
        
        contador = 1
        while contador <= 3:
            usuario = int(input ("Telefono: "))
            contraseña = int(input ("Clave: "))
            if usuario == self.telefono and contraseña == self.contraseña:
                print ("Cargando.... ")
                print("----------------------------------")
                contador = 4
            else:
                print ("Contraseña o usuario incorrectos, intentalo de nuevo")
                if contador == 3:
                    print("---------------------------")
                    print ("<<Sistema bloqueado>>")
                    exit()
                contador = contador + 1
                
class mostrar(nequi,entrar):
    
    def datos(self):
        
        print("<<Bienvenido "f"{self.nombres}>>")
        saldo = 0
        print("el saldo de su cuenta es: ","$",saldo)
        print("------------------------------------------------")
        print("¿desea recargar su cuenta? ")
        print("")
        print("1) si")
        print("2) no")
        print("")
        recargar = int(input("Eliga una opcion >>> "))
        print("------------------------------------------------")
            
        if recargar == 1:
            consignar = int(input("Escriba la cantidad de dinero que quiere consignar: "))
            total = consignar + saldo
            print("<<Consignacion Exitosa, su saldo actual es de $"f"{total}>>")
            print("------------------------------------------------")
            print("<<<¿Que desea hacer?>>>")
            print("------------------------------------------------")
            print("<<<¿Guardar el dinero?>>>")
            print("")
            print("1) Cuenta de ahorro ")
            print("2) Bolsillo ")
            print("------------------------------------------------")
            print("<<<¿Retirar o enviar?>>>")
            print("")
            print("3) Retirar")
            print("4) Enviar plata ")
            print("------------------------------------------------")
            print("5) salir ")
            print("------------------------------------------------")
            ahorro = int(input("Eliga una opcion: "))
            print("------------------------------------------------")
            
            if ahorro == 1:
                print("Cuenta de ahorro #001")
                print("Saldo: ","$",saldo)
                guardar = int(input(("¿Cuanto desea consignar en su cuenta de ahorro? recuerde que el saldo disponible es:",consignar)))
                if guardar <= consignar:
                    print("------------------------------------------------------------------------------------")
                    print("Consignacion realizada con exito, su saldo en su cuenta de ahorro #001 es: $",guardar)
                    print("Saldo disponible ",consignar-guardar)
                    print("Gracias por usar nuestra app, vuelva pronto ")
                    print("------------------------------------------------------------------------------------")
                    exit()
                else:
                    if guardar > consignar:
                        print("Saldo insuficiente, no es posible consignar el valor deseado")
                        exit()
            if ahorro == 2:
                print("Bienvenido al bosillo")
                print("saldo: ","$",saldo)
                bolsillo = int(input(("¿Cuanto desea consignar en su bolsillo? recuerde que el saldo disponible es:",consignar)))
                if bolsillo <= consignar:
                    print("------------------------------------------------------------------------------------")
                    print("Consignacion realizada con Exito, el saldo en su bolsillo es: $",bolsillo)
                    print("Saldo disponible: ",consignar-bolsillo)  
                    print("Gracias por usar nuestra app, vuelva pronto")
                    print("------------------------------------------------------------------------------------")
                    exit()
                else:
                    if bolsillo > consignar:
                        print("Saldo insuficiente, no es posible consignar el valor deseado")
                        exit() 
            if ahorro == 3:
                print("¿Cuanto desea retirar?: ")
                print("Saldo disponible ","$",consignar)
                retiro = int(input("$ = "))
                if retiro <= consignar:
                    print("------------------------------------------")
                    print("retiro exitoso, su retiro fue de: ","$",retiro)
                    print("Gracias por usar nuestra app, vuelva pronto")
                    print("saldo disponible: $",retiro-consignar)
                    print("------------------------------------------")
                    exit()
                else:
                    if retiro > consignar:
                        print("¡Fondos insuficientes! ")
                        exit()
            if ahorro == 4:
                print("<<<ENVIOS>>>")
                nombre = str(input("Nombre a quien se le enviara el dinero: "))
                cel = int(input("telefono a donde se le consignara el dinero: "))
                print("Saldo disponible ","$",consignar)
                valor = int(input("valor: $"))
                if valor <= consignar:
                    print("------------------------")
                    print("<<<Envio Exitoso>>>")
                    print("-Nombre: ",nombre)
                    print("-Telefono: ",cel)
                    print("-Valor: ","$",valor)
                    print("------------------------")
                    print("Gracias por usar nuestra app, vuelva pronto ")
                    exit()
                else: 
                    if valor > consignar:
                        print("¡Fondos insuficientes!")
                        exit()
            if ahorro == 5:
                print("Gracias por usar nuestra app, vuelva pronto")
                exit()  
        else:
            if recargar == 2:
                print("Gracias por usar nuestra app, vuelva pronto")
                exit()                         
x = mostrar()
x.registro()
x.ingreso()
x.datos()


