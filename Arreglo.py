import time
import random


NUM_ALUMNOS = 500
NUM_MATERIAS = 6

def generar_matriz_calificaciones():
    """Genera una matriz de calificaciones aleatorias."""
    matriz = [[random.randint(50, 100) for _ in range(NUM_MATERIAS)] for _ in range(NUM_ALUMNOS)]
    return matriz

def buscar_calificacion(matriz, alumno, materia):
    """Busca y retorna la calificación de un alumno en una materia."""
    return matriz[alumno - 1][materia - 1]

def medir_tiempo_busqueda(matriz, num_alumnos, num_materias):
    """Mide el tiempo de búsqueda de una calificación."""

    alumno_a_buscar = 321
    materia_a_buscar = 5
    
    start_time = time.time()
    calificacion = buscar_calificacion(matriz, alumno_a_buscar, materia_a_buscar)
    end_time = time.time()
    
    tiempo_ejecucion = (end_time - start_time) * 1000  # Convertir a milisegundos
    
    print(f"Búsqueda de la calificación para el alumno {alumno_a_buscar} en la materia {materia_a_buscar}:")
    print(f"Calificación encontrada: {calificacion}")
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} milisegundos")
    
    return tiempo_ejecucion


print("--- Escenario 1: Matriz de (Alumnos x Materias) ---")
matriz_por_filas = generar_matriz_calificaciones()
tiempo_filas = medir_tiempo_busqueda(matriz_por_filas, NUM_ALUMNOS, NUM_MATERIAS)
print("-" * 50)



print("--- Escenario 2: Matriz transpuesta (Materias x Alumnos) ---")


matriz_por_columnas = [[random.randint(50, 100) for _ in range(NUM_ALUMNOS)] for _ in range(NUM_MATERIAS)]

def buscar_calificacion_transpuesta(matriz_t, alumno, materia):
    """Busca la calificación en la matriz transpuesta."""
    return matriz_t[materia - 1][alumno - 1]

def medir_tiempo_busqueda_transpuesta(matriz_t, num_materias, num_alumnos):
    """Mide el tiempo de búsqueda de una calificación en una matriz transpuesta."""
    alumno_a_buscar = 321
    materia_a_buscar = 5
    
    start_time = time.time()
    calificacion = buscar_calificacion_transpuesta(matriz_t, alumno_a_buscar, materia_a_buscar)
    end_time = time.time()
    
    tiempo_ejecucion = (end_time - start_time) * 1000
    
    print(f"Búsqueda de la calificación para el alumno {alumno_a_buscar} en la materia {materia_a_buscar}:")
    print(f"Calificación encontrada: {calificacion}")
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} milisegundos")
    
    return tiempo_ejecucion

tiempo_columnas = medir_tiempo_busqueda_transpuesta(matriz_por_columnas, NUM_MATERIAS, NUM_ALUMNOS)
print("-" * 50)



print("\n--- Comparación de Tiempos ---")
if tiempo_filas < tiempo_columnas:
    print("La matriz por filas (alumnos x materias) fue más rápida.")
elif tiempo_columnas < tiempo_filas:
    print("La matriz por columnas (materias x alumnos) fue más rápida.")
else:
    print("Ambas implementaciones tuvieron un tiempo de ejecución similar.")

