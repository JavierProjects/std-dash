import os
import sys
import unittest
import json
from alumnos_data import MAPEO_ALUMNOS

sys.path.append(os.path.abspath('.'))

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
        print(f"La rama '{nombre_rama}' no está mapeada.")
        return

    datos_alumno = MAPEO_ALUMNOS[nombre_rama]
    equipo = datos_alumno["equipo"]
    funciones_asignadas = datos_alumno["funciones"]
    total_funciones = len(funciones_asignadas)

    print(f"Evaluando a: {nombre_rama} del {equipo}")

    loader = unittest.TestLoader()
    suite_completa = loader.discover(start_dir='tests', pattern='test_*.py')
    todos_los_tests = obtener_todos_los_tests(suite_completa)

    # --- INICIO DEL DIAGNÓSTICO ---
    print("\n--- DIAGNÓSTICO DE TESTS ENCONTRADOS ---")
    if not todos_los_tests:
        print("¡ALERTA! Python no encontró NINGÚN test en la carpeta 'tests/'")
    else:
        for t in todos_los_tests:
            print(f"Detectado: {t.id()}")
    print("----------------------------------------\n")
    # --- FIN DEL DIAGNÓSTICO ---

    funciones_pasadas = 0

    for funcion in funciones_asignadas:
        sub_suite = unittest.TestSuite()
        
        for test_case in todos_los_tests:
            if funcion in test_case.id():
                sub_suite.addTest(test_case)
        
        if sub_suite.countTestCases() > 0:
            # Subimos la verbosidad a 2 para que imprima más detalles
            runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
            resultado = runner.run(sub_suite)
            
            if resultado.wasSuccessful():
                funciones_pasadas += 1
            else:
                # Si fallan, imprimimos el motivo exacto (Error de Sintaxis, Assert, Import, etc.)
                print(f"\n[!] REVISIÓN NECESARIA EN: {funcion}")
                for test, trace in resultado.failures:
                    print(f"⚠️ FALLO LÓGICO en {test.id()}:\n{trace}")
                for test, trace in resultado.errors:
                    print(f"❌ ERROR DE CÓDIGO en {test.id()}:\n{trace}")
                print("-" * 40 + "\n")

    porcentaje = int((funciones_pasadas / total_funciones) * 100)
    print(f"Resultado final: {funciones_pasadas}/{total_funciones} funciones aprobadas ({porcentaje}%)")

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