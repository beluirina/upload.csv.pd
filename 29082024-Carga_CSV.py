
#1.Leer los datos del archivo CSV en un DataFrame de Pandas.
#2.Crear una clase Producto que contenga los atributos nombre, categoría, cantidad, y precio.
#3.Crear una clase Inventario que permita agregar productos y calcular el valor total del inventario.
#4.Implementar un método en Inventario que permita buscar un producto por nombre y manejar posibles errores.
#5.Escribir un conjunto de pruebas unitarias para asegurarte de que las funciones funcionan correctamente.

df = pd.read_csv(r'C:\Users\BelénJessikowski\Downloads\curso.python\trial.csv')
#Producto: Nombre del producto.
#Categoría: Categoría a la que pertenece el producto.
#Cantidad: Cantidad disponible en stock.
#Precio: Precio unitario del producto.
trail_object = []

trail_object.append({
            "Producto": df["Producto"],
            "Categoria": df["Categoría"],
            "Cantidad": df["Cantidad"],
            "Precio": df["Precio"]
        })
df = pd.DataFrame(trail_object)

#Tu tarea es:
print(df)
class Empleado:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado:")
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)
 
