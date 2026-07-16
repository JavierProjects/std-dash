import os
import sys
import unittest
import json
from alumnos_data import MAPEO_ALUMNOS

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

    funciones_pasadas = 0

    for funcion in funciones_asignadas:
        sub_suite = unittest.TestSuite()
        for suite in suite_completa:
            for test_case in suite:
                if funcion in test_case.id():
                    sub_suite.addTest(test_case)
        
        if sub_suite.countTestCases() > 0:
            runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=1)
            resultado = runner.run(sub_suite)
            
            if resultado.wasSuccessful():
                funciones_pasadas += 1

    porcentaje = int((funciones_pasadas / total_funciones) * 100)
    print(f"Resultado final: {funciones_pasadas}/{total_funciones} funciones aprobadas ({porcentaje}%)")

    # Guardar resultado en una boleta JSON
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