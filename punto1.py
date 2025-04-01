from collections import Counter
import string

def contar_letras(archivo):
  with open(archivo, 'r') as f:
    texto = f.read().lower()
        
  # Filtrar solo letras
  letras = [char for char in texto if char in string.ascii_lowercase]
        
  # Contar frecuencia de letras
  frecuencia = Counter(letras)
        
  # Mostrar resultados
  for letra, cantidad in sorted(frecuencia.items()):
    print(f"{letra}: {cantidad}")


# Uso: Reemplaza 'archivo.txt' con el nombre de tu archivo
txt_archivo = './caracteres.txt'
contar_letras(txt_archivo)
