import os
import pandas as pd

from stats_backend.settings import EXCEL_DIR

# CONSTANTES
ROUND = 3
COEF_VAR = 15

# HELPERS FUNCTIONS
_r = lambda value: round(value, ROUND)
# excel_file = lambda file: os.path.join(EXCEL_DIR, f"{file}.xlsx")
# serie_from_excel = lambda file: list(pd.read_excel(excel_file(file))['DATA'])

def serie_from_excel(file, data='DATA'):
    path = os.path.join(EXCEL_DIR, f"{file}.xlsx")
    return list(pd.read_excel(path)[data])
