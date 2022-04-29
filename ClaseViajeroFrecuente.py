class ViajeroFrecuente:
    __num_viajero= 0
    __dni= ""
    __nombre=""
    __apellido=""
    __millas_acum= 0

    def __init__(self, n_v, doc, nom, apell, mill):
        self.__num_viajero = n_v
        self.__dni = doc
        self.__nombre=nom
        self.__apellido=apell
        self.__millas_acum= int (mill)

    def cantidadTotalMillas(self) :
        return self.__millas_acum

    def acumularMillas(self, mill):
           self.__millas_acum += int(mill)



    def canjearMillas(self, canjear):
        if(int(canjear)<=self.__millas_acum):
            self.__millas_acum-= int(canjear)
            print("Canje realizado con exito.")
        else:
            print("No se pudo canjear millas")

    def getnum_viajero(self):
        return self.__num_viajero

    def __str__(self):
        return "%s %s %s %s %d"% (self.__num_viajero, self.__dni, self.__nombre, self.__apellido,self.__millas_acum)


