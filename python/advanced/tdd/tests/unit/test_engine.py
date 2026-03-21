"""
Test cases for the Car class.
"""

import pytest

from car.engine import Engine


def test_engine_initialization():
    """Test that the Engine class initializes correctly."""
    engine = Engine(type='V6',horsepower=150)
    assert engine.type == 'V6'
    assert engine.horsepower == 150
    

@pytest.mark.parametrize("type, horsepower", [
    ('V8', 300),
    ('Electric', 200),
    ('Hybrid', 250),
])
def test_engine_valid_parameters(type, horsepower):
    """Test that the Engine class initializes correctly with valid parameters."""
    engine = Engine(type=type, horsepower=horsepower)
    assert engine.type == type
    assert engine.horsepower == horsepower

@pytest.mark.parametrize("type, horsepower", [
    ('V8', -100),
    ('Electric', "fifty"),
    ('Hybrid', -50),
])
def test_engine_invalid_horsepower(type, horsepower):
    """Test that the Engine class raises an error for invalid horsepower."""
    with pytest.raises(ValueError):
        Engine(type, horsepower)
