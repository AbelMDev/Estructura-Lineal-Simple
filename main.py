class Persona:
    def __init__(self, nombre, edad, ciudad_residencia, lugar_trabajo, profesion, pasatiempo, color_favorito):
        self.nombre = nombre
        self.edad = edad
        self.ciudad_residencia = ciudad_residencia
        self.lugar_trabajo = lugar_trabajo
        self.profesion = profesion
        self.pasatiempo = pasatiempo
        self.color_favorito = color_favorito

    def imprimir_historia(self):
        print(f"¡Hola, {self.nombre}! Tienes {self.edad} años y vives en {self.ciudad_residencia}.")
        print(f"Trabajas en {self.lugar_trabajo} como {self.profesion}.")
        print(f"Tu pasatiempo favorito es {self.pasatiempo} y tu color favorito es {self.color_favorito}.")
        print(f"Un día, {self.nombre} decidió usar su talento como {self.profesion} para ayudar a su comunidad en {self.ciudad_residencia}.")
        if self.edad < 18:
            print("Aún eres joven, ¡sigue aprendiendo cosas nuevas!")
        else:
            print("Ya eres adulto, sigue cumpliendo tus metas.")
        print(f"En 5 años tendrás {self.edad + 5} años. ¡Sigue adelante!")

if __name__ == "__main__":
    nombre = input("Inserte su nombre: ")
    edad = int(input("Inserte su edad: "))
    ciudad_residencia = input("Inserte su ciudad de residencia: ")
    lugar_trabajo = input("Inserte su lugar de trabajo: ")
    profesion = input("Inserte su profesión: ")
    pasatiempo = input("Inserte su pasatiempo favorito: ")
    color_favorito = input("Inserte su color favorito: ")

    persona = Persona(nombre, edad, ciudad_residencia, lugar_trabajo, profesion, pasatiempo, color_favorito)
    persona.imprimir_historia()
