import csv

# Глобальные переменные для хранения данных по регионам
REGIONAL_INFO = {}
REGIONAL_DATA = {}
LOADED_REGIONAL = False

def load_regional_info():
    """Загружает статические данные по переменным регионов из файла CBA_regional_info.csv."""
    with open('CBA_regional_info.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            variable = row['variable']
            REGIONAL_INFO[variable] = {
                'gdx_variable': row['gdx_variable'],
                'description': row['description'],
                'unit': row['unit']
            }

def load_regional_data():
    """Загружает динамические данные по каждому региону из файла CBA_regional_data.csv."""
    with open('CBA_regional_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            year = int(row['year'])
            region_id = row.get('region_id', 'global')  # Используем уникальный идентификатор региона
            
            if region_id not in REGIONAL_DATA:
                REGIONAL_DATA[region_id] = {}

            if year not in REGIONAL_DATA[region_id]:
                REGIONAL_DATA[region_id][year] = {}

            # Добавление данных для каждого параметра
            REGIONAL_DATA[region_id][year] = {
                'gdp_baseline': float(row['gdp_baseline']),
                'mitigation': float(row['mitigation']),
                'pop': float(row['pop']),
                'emi_ind': float(row['emi_ind']),
                'gdp_net': float(row['gdp_net']),
                'gdp_gross': float(row['gdp_gross']),
                'capital': float(row['capital']),
                'investments': float(row['investments']),
                'savings': float(row['savings']),
                'consumption': float(row['consumption']),
                # Добавьте другие переменные при необходимости
            }

def load_all_regional_data():
    """Загружает все региональные данные, если они еще не загружены."""
    global LOADED_REGIONAL
    if not LOADED_REGIONAL:
        load_regional_info()
        load_regional_data()
        LOADED_REGIONAL = True

def get_regional_data(region, year, parameter):
    """Получает значение параметра для конкретного региона и года."""
    load_all_regional_data()
    return REGIONAL_DATA.get(region, {}).get(year, {}).get(parameter, None)

def get_regional_info(parameter):
    """Получает информацию о параметре из файла CBA_regional_info.csv."""
    load_all_regional_data()
    return REGIONAL_INFO.get(parameter, None)