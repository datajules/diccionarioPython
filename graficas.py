import matplotlib.pyplot as plt

# Datos
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 
         'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 
         'Noviembre', 'Diciembre']
ventas_mensuales = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]

# Gráfica de barras
# plt.bar(meses, ventas_mensuales, color='#A60303')
# plt.title('Ventas mensuales')
# plt.xlabel('Meses')
# plt.ylabel('Ventas')
# plt.grid(True)
# plt.show()

#Gráfica de pastel
data = [20,30,10,40]
etiqueta = ['manzana','pera','mango','fresa']
colores = ['#82B0D9','#D2D904','#F29F05','#F20505']

plt.pie(data, labels=etiqueta, colors=colores)
plt.title('Ventas mensuales de frutas')
plt.show() 
