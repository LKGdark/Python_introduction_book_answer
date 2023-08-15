from city_functions import city_country_mix

def test_city_country_mix():
    """能够正确处理santiago chile这样的国家城市名吗"""
    mix = city_country_mix('santiago','chile')
    assert mix == 'Santiago,Chile'



def test_city_country_population_mix():
    """能够正确处理santiago chile 5000000这样的国家城市名和人口数吗"""
    mix = city_country_mix('santiago','chile',population=5000000)
    assert mix == 'Santiago,Chile,5000000'