"""
Ejemplo_traduccion.py
Script de ejemplo para usar las secuencias de DNA con AminoLab

Este script lee una secuencia de ADN de ejemplo y muestra cómo se usaría
con el programa AminoLab para traducir a proteína.

Nota: La función 'traducir' de AminoLab está comentada, ya que es un ejemplo.
"""

# En AminoLab, importar la función de traducción:
# from AminoLab import traducir

# Ruta del archivo de ejemplo
archivo = "Secuencias de DNA de ejemplo/Ejemplos_basicos/Secuencia1.txt"

# Leer la secuencia del archivo
with open(archivo, "r") as f:
    secuencia = f.read().strip()

# Mostrar la secuencia leída
print("Secuencia de ADN leída:")
print(secuencia)

# Traducir la secuencia a proteína (ejemplo)
# proteina = traducir([secuencia])
# print("Proteína resultante:")
# print(proteina)

print("\nEste script sirve como ejemplo de cómo leer secuencias y pasarlas a AminoLab.")
