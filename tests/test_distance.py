from babs_utils.distance import haversine

def test_return_type_haversine():
    assert type(haversine(23, 23, 45, 45)) == float

def test_return_value_haversine():
    assert round(haversine(23, 23, 45, 45),2) == 3156.07
