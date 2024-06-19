#https://github.com/SaMii0108/samantha_munizaga_prueba3.git#
import csv
def categoria(puntos):
    if puntos>=0 and puntos<=40:
        cal="Amateur"
        return cal
    if puntos>=81 and puntos<=120:
        cal="Avanzado"
        return cal
    if puntos>120:
        cal="Idolos"
        return cal
def confirmar():
    resp=input("Esta seguro que quiere modificarlo ? (si/no)").lower()
    if resp=="si":
        return True
    else:
        return False
    
def mod(act,listita):
     for x in listita:
            if act==x['id_e']:
                nom_c=input("Ingrese nuevo nombre:")
                r=confirmar()
                if r==True:
                    listita['nombre']=nom_c
                elif r:
                    print("no se cambio el nombre del equipo")
def promedio():
    acum=0
    cant=len(lista)
    if cant>0:
        for x in lista:
            acum=acum+int(x['puntos'])
        prom=acum/cant
        print("El promedio de puntos es :",prom)
def mayor():
    mayor=0
    for x in lista:
        if int(x['puntos'])>int(mayor):
            mayor=int(x['puntos'])
        else:
            mayor=mayor
    print ("El puntaje mas alto es :",mayor)   
       
                
diccionario={}
lista=[]
while True:
    print ("")
    print ("-.-.-.-.-.M E N U  E Q U I P O S-.-.-.-")
    print ("")
    print ("1-Agregar equipo")
    print ("2-Listar equipo")
    print ("3-Actualizar nombre de quipo por id")
    print ("4-Generar BBDD")
    print ("5-Cargar BBDD")
    print ("6-Estadisticas")
    print ("0-Salir")
    print ("")
    op=int(input("Ingrese una opcion: \n"))
    if op==1:
        print ("")
        id_e=int(input("Ingrese id del equipo: \n"))
        nombre=input("Ingrese nombre del equipo :\n")
        puntos=int(input("Ingrese cantidad de puntos :\n"))
        calificar=categoria(puntos)
        diccionario={'id_e':id_e,'nombre':nombre,'puntos':puntos,'categoria':calificar}
        lista.append(diccionario)
        print ("")        
    elif op==2:
        print ("")
        print (".-.-.-.-.-L I S T A D O  D E  E Q U I P O S.-.-.-.-")
        for x in lista:
            print ("ID :",x['id_e'],"NOMBRE DEL EQUIPO :",x['nombre'],"PUNTOS :",x['puntos'],"CATEGORIA:",x['categoria'])
    elif op==3:
        print ("")        
        actualizar=int(input("Ingrese id del equipo a actualizar"))
        mod(actualizar,lista)
        print("")           
                
    elif op==4:
        print ("")
        with open ('bbdd.csv','w',newline='') as bbdd:
            campos=['id_e','nombre','puntos','categoria']
            escritor=csv.DictWriter(bbdd,fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(lista)            
    elif op==5:
        print ("")
        with open ('bbdd.csv','r',newline='') as bbdd:
            lector =csv.DictReader(bbdd)
            for fila in lector:
                lista.append(fila)
    elif op==6:
        print ("")
        promedio()
        mayor()
    elif op==0:
        print ("")
        print ("Saliendo....")
        print ("Adios.")
    else:
        print ("")
        print ("Ingrese una opcion valida ")
    
        
