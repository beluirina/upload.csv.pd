'''
Tener en cuenta que este codigo fue originalmente desarrollado en un notebook ipynb por lo cual hubo uso de celdas para la ejecucion del codigo, el cual en un archivo py puede ser poco intuitivo.

'''
#1) Transformar las columnas de fechas para que tengan todas el mismo formato (datetime)

#2) Reemplazar los valores nulos de las tablas por "no_definido"

#3) En la tabla df_purchases Crear una variable que represente el rezago en dias de llegada de los productos pedidos.

#4) En base a esa variable calcular la media, el maximo y el minimo de rezago por marca ('Brand')

#5) En base a la tabla df_EndInv calcular cuantas unidades de cada marca quedaron

#6) Filtrar los datos de las tablas df_sales y df_purchases para solo quedarme con info de Noviembre.

# 7) Combinar las tablas filtradas por el mes de noviembre df_sales y df_purchases. Joinear utilizando las columnas ['InventoryId', 'Store', 'Brand', 'Size'].
import pandas as pd
import numpy as np

base_path = r'C:\Users\BelénJessikowski\Downloads\curso.python\input files'

preciosDeCompra_dir = r"\2017PurchasePricesDec.csv"
beginInv_dir = r'\BegInvFINAL12312016.csv'
endInv_dir = r'\EndInvFINAL12312016.csv'
purchases_dir = r'\PurchasesFINAL12312016.csv'

sales_dir = r'\SalesFINAL12312016.csv'
file_id_invoice = r"\InvoicePurchases12312016.csv"


df_PurchasePrices = pd.read_csv(base_path + preciosDeCompra_dir)  
df_BeginInv = pd.read_csv( base_path + beginInv_dir) 
df_EndInv = pd.read_csv( base_path +  endInv_dir) 
df_purchases = pd.read_csv( base_path +  purchases_dir) 
df_sales = pd.read_csv( base_path + sales_dir) 
df_invoice = pd.read_csv( base_path + file_id_invoice)

df_PurchasePrices.head()
##1) Transformar las columnas de fechas para que tengan todas el mismo formato (datetime)
def format_date(df, column, separator):
    try:
        df[column] = pd.to_datetime(df[column], format=f"%Y{separator}%m{separator}%d")
        df[column] = df[column].dt.strftime("%d-%m-%Y")
    except ValueError:
        print('there is a value error ')


#2) Reemplazar los valores nulos de las tablas por "no_definido"
def ifnaValues (df):
    test = df.isnull().values.any()
    if test == True:
            print(f'there ARE null values')
            df.fillna("no_definido", inplace=True)
    else:
          print(f' has NO null values')
    
    return df.head()

ifnaValues(df_BeginInv)
ifnaValues(df_EndInv)
ifnaValues(df_invoice)

ifnaValues(df_PurchasePrices)
ifnaValues(df_purchases)
ifnaValues(df_sales)

#    "no_definido"
df_BeginInv.head()

df_EndInv.head()

format_date(df_purchases, "ReceivingDate", '-')
format_date(df_purchases, "InvoiceDate", '-')
format_date(df_purchases, "PayDate", '-')
df_purchases.head()

#3) En la tabla df_purchases Crear una variable que represente el rezago en dias de llegada de los productos pedidos.

format_date(df_sales, 'SalesDate', '/')
df_sales.head()

format_date(df_invoice, 'PayDate', '-')
format_date(df_invoice, 'PODate', '-')
format_date(df_invoice, 'InvoiceDate', '-')
df_invoice.head()


