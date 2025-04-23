def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Tests

def test_add():
    assert add(1, 1) == 2
    assert add(-1, 1) == 0

def test_substract():
    assert substract(1, 1) == 0 
    assert substract(-1, 1) == -2 

def test_multiply():
    assert multiply(1, 1) == 1
    assert multiply(-1, 1) == 1 # Fail

def test_divide():
    assert divide(1, 1) == 1
    assert divide(-1, 1) == -1 
    assert divide(0, 1) == 0 
    assert divide(1, 0) == 0 # Fail (Zero Division Error)



