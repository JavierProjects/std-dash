import os
import sys
import unittest
import requests
# Importamos el diccionario desde el nuevo archivo
from alumnos_data import MAPEO_ALUMNOS

def evaluar_progreso():
    url_base = os.environ.get("FIREBASE_URL")
    secreto = os.environ.get("FIREBASE_SECRET")
    nombre_rama = os.environ.get("NOMBRE_RAMA")

    if nombre_rama not in MAPEO_ALUMNOS:
        print(f"La rama '{nombre_rama}' no está mapeada como un alumno activo. Fin del script.")
        return

    datos_alumno = MAPEO_ALUMNOS[nombre_rama]
    equipo = datos_alumno["equipo"]
    funciones_asignadas = datos_alumno["funciones"]
    # Hacemos el total de funciones dinámico (serán 7 según el módulo)
    total_funciones = len(funciones_asignadas) 

    print(f"Evaluando a: {nombre_rama} del {equipo}")
    print(f"Funciones a evaluar: {funciones_asignadas}")

    loader = unittest.TestLoader()
    suite_completa = loader.discover(start_dir='tests', pattern='test_*.py')

    funciones_pasadas = 0

    for funcion in funciones_asignadas:
        sub_suite = unittest.TestSuite()
        for suite in suite_completa:
            for test_case in suite:
                if hasattr(test_case, '_testMethodName') and funcion in test_case._testMethodName:
                    sub_suite.addTest(test_case)
        
        if sub_suite.countTestCases() > 0:
            runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=1)
            resultado = runner.run(sub_suite)
            
            if resultado.wasSuccessful():
                print(f"--> {funcion}: PASÓ los tests.")
                funciones_pasadas += 1
            else:
                print(f"--> {funcion}: FALLÓ o está incompleta.")
        else:
            print(f"--> Advertencia: No se encontraron tests para {funcion}")

    # Calculamos el porcentaje usando la variable dinámica
    porcentaje = int((funciones_pasadas / total_funciones) * 100)
    print(f"Resultado final: {funciones_pasadas}/{total_funciones} funciones aprobadas ({porcentaje}%)")

    if url_base and secreto:
        if not url_base.endswith("/"):
            url_base += "/"
        
        url_destino = f"{url_base}equipos/{equipo}/{nombre_rama}.json?auth={secreto}"
        payload = {
            "progreso": porcentaje,
            "funciones_terminadas": funciones_pasadas
        }
        
        try:
            respuesta = requests.patch(url_destino, json=payload)
            if respuesta.status_code == 200:
                print("¡Firebase actualizado exitosamente en tiempo real!")
            else:
                print(f"Error al actualizar Firebase. Código de estado: {respuesta.status_code}")
        except Exception as e:
            print(f"Error de conexión con Firebase: {e}")
    else:
        print("Error: Credenciales de Firebase no disponibles en el entorno.")

if __name__ == "__main__":
    evaluar_progreso()