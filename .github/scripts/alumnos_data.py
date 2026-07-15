# Función auxiliar para generar las listas de funciones según el módulo
def generar_funciones(modulo):
    if modulo == 1:
        return ['test_01_contar_calificaciones.py', 'test_02_sumar_calificaciones.py', 'test_03_calificacion_maxima.py', 'test_04_calificacion_minima.py', 'test_05_contar_aprobados.py', 'test_06_contar_reprobados.py', 'test_07_clasificar_calificacion.py']    # 1 al 7
    elif modulo == 2:
        return ['test_08_promedio.py', 'test_09_porcentaje_aprobados.py', 'test_10_porcentaje_reprobados.py', 'test_11_frecuencia_calificaciones.py', 'test_12_moda.py', 'test_13_mediana.py', 'test_14_resumen_calificaciones.py']   # 8 al 14
    elif modulo == 3:
        return ['test_15_contar_clases.py', 'test_16_contar_asistencias.py', 'test_17_contar_faltas.py', 'test_18_porcentaje_asistencia.py', 'test_19_esta_en_riesgo.py', 'test_20_alumnos_en_riesgo.py', 'test_21_promedio_asistencia_grupo.py']  # 15 al 21
    elif modulo == 4:
        return ['test_22_contar_respuestas.py', 'test_23_obtener_opciones.py', 'test_24_frecuencia_respuestas.py', 'test_25_respuesta_mas_comun.py', 'test_26_porcentaje_respuesta.py', 'test_27_resumen_encuesta.py', 'test_28_reporte_general.py']  # 22 al 28
    return []

# Diccionario importable basado en tu CSV
# >>> INICIO_MAPEO <<<
MAPEO_ALUMNOS = {
    "angeles_m_luis": {
        "equipo": "equipo_1",
        "funciones": [
            "test_01_contar_calificaciones.py",
            "test_02_sumar_calificaciones.py",
            "test_03_calificacion_maxima.py",
            "test_04_calificacion_minima.py",
            "test_05_contar_aprobados.py",
            "test_06_contar_reprobados.py",
            "test_07_clasificar_calificacion.py"
        ]
    },
    "artega_a_angel": {
        "equipo": "equipo_2",
        "funciones": [
            "test_01_contar_calificaciones.py",
            "test_02_sumar_calificaciones.py",
            "test_03_calificacion_maxima.py",
            "test_04_calificacion_minima.py",
            "test_05_contar_aprobados.py",
            "test_06_contar_reprobados.py",
            "test_07_clasificar_calificacion.py"
        ]
    },
    "bravo_r_alain": {
        "equipo": "equipo_3",
        "funciones": [
            "test_01_contar_calificaciones.py",
            "test_02_sumar_calificaciones.py",
            "test_03_calificacion_maxima.py",
            "test_04_calificacion_minima.py",
            "test_05_contar_aprobados.py",
            "test_06_contar_reprobados.py",
            "test_07_clasificar_calificacion.py"
        ]
    },
    "cruz_o_sam": {
        "equipo": "equipo_4",
        "funciones": [
            "test_01_contar_calificaciones.py",
            "test_02_sumar_calificaciones.py",
            "test_03_calificacion_maxima.py",
            "test_04_calificacion_minima.py",
            "test_05_contar_aprobados.py",
            "test_06_contar_reprobados.py",
            "test_07_clasificar_calificacion.py"
        ]
    },
    "galevz_j_dulce": {
        "equipo": "equipo_5",
        "funciones": [
            "test_01_contar_calificaciones.py",
            "test_02_sumar_calificaciones.py",
            "test_03_calificacion_maxima.py",
            "test_04_calificacion_minima.py",
            "test_05_contar_aprobados.py",
            "test_06_contar_reprobados.py",
            "test_07_clasificar_calificacion.py"
        ]
    },
    "garcia_a_gael": {
        "equipo": "equipo_6",
        "funciones": [
            "test_01_contar_calificaciones.py",
            "test_02_sumar_calificaciones.py",
            "test_03_calificacion_maxima.py",
            "test_04_calificacion_minima.py",
            "test_05_contar_aprobados.py",
            "test_06_contar_reprobados.py",
            "test_07_clasificar_calificacion.py"
        ]
    },
    "garcia_g_emilio": {
        "equipo": "equipo_7",
        "funciones": [
            "test_01_contar_calificaciones.py",
            "test_02_sumar_calificaciones.py",
            "test_03_calificacion_maxima.py",
            "test_04_calificacion_minima.py",
            "test_05_contar_aprobados.py",
            "test_06_contar_reprobados.py",
            "test_07_clasificar_calificacion.py"
        ]
    },
    "hndez_m_allison": {
        "equipo": "equipo_1",
        "funciones": [
            "test_08_promedio.py",
            "test_09_porcentaje_aprobados.py",
            "test_10_porcentaje_reprobados.py",
            "test_11_frecuencia_calificaciones.py",
            "test_12_moda.py",
            "test_13_mediana.py",
            "test_14_resumen_calificaciones.py"
        ]
    },
    "lopez_e_melissa": {
        "equipo": "equipo_2",
        "funciones": [
            "test_08_promedio.py",
            "test_09_porcentaje_aprobados.py",
            "test_10_porcentaje_reprobados.py",
            "test_11_frecuencia_calificaciones.py",
            "test_12_moda.py",
            "test_13_mediana.py",
            "test_14_resumen_calificaciones.py"
        ]
    },
    "mejia_h_sinai": {
        "equipo": "equipo_3",
        "funciones": [
            "test_08_promedio.py",
            "test_09_porcentaje_aprobados.py",
            "test_10_porcentaje_reprobados.py",
            "test_11_frecuencia_calificaciones.py",
            "test_12_moda.py",
            "test_13_mediana.py",
            "test_14_resumen_calificaciones.py"
        ]
    },
    "maturano_p_citla": {
        "equipo": "equipo_4",
        "funciones": [
            "test_08_promedio.py",
            "test_09_porcentaje_aprobados.py",
            "test_10_porcentaje_reprobados.py",
            "test_11_frecuencia_calificaciones.py",
            "test_12_moda.py",
            "test_13_mediana.py",
            "test_14_resumen_calificaciones.py"
        ]
    },
    "mendoza_r_jose": {
        "equipo": "equipo_5",
        "funciones": [
            "test_08_promedio.py",
            "test_09_porcentaje_aprobados.py",
            "test_10_porcentaje_reprobados.py",
            "test_11_frecuencia_calificaciones.py",
            "test_12_moda.py",
            "test_13_mediana.py",
            "test_14_resumen_calificaciones.py"
        ]
    },
    "monjaraz_p_jovany": {
        "equipo": "equipo_6",
        "funciones": [
            "test_08_promedio.py",
            "test_09_porcentaje_aprobados.py",
            "test_10_porcentaje_reprobados.py",
            "test_11_frecuencia_calificaciones.py",
            "test_12_moda.py",
            "test_13_mediana.py",
            "test_14_resumen_calificaciones.py"
        ]
    },
    "perez_a_alison": {
        "equipo": "equipo_7",
        "funciones": [
            "test_08_promedio.py",
            "test_09_porcentaje_aprobados.py",
            "test_10_porcentaje_reprobados.py",
            "test_11_frecuencia_calificaciones.py",
            "test_12_moda.py",
            "test_13_mediana.py",
            "test_14_resumen_calificaciones.py"
        ]
    },
    "perez_r_oscar": {
        "equipo": "equipo_1",
        "funciones": [
            "test_15_contar_clases.py",
            "test_16_contar_asistencias.py",
            "test_17_contar_faltas.py",
            "test_18_porcentaje_asistencia.py",
            "test_19_esta_en_riesgo.py",
            "test_20_alumnos_en_riesgo.py",
            "test_21_promedio_asistencia_grupo.py"
        ]
    },
    "portillo_g_bruno": {
        "equipo": "equipo_2",
        "funciones": [
            "test_15_contar_clases.py",
            "test_16_contar_asistencias.py",
            "test_17_contar_faltas.py",
            "test_18_porcentaje_asistencia.py",
            "test_19_esta_en_riesgo.py",
            "test_20_alumnos_en_riesgo.py",
            "test_21_promedio_asistencia_grupo.py"
        ]
    },
    "rufino_v_luis": {
        "equipo": "equipo_3",
        "funciones": [
            "test_15_contar_clases.py",
            "test_16_contar_asistencias.py",
            "test_17_contar_faltas.py",
            "test_18_porcentaje_asistencia.py",
            "test_19_esta_en_riesgo.py",
            "test_20_alumnos_en_riesgo.py",
            "test_21_promedio_asistencia_grupo.py"
        ]
    },
    "salvador_b_citla": {
        "equipo": "equipo_4",
        "funciones": [
            "test_15_contar_clases.py",
            "test_16_contar_asistencias.py",
            "test_17_contar_faltas.py",
            "test_18_porcentaje_asistencia.py",
            "test_19_esta_en_riesgo.py",
            "test_20_alumnos_en_riesgo.py",
            "test_21_promedio_asistencia_grupo.py"
        ]
    },
    "aspeytia_g_alma": {
        "equipo": "equipo_5",
        "funciones": [
            "test_15_contar_clases.py",
            "test_16_contar_asistencias.py",
            "test_17_contar_faltas.py",
            "test_18_porcentaje_asistencia.py",
            "test_19_esta_en_riesgo.py",
            "test_20_alumnos_en_riesgo.py",
            "test_21_promedio_asistencia_grupo.py"
        ]
    },
    "galea_l_miguel": {
        "equipo": "equipo_6",
        "funciones": [
            "test_15_contar_clases.py",
            "test_16_contar_asistencias.py",
            "test_17_contar_faltas.py",
            "test_18_porcentaje_asistencia.py",
            "test_19_esta_en_riesgo.py",
            "test_20_alumnos_en_riesgo.py",
            "test_21_promedio_asistencia_grupo.py"
        ]
    },
    "islas_o_maria": {
        "equipo": "equipo_7",
        "funciones": [
            "test_15_contar_clases.py",
            "test_16_contar_asistencias.py",
            "test_17_contar_faltas.py",
            "test_18_porcentaje_asistencia.py",
            "test_19_esta_en_riesgo.py",
            "test_20_alumnos_en_riesgo.py",
            "test_21_promedio_asistencia_grupo.py"
        ]
    },
    "lopez_l_elias": {
        "equipo": "equipo_1",
        "funciones": [
            "test_22_contar_respuestas.py",
            "test_23_obtener_opciones.py",
            "test_24_frecuencia_respuestas.py",
            "test_25_respuesta_mas_comun.py",
            "test_26_porcentaje_respuesta.py",
            "test_27_resumen_encuesta.py",
            "test_28_reporte_general.py"
        ]
    },
    "mnez_h_gael": {
        "equipo": "equipo_2",
        "funciones": [
            "test_22_contar_respuestas.py",
            "test_23_obtener_opciones.py",
            "test_24_frecuencia_respuestas.py",
            "test_25_respuesta_mas_comun.py",
            "test_26_porcentaje_respuesta.py",
            "test_27_resumen_encuesta.py",
            "test_28_reporte_general.py"
        ]
    },
    "mnez_o_angel": {
        "equipo": "equipo_3",
        "funciones": [
            "test_22_contar_respuestas.py",
            "test_23_obtener_opciones.py",
            "test_24_frecuencia_respuestas.py",
            "test_25_respuesta_mas_comun.py",
            "test_26_porcentaje_respuesta.py",
            "test_27_resumen_encuesta.py",
            "test_28_reporte_general.py"
        ]
    },
    "perez_m_chris": {
        "equipo": "equipo_4",
        "funciones": [
            "test_22_contar_respuestas.py",
            "test_23_obtener_opciones.py",
            "test_24_frecuencia_respuestas.py",
            "test_25_respuesta_mas_comun.py",
            "test_26_porcentaje_respuesta.py",
            "test_27_resumen_encuesta.py",
            "test_28_reporte_general.py"
        ]
    },
    "porras_b_ama": {
        "equipo": "equipo_5",
        "funciones": [
            "test_22_contar_respuestas.py",
            "test_23_obtener_opciones.py",
            "test_24_frecuencia_respuestas.py",
            "test_25_respuesta_mas_comun.py",
            "test_26_porcentaje_respuesta.py",
            "test_27_resumen_encuesta.py",
            "test_28_reporte_general.py"
        ]
    },
    "mejia_e_estrella": {
        "equipo": "equipo_6",
        "funciones": [
            "test_22_contar_respuestas.py",
            "test_23_obtener_opciones.py",
            "test_24_frecuencia_respuestas.py",
            "test_25_respuesta_mas_comun.py",
            "test_26_porcentaje_respuesta.py",
            "test_27_resumen_encuesta.py",
            "test_28_reporte_general.py"
        ]
    },
    "mnez_a_jose": {
        "equipo": "equipo_7",
        "funciones": [
            "test_22_contar_respuestas.py",
            "test_23_obtener_opciones.py",
            "test_24_frecuencia_respuestas.py",
            "test_25_respuesta_mas_comun.py",
            "test_26_porcentaje_respuesta.py",
            "test_27_resumen_encuesta.py",
            "test_28_reporte_general.py"
        ]
    },
    "bob": {
        "equipo": "equipo_8",
        "funciones": [
            "test_01_contar_calificaciones.py",
            "test_02_sumar_calificaciones.py",
            "test_03_calificacion_maxima.py",
            "test_04_calificacion_minima.py",
            "test_05_contar_aprobados.py",
            "test_06_contar_reprobados.py",
            "test_07_clasificar_calificacion.py"
        ]
    },
    "javier": {
        "equipo": "equipo_8",
        "funciones": [
            "test_08_promedio.py",
            "test_09_porcentaje_aprobados.py",
            "test_10_porcentaje_reprobados.py",
            "test_11_frecuencia_calificaciones.py",
            "test_12_moda.py",
            "test_13_mediana.py",
            "test_14_resumen_calificaciones.py"
        ]
    },
    "eve": {
        "equipo": "equipo_8",
        "funciones": [
            "test_15_contar_clases.py",
            "test_16_contar_asistencias.py",
            "test_17_contar_faltas.py",
            "test_18_porcentaje_asistencia.py",
            "test_19_esta_en_riesgo.py",
            "test_20_alumnos_en_riesgo.py",
            "test_21_promedio_asistencia_grupo.py"
        ]
    },
    "alice": {
        "equipo": "equipo_8",
        "funciones": [
            "test_22_contar_respuestas.py",
            "test_23_obtener_opciones.py",
            "test_24_frecuencia_respuestas.py",
            "test_25_respuesta_mas_comun.py",
            "test_26_porcentaje_respuesta.py",
            "test_27_resumen_encuesta.py",
            "test_28_reporte_general.py"
        ]
    }
}
# >>> FIN_MAPEO <<<