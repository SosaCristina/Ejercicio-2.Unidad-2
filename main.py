from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

if __name__=="__main__":
    lista=[]
    archivo=open("ListaViajero.csv")
    reader=csv.reader(archivo,delimiter=";")
    for fila in reader:
        num_viajero= int(fila[0])
        dni= fila[1]
        nombre=fila[2]
        apellido=fila[3]
        millas_acum= fila[4]
        unViajero=ViajeroFrecuente(num_viajero,dni,nombre,apellido,millas_acum)
        lista.append(unViajero)
        print(unViajero)

    archivo.close()



    opcion= 0
    def menu():
        opc= int(input("Menu Principal\n" +
                      "1)Consultar cantidad de millas\n" +
                      "2)Acumular millas\n" +
                      "3)Canjear millas\n" +
                      "4)Finalizar\n" +
                      "Elija una opcion\n"))
        return opc
    while opcion!=4:
        opcion=menu()

        if opcion == 1:
           print("Ingresar numero de viajero")
            numero=int(input())
            i=0
            while i< len(lista) and numero!= lista[i].getnum_viajero():
                i+=1
            if i<=len(lista):
                print("La cantidad de millas es:", lista[i].cantidadTotalMillas())



        if opcion==2:
            print("Ingresar numero de viajero")
            numero=int(input())
            i=0
            while i< len(lista) and numero!= lista[i].getnum_viajero():
                i+=1
            if i<=len(lista):
                    mill=int(input("Ingresar cantidad de millas para acumular"))
                    lista[i].acumularMillas(mill)
                    print("Millas actualizadas:",lista[i].cantidadTotalMillas())


        if opcion == 3:
            print("Ingresar numero de viajero")
            numero=int(input())
            i=0
            while i< len(lista) and numero!= lista[i].getnum_viajero():
                i+=1
            if i<=len(lista):
                    canjear=int(input("Ingresar cantidad de millas para canjear"))
                    lista[i].canjearMillas(canjear)
                    print("Millas actualizadas, con canje realizado:",lista[i].cantidadTotalMillas())




