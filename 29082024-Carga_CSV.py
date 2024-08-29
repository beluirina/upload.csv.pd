import pandas as pd


#1.Leer los datos del archivo CSV en un DataFrame de Pandas.
df = pd.read_csv(r'C:\Users\BelénJessikowski\Downloads\curso.python\trial.csv')
#Producto: Nombre del producto.
#Categoría: Categoría a la que pertenece el producto.
#Cantidad: Cantidad disponible en stock.
#Precio: Precio unitario del producto.
trail_object = []

#the way i did it before would treat each column as a singe df and append it to a list of diccionaries, each column is treated as a separate element in the list
for index, row in df.iterrows():
    trail_object.append({
            "Producto": row["Producto"],
            "Categoria": row["Categoría"],
            "Cantidad": row["Cantidad"],
            "Precio": row["Precio"]
        })
constructed_df = pd.DataFrame(trail_object)

#2.Crear una clase Producto que contenga los atributos nombre, categoría, cantidad, y precio.
class Producto:
    def __init__(self, Producto, categoría, cantidad, precio):
        self.Producto=Producto
        self.categoria=categoría
        self.cantidad=cantidad
        self.precio=precio
#3.Crear una clase Inventario que permita agregar productos y calcular el valor total del inventario.

    def to_dict(self):
        return{
            'Producto': self.Producto,
            'Categoria': self.categoria,
            'Cantidad': self.cantidad,
            'Precio': self.precio
        }
    
#Empezamos a crear una instancia de un nuevo producto para agregar 
new_prd = Producto(Producto='parlante', categoría='electronica', cantidad=3 , precio=300)

#convertir la instancia a dicc, y de ahi a DF
new_prd_toDF = pd.DataFrame([new_prd.to_dict()])
#concat ambos DF ignorando index
df = pd.concat([constructed_df, new_prd_toDF], ignore_index=True)
print(df)

#4.Implementar un método en Inventario que permita buscar un producto por nombre y manejar posibles errores.


#5.Escribir un conjunto de pruebas unitarias para asegurarte de que las funciones funcionan correctamente.

