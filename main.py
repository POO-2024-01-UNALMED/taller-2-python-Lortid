class Asiento:

    def __init__(self, color, precio, registro) :

        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color_auto):

        list = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']
        
        if color_auto in list:

            self.color= color_auto

class Motor :

    def __init__(self, numeroCilindros, tipo, registro) :

        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro (self, registro_auto):

        self.registro = registro_auto

    def asignarTipo (self, tipo_auto):

        if tipo_auto == 'electrico' or tipo_auto == 'gasolina' :

            self.tipo = tipo_auto

class Auto :

    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro ):

        self.modelo = modelo
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.precio = precio

    def cantidadAsientos(self):

        numAsientos = 0

        for i in range(0, len(self.asientos)):

            if isinstance(self.asientos[i], Asiento):

                numAsientos +=1

        return numAsientos

    def verificarIntegridad (self):

        lista = []
        a = 0

        if self.motor.registro == self.registro :
            
            for j in range(0, len(self.asientos)):
                
                if isinstance(self.asientos[j], Asiento):
                    
                    lista.append(self.asientos[j])
                
            for x in range(0, len(lista)-1):
                
                if lista[x].registro == lista[x+1].registro:
                    
                    a+=1
                    
                
                if a == len(lista)-1:
                    
                    return "Auto original"
                
                else :
                    return "Las piezas no son originales"
                

        else :
            
            return "Las piezas no son originales"