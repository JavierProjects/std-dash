# Función auxiliar para generar las listas de funciones según el módulo
def generar_funciones(modulo):
    if modulo == 1:
        return [f"funcion_{i}" for i in range(1, 8)]    # 1 al 7
    elif modulo == 2:
        return [f"funcion_{i}" for i in range(8, 15)]   # 8 al 14
    elif modulo == 3:
        return [f"funcion_{i}" for i in range(15, 22)]  # 15 al 21
    elif modulo == 4:
        return [f"funcion_{i}" for i in range(22, 29)]  # 22 al 28
    return []

# Diccionario importable basado en tu CSV
# >>> INICIO_MAPEO <<<
MAPEO_ALUMNOS = {
    "angeles_m_luis": {
        "equipo": "equipo_1",
        "funciones": [
            "funcion_1",
            "funcion_2",
            "funcion_3",
            "funcion_4",
            "funcion_5",
            "funcion_6",
            "funcion_7"
        ]
    },
    "artega_a_angel": {
        "equipo": "equipo_2",
        "funciones": [
            "funcion_1",
            "funcion_2",
            "funcion_3",
            "funcion_4",
            "funcion_5",
            "funcion_6",
            "funcion_7"
        ]
    },
    "bravo_r_alain": {
        "equipo": "equipo_3",
        "funciones": [
            "funcion_1",
            "funcion_2",
            "funcion_3",
            "funcion_4",
            "funcion_5",
            "funcion_6",
            "funcion_7"
        ]
    },
    "cruz_o_sam": {
        "equipo": "equipo_4",
        "funciones": [
            "funcion_1",
            "funcion_2",
            "funcion_3",
            "funcion_4",
            "funcion_5",
            "funcion_6",
            "funcion_7"
        ]
    },
    "galevz_j_dulce": {
        "equipo": "equipo_5",
        "funciones": [
            "funcion_1",
            "funcion_2",
            "funcion_3",
            "funcion_4",
            "funcion_5",
            "funcion_6",
            "funcion_7"
        ]
    },
    "garcia_a_gael": {
        "equipo": "equipo_6",
        "funciones": [
            "funcion_1",
            "funcion_2",
            "funcion_3",
            "funcion_4",
            "funcion_5",
            "funcion_6",
            "funcion_7"
        ]
    },
    "garcia_g_emilio": {
        "equipo": "equipo_7",
        "funciones": [
            "funcion_1",
            "funcion_2",
            "funcion_3",
            "funcion_4",
            "funcion_5",
            "funcion_6",
            "funcion_7"
        ]
    },
    "hndez_m_allison": {
        "equipo": "equipo_1",
        "funciones": [
            "funcion_8",
            "funcion_9",
            "funcion_10",
            "funcion_11",
            "funcion_12",
            "funcion_13",
            "funcion_14"
        ]
    },
    "lopez_e_melissa": {
        "equipo": "equipo_2",
        "funciones": [
            "funcion_8",
            "funcion_9",
            "funcion_10",
            "funcion_11",
            "funcion_12",
            "funcion_13",
            "funcion_14"
        ]
    },
    "mejia_h_sinai": {
        "equipo": "equipo_3",
        "funciones": [
            "funcion_8",
            "funcion_9",
            "funcion_10",
            "funcion_11",
            "funcion_12",
            "funcion_13",
            "funcion_14"
        ]
    },
    "maturano_p_citla": {
        "equipo": "equipo_4",
        "funciones": [
            "funcion_8",
            "funcion_9",
            "funcion_10",
            "funcion_11",
            "funcion_12",
            "funcion_13",
            "funcion_14"
        ]
    },
    "mendoza_r_jose": {
        "equipo": "equipo_5",
        "funciones": [
            "funcion_8",
            "funcion_9",
            "funcion_10",
            "funcion_11",
            "funcion_12",
            "funcion_13",
            "funcion_14"
        ]
    },
    "monjaraz_p_jovany": {
        "equipo": "equipo_6",
        "funciones": [
            "funcion_8",
            "funcion_9",
            "funcion_10",
            "funcion_11",
            "funcion_12",
            "funcion_13",
            "funcion_14"
        ]
    },
    "perez_a_alison": {
        "equipo": "equipo_7",
        "funciones": [
            "funcion_8",
            "funcion_9",
            "funcion_10",
            "funcion_11",
            "funcion_12",
            "funcion_13",
            "funcion_14"
        ]
    },
    "perez_r_oscar": {
        "equipo": "equipo_1",
        "funciones": [
            "funcion_15",
            "funcion_16",
            "funcion_17",
            "funcion_18",
            "funcion_19",
            "funcion_20",
            "funcion_21"
        ]
    },
    "portillo_g_bruno": {
        "equipo": "equipo_2",
        "funciones": [
            "funcion_15",
            "funcion_16",
            "funcion_17",
            "funcion_18",
            "funcion_19",
            "funcion_20",
            "funcion_21"
        ]
    },
    "rufino_v_luis": {
        "equipo": "equipo_3",
        "funciones": [
            "funcion_15",
            "funcion_16",
            "funcion_17",
            "funcion_18",
            "funcion_19",
            "funcion_20",
            "funcion_21"
        ]
    },
    "salvador_b_citla": {
        "equipo": "equipo_4",
        "funciones": [
            "funcion_15",
            "funcion_16",
            "funcion_17",
            "funcion_18",
            "funcion_19",
            "funcion_20",
            "funcion_21"
        ]
    },
    "aspeytia_g_alma": {
        "equipo": "equipo_5",
        "funciones": [
            "funcion_15",
            "funcion_16",
            "funcion_17",
            "funcion_18",
            "funcion_19",
            "funcion_20",
            "funcion_21"
        ]
    },
    "galea_l_miguel": {
        "equipo": "equipo_6",
        "funciones": [
            "funcion_15",
            "funcion_16",
            "funcion_17",
            "funcion_18",
            "funcion_19",
            "funcion_20",
            "funcion_21"
        ]
    },
    "islas_o_maria": {
        "equipo": "equipo_7",
        "funciones": [
            "funcion_15",
            "funcion_16",
            "funcion_17",
            "funcion_18",
            "funcion_19",
            "funcion_20",
            "funcion_21"
        ]
    },
    "lopez_l_elias": {
        "equipo": "equipo_1",
        "funciones": [
            "funcion_22",
            "funcion_23",
            "funcion_24",
            "funcion_25",
            "funcion_26",
            "funcion_27",
            "funcion_28"
        ]
    },
    "mnez_h_gael": {
        "equipo": "equipo_2",
        "funciones": [
            "funcion_22",
            "funcion_23",
            "funcion_24",
            "funcion_25",
            "funcion_26",
            "funcion_27",
            "funcion_28"
        ]
    },
    "mnez_o_angel": {
        "equipo": "equipo_3",
        "funciones": [
            "funcion_22",
            "funcion_23",
            "funcion_24",
            "funcion_25",
            "funcion_26",
            "funcion_27",
            "funcion_28"
        ]
    },
    "perez_m_chris": {
        "equipo": "equipo_4",
        "funciones": [
            "funcion_22",
            "funcion_23",
            "funcion_24",
            "funcion_25",
            "funcion_26",
            "funcion_27",
            "funcion_28"
        ]
    },
    "porras_b_ama": {
        "equipo": "equipo_5",
        "funciones": [
            "funcion_22",
            "funcion_23",
            "funcion_24",
            "funcion_25",
            "funcion_26",
            "funcion_27",
            "funcion_28"
        ]
    },
    "mejia_e_estrella": {
        "equipo": "equipo_6",
        "funciones": [
            "funcion_22",
            "funcion_23",
            "funcion_24",
            "funcion_25",
            "funcion_26",
            "funcion_27",
            "funcion_28"
        ]
    },
    "mnez_a_jose": {
        "equipo": "equipo_7",
        "funciones": [
            "funcion_22",
            "funcion_23",
            "funcion_24",
            "funcion_25",
            "funcion_26",
            "funcion_27",
            "funcion_28"
        ]
    },
    "bob": {
        "equipo": "equipo_8",
        "funciones": [
            "funcion_1",
            "funcion_2",
            "funcion_3",
            "funcion_4",
            "funcion_5",
            "funcion_6",
            "funcion_7"
        ]
    },
    "javier": {
        "equipo": "equipo_8",
        "funciones": [
            "funcion_8",
            "funcion_9",
            "funcion_10",
            "funcion_11",
            "funcion_12",
            "funcion_13",
            "funcion_14"
        ]
    },
    "eve": {
        "equipo": "equipo_8",
        "funciones": [
            "funcion_15",
            "funcion_16",
            "funcion_17",
            "funcion_18",
            "funcion_19",
            "funcion_20",
            "funcion_21"
        ]
    },
    "alice": {
        "equipo": "equipo_8",
        "funciones": [
            "funcion_22",
            "funcion_23",
            "funcion_24",
            "funcion_25",
            "funcion_26",
            "funcion_27",
            "funcion_28"
        ]
    }
}
# >>> FIN_MAPEO <<<