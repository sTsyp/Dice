from ssp import get_regional_data, get_regional_info

# Список регионов, для которых будет производиться расчет
REGIONS = ['region1', 'region2', 'region3']  # можно задать любые имена регионов

# Глобальные параметры для хранения результатов по регионам
regional_results = {
    region: {
        'GDP': [],
        'emissions': [],
        'population': [],
        # Добавьте другие параметры, если необходимо
    }
    for region in REGIONS
}

def calculate_regional_gdp(region, year):
    """Рассчитывает ВВП для конкретного региона и года."""
    gdp_baseline = get_regional_data(region, year, 'gdp_baseline')
    mitigation = get_regional_data(region, year, 'mitigation')
    # Пример расчета ВВП с учетом смягчения выбросов
    gdp = gdp_baseline * (1 - mitigation)
    return gdp

def calculate_regional_emissions(region, year):
    """Рассчитывает выбросы для конкретного региона и года."""
    pop = get_regional_data(region, year, 'pop')
    emi_ind = get_regional_data(region, year, 'emi_ind')
    emissions = pop * emi_ind
    return emissions

def run_regional_calculations():
    """Запускает расчеты для каждого региона и сохраняет результаты."""
    for region in REGIONS:
        for year in range(2015, 2100):  # Пример диапазона лет
            # Расчет ВВП
            gdp = calculate_regional_gdp(region, year)
            regional_results[region]['GDP'].append((year, gdp))
            
            # Расчет выбросов
            emissions = calculate_regional_emissions(region, year)
            regional_results[region]['emissions'].append((year, emissions))
            
            # Сохранение данных по населению
            population = get_regional_data(region, year, 'pop')
            regional_results[region]['population'].append((year, population))

# Пример использования функции
run_regional_calculations()
print(regional_results)  # Выводим результаты расчета для проверки