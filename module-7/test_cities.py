from city_functions import city_country

def test_city_country():
    """Would foreign cities work?"""
    paris_france = city_country('paris', 'france')
    assert paris_france == 'Paris, France'

