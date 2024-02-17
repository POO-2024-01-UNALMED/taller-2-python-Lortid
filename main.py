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

        if self.motor.registro == self.registro :
            
            for j in range(0, len(self.asientos)):
                
                if isinstance(self.asientos[j], Asiento):
                
                    if self.asientos[j].registro == self.asientos[j+1].registro:
                
                        return "Auto original"
                
                    else:
                    
                        return "Las piezas no son originales"
            
        else :
            
            return "Las piezas no son originales"


if __name__ == "__main__":

    a1 = Auto("model 3", 33000, [Asiento("blanco", 5000, 30), None ,Asiento("blanco", 5000, 32)],
    "tesla", Motor(4, "electrico", 32), 32)

print(a1.verificarIntegridad())
