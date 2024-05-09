import unittest
from login import login

class TestLoginFunction(unittest.TestCase):
    def test_login_success(self):
        # Prueba para inicio de sesión exitoso
        username = "dani"
        password = "123"
        result = login(username, password)
        self.assertEqual(result, "Sesion iniciada")

    def test_login_failure_username(self):
        # Prueba para nombre de usuario incorrecto
        username = "usuario_incorrecto"
        password = "123"
        result = login(username, password)
        self.assertEqual(result, "Contraseña o usuario incorrecto")

    def test_login_failure_password(self):
        # Prueba para contraseña incorrecta
        username = "dani"
        password = "contraseña_incorrecta"
        result = login(username, password)
        self.assertEqual(result, "Contraseña o usuario incorrecto")

    def test_login_failure_both(self):
        # Prueba para nombre de usuario y contraseña incorrectos
        username = "usuario_incorrecto"
        password = "contraseña_incorrecta"
        result = login(username, password)
        self.assertEqual(result, "Contraseña o usuario incorrecto")

if __name__ == '__main__':
    unittest.main()
