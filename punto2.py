def leer_palabras(archivo):
    with open(archivo, 'r') as f:
        palabras = f.read().lower().split()
    return set(palabras)

def operaciones_con_archivos(archivo_a, archivo_b):
    # Array con valores de cada una de las palabras
    palabras_a = leer_palabras(archivo_a)
    palabras_b = leer_palabras(archivo_b)
    
    
    # Operaciones de Conjuntos
    union = palabras_a | palabras_b
    interseccion = palabras_a & palabras_b
    diferencia_a_b = palabras_a - palabras_b
    diferencia_b_a = palabras_b - palabras_a
    
    # Valores de salida
    print(f"\n A U B (Unión): {union} palabras \n")
    print(f"A n B (Intersección): {interseccion} palabras \n")
    print(f"A - B (Diferencia A - B): {diferencia_a_b} palabras \n")
    print(f"B - A (Diferencia B - A): {diferencia_b_a} palabras \n")
    print(f"|A| (Cantidad de palabras en A): {palabras_a} \n")
    print(f"|B| (Cantidad de palabras en B): {palabras_b} \n")
    
    # Verificar si {para, informacion} está contenido en A ∩ B
    subconjunto = {"para", "informacion"}
    es_subconjunto = subconjunto.issubset(interseccion)
    print(f"{{para, informacion}} ⊆ A ∩ B: {es_subconjunto}")

# Carga de archivos
archivo_a = "conjuntoA.txt"
archivo_b = "conjuntoB.txt"
operaciones_con_archivos(archivo_a, archivo_b)