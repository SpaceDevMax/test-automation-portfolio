import pytest
from geometry import rectangle_area, circle_area

def test_rectangle_area():
    assert rectangle_area(0, 1) == 0
    assert rectangle_area(1, 1) == 1 
    assert rectangle_area(5, 4) == 20
    assert rectangle_area(1.2, 2.4) == 2.87 # Fails

def test_circle_area():
    assert abs(circle_area(5)) == 78.53981633974483 
    
    
def test_circle_area_radius_zero():
    assert circle_area(0) == 0

def test_circle_area_negative_1():
    assert circle_area(-1) == -1 # Fails

def test_circle_area_negative_2():
    with pytest.raises(ValueError, match = "Radius cannot be negative"): 
        circle_area(-1)



