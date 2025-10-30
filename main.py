class Persona:
    def __init__(self, nombre, edad, ciudad_residencia):
        self.nombre = nombre
        self.edad = edad
        self.ciudad_residencia = ciudad_residencia
        
    def imprimir_saludo(self) -> str:
        print(f"¡Hola, {self.nombre}! Tienes {self.edad} años y vives en {self.ciudad_residencia}.")
        
if __name__ == "__main__":
    nombre = input("Inserte su nombre: ")
    edad = int(input("Inserte su edad: "))
    ciudad_residencia = input("Inserte su ciudad de residencia: ")
    
    new_persona = Persona(nombre, edad, ciudad_residencia)
    new_persona.imprimir_saludo()
