from city_functions import city_country_mix

def test_city_country_mix():
    """能够正确处理santiago chile这样的国家城市名吗"""
    mix = city_country_mix('santiago','chile')
    assert mix == 'Santiago,Chile'