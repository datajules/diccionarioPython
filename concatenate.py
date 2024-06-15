# Cadenas de texto(
#print('Hola' + ' ' + 'Mundo')

texto1 = 'Hola '
texto2 = 'Mundo'

texto_completo = texto1 + texto2

print(texto_completo)

texto1 = 'Yo tengo '
texto2 = str(2) + ' manos'

texto_completo = texto1 + texto2

print(texto_completo)

print('-'.join(['Cómo', 'estás', 'hoy']))

#nombre = input(f"¿Cómo te llmas?")

#edad = input(f"¿Cuántos años tienes?")

#print(f"Hola {nombre}, tienes {edad} años")

milista1 = [1,2,3]
milista2 = [4,5,6]

milistafinal = milista1 + milista2

print(milistafinal)

milista1.extend(milista2)

print(milista1)