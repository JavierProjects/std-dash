import os
import sys
import unittest
import json
from alumnos_data import MAPEO_ALUMNOS

# ¡CORRECCIÓN CLAVE 1!
# Le indicamos a Python que la carpeta raíz del proyecto es parte de su ruta de búsqueda
# Esto permite que los tests puedan hacer "from src.archivo import funcion" sin fallar.
sys.path.append(os.path.abspath('.'))

# ¡CORRECCIÓN CLAVE 2!
# Función para desempaquetar las cajas de tests que genera Python 
# y convertirlas en una lista plana fácil de evaluar.
def obtener_todos_los_tests(suite_o_test):
    tests = []
    if isinstance(suite_o_test, unittest.TestSuite):
        for test in suite_o_test:
            tests.extend(obtener_todos_los_tests(test))
    else:
        tests.append(suite_o_test)
    return tests

def evaluar_progreso():
    nombre_rama = os.environ.get("NOMBRE_RAMA")

    if nombre_rama not in MAPEO_ALUMNOS:
        print(f"La rama '{nombre_rama}' no está mapeada como un alumno activo.")
        return

    datos_alumno = MAPEO_ALUMNOS[nombre_rama]
    equipo = datos_alumno["equipo"]
    funciones_asignadas = datos_alumno["funciones"]
    total_funciones = len(funciones_asignadas)

    print(f"Evaluando a: {nombre_rama} del {equipo}")

    loader = unittest.TestLoader()
    suite_completa = loader.discover(start_dir='tests', pattern='test_*.py')
    
    # Extraemos todos los tests a una lista plana segura
    todos_los_tests = obtener_todos_los_tests(suite_completa)

    funciones_pasadas = 0

    for funcion in funciones_asignadas:
        sub_suite = unittest.TestSuite()
        
        # Filtramos los tests que le tocan a esta función específica
        for test_case in todos_los_tests:
            if funcion in test_case.id():
                sub_suite.addTest(test_case)
        
        if sub_suite.countTestCases() > 0:
            runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=1)
            resultado = runner.run(sub_suite)
            
            # Si todas las pruebas internas de esta función pasan, sumamos 1
            if resultado.wasSuccessful():
                funciones_pasadas += 1

    porcentaje = int((funciones_pasadas / total_funciones) * 100)
    print(f"Resultado final: {funciones_pasadas}/{total_funciones} funciones aprobadas ({porcentaje}%)")

    # Generamos la boleta para el flujo mensajero
    datos = {
        "rama": nombre_rama,
        "equipo": equipo,
        "porcentaje": porcentaje,
        "funciones_terminadas": funciones_pasadas
    }
    
    with open("resultado.json", "w") as f:
        json.dump(datos, f)
    
    print("Boleta de calificación generada: resultado.json")

if __name__ == "__main__":
    evaluar_progreso()