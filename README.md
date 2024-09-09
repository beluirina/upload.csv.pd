# upload.csv.pd
Use of Pandas, Numpy to practice upload of CSV file and Transformation of data. 
Uso de Pandas, Numpy para practicar subida de archivos CSV y la ELT de la data.

Consignas por archivos:
29082024
  
1.Leer los datos del archivo CSV en un DataFrame de Pandas.
2.Crear una clase Producto que contenga los atributos nombre, categoría, cantidad, y precio.
3.Crear una clase Inventario que permita agregar productos y calcular el valor total del inventario.
4.Implementar un método en Inventario que permita buscar un producto por nombre y manejar posibles errores.
5.Escribir un conjunto de pruebas unitarias para asegurarte de que las funciones funcionan correctamente.

03092024


1) Transformar las columnas de fechas para que tengan todas el mismo formato (datetime)
2) Reemplazar los valores nulos de las tablas por "no_definido"
3) En la tabla df_purchases Crear una variable que represente el rezago en dias de llegada de los productos pedidos.
4) En base a esa variable calcular la media, el maximo y el minimo de rezago por marca ('Brand')
5) En base a la tabla df_EndInv calcular cuantas unidades de cada marca quedaron
6) Filtrar los datos de las tablas df_sales y df_purchases para solo quedarme con info de Noviembre.
7) Combinar las tablas filtradas por el mes de noviembre df_sales y df_purchases. Joinear utilizando las columnas ['InventoryId', 'Store', 'Brand', 'Size'].
