import pandas as pd

# Función para convertir a datetime y manejar errores


def convertir_fecha(fecha):
    """convertir fecha con valor erroneo custom

    Args:
        fecha (str): valor inicial del string

    Returns:
        date/str: resultado de la transformacion
    """
    try:
        # Intentar conversión
        return pd.to_datetime(fecha, errors='raise')
    except Exception:
        # Si falla, devolver mensaje de error con el valor original
        return f"ERROR - ({fecha})"
