import unittest
from greeter import Greeter

class TestGreeter(unittest.TestCase):
    def test_greet_morning(self):
        greeter = Greeter()
        self.assertEqual(greeter.greet("sara"), "Good morning Sara")
    
    # Ejemplo de prueba 1
def test_greet_morning():
    greeter = Greeter()
    assert greeter.greet("Alice", current_hour=10) == "Good morning Alice"

    # Ejemplo de prueba 2
def test_greet_afternoon():
    greeter = Greeter()
    assert greeter.greet("Bob", current_hour=14) == "Good afternoon Bob"

    # Ejemplo de prueba 3
def test_greet_evening():
    greeter = Greeter()
    assert greeter.greet("Charlie", current_hour=19) == "Good evening Charlie"

    # Ejemplo de prueba 4
def test_greet_night():
    greeter = Greeter()
    assert greeter.greet("David", current_hour=23) == "Good night David"
    
if __name__ == '__main__':
    unittest.main()