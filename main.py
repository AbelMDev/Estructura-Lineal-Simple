class Persona:
    def __init__(self, nombre, edad, ciudad_residencia, lugar_trabajo, profesion):
        self.nombre = nombre
        self.edad = edad
        self.ciudad_residencia = ciudad_residencia
        self.lugar_trabajo = lugar_trabajo
        self.profesion = profesion
        
    def imprimir_saludo(self) -> str:
        print(f"¡Hola, {self.nombre}! Tienes {self.edad} años y vives en {self.ciudad_residencia}, tu profesión es {self.profesion} y trabajas en {self.lugar_trabajo}.")
        
if __name__ == "__main__":
    nombre = input("Inserte su nombre: ")
    edad = int(input("Inserte su edad: "))
    ciudad_residencia = input("Inserte su ciudad de residencia: ")
    lugar_trabajo = input("Inserte su lugar de trabajo: ")
    profesion = input("Inserte su profesión: ")
    
    new_persona = Persona(nombre, edad, ciudad_residencia, lugar_trabajo, profesion)
    new_persona.imprimir_saludo()
