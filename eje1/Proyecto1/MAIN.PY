import math

class CalculadoraAreas:
    """Clase principal que contiene los métodos de cálculo."""
    
    def area_cuadrado(self, lado):
        return lado ** 2

    def area_rectangulo(self, base, altura):
        return base * altura

    def area_circulo(self, radio):
        return math.pi * (radio ** 2)

    def area_triangulo(self, base, altura):
        return (base * altura) / 2

def menu():
    calc = CalculadoraAreas()
    
    while True:
        print("\n--- Calculadora de Áreas ---")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Círculo")
        print("4. Triángulo")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            l = float(input("Introduce el lado: "))
            print(f"El área es: {calc.area_cuadrado(l):.2f}")
        elif opcion == '2':
            b = float(input("Introduce la base: "))
            h = float(input("Introduce la altura: "))
            print(f"El área es: {calc.area_rectangulo(b, h):.2f}")
        elif opcion == '3':
            r = float(input("Introduce el radio: "))
            print(f"El área es: {calc.area_circulo(r):.2f}")
        elif opcion == '4':
            b = float(input("Introduce la base: "))
            h = float(input("Introduce la altura: "))
            print(f"El área es: {calc.area_triangulo(b, h):.2f}")
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()