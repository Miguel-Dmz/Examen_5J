print("***** Examen Miguel Dominguez 1173 ***** \n")
# zona de clases
class Inventario1173:
        
# LISTAS
    print("***** Listas ***** \n")
    def lista_zapateria_1173(self):
        Tipo_calzado_1173 = ["tenis de futbol","tenis para correr","zapatos casuales",
                            "tenis de basquetball", "botas vaqueras", "chanclas"]
        print(Tipo_calzado_1173)
        for y in Tipo_calzado_1173:
            print(y)
        print("\n")

# TUPLAS
    def tupla_zapateria_1173(self):
        print("***** Tuplas ***** \n")
        ## esto se refiere a la cantidad de pares de calzados que se necesita para una sucursal
        Cantidad_necesaria_1173 = ("120 pares", "60 pares", "200 pares","50 pares", "40 pares", "100 pares","250 pares")
        print(Cantidad_necesaria_1173)
        for a in Cantidad_necesaria_1173:
            print(a)
        print("\n")

# CONJUNTOS
    def diccionario_zapateria_1173(self):
        print("***** Diccionarios ***** \n")
        ## esto se refiere al precio que tiene cada calzado
        P_calzado_1173 = {
        "tenis de futbol-":450, "tenis para correr-":400,
        "zapatos casuales-":450 ,"tenis de basquetball-":800,
        "botas vaqueras-":1500,"chanclas-":200,
        "botas de lluvia-":300
        } 
        print(P_calzado_1173)
        for b, z in P_calzado_1173.items():
            print(b,z)
        print("\n")

# SETS
    def sets_zapateria_1173(self):
        print("***** Sets ***** \n")
        ## esto se refiere a la capacidad maxima de calzados que puede tener una susucrsal
        Capacidad_max_1173 = {"3500 pares","4005 pares","4500 pares","1620 pares", "1500 pares", "2020 pares", "3000 pares"}
        print(Capacidad_max_1173)
        for c in Capacidad_max_1173:
            print(c)

# utilizacion del objeto
x = Inventario1173 ()
x.lista_zapateria_1173()
x.tupla_zapateria_1173()
x.diccionario_zapateria_1173()
x.sets_zapateria_1173()