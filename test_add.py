from mathematics import add, multiplicar

def test_add():
    print("Suma")
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(20, 10) == 30


def test_multiplicar():
    print("Multiplicar")
    assert multiplicar(5,5) == 25 # <= error aquí
    assert multiplicar(10, 10) == 100

test_multiplicar()
test_add()