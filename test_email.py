import unittest
from email import este_valid
import time

# assert 2 == 3, "Aceste 2 nu sunt egale.../:)"


class TestValidareEmail(unittest.TestCase):

    def test_fara_insemnatate(self):
        self.assertEqual(2, 2, "Cele doua trebuie sa fie egale...!!!")

    def test_de_test(self):
        time.sleep(1)
        self.assertNotEqual(2, 3, "cele 2 nu trebuie sa fie egale..!!!")


    def test_contine_coada_de_maimuta(self):
        # self.assertTrue(este_valid("@."), "Trebuie sa contina @")
        self.assertFalse(este_valid("dhasgdjhasg"), "Trebuie sa contina @")

    def test_contine_punct(self):
        # self.assertTrue(este_valid("@."), "Trebuie sa contina .")
        self.assertFalse(este_valid("dasdas@com"), "Trebuie sa contina .")
        
    def test_are_ceva_inainte_de_coada_de_maimuta(self):
        self.assertFalse(este_valid("@ceva.ro"), "Trebuie sa contina ceva inainte de @")

    def test_caractere_neobisnuite(self):
        self.assertFalse(este_valid("$@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid("#@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid("!@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid(">@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid("(@ceva.ro"), "Trebuie sa nu contina caractere speciale")
        self.assertFalse(este_valid(")@ceva.ro"), "Trebuie sa nu contina caractere speciale")

        self.assertFalse(este_valid(" @ceva.ro"), "Trebuie sa nu contina caractere speciale")

        self.assertFalse(este_valid("?@ceva.ro"), "Trebuie sa nu contina caractere speciale")


    def test_numar_caractere(self):
        rezultat = este_valid("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@ceva.ro")

        self.assertFalse(rezultat, "Numarul maxim este 64 de charactere")


    def test_are_ceva_dupa_punct(self):
        self.assertFalse(este_valid("a@."), "Trebuie sa aibe 2 caractere cel putin")
        self.assertFalse(este_valid("a@.--"))

        self.assertFalse(este_valid("a@.tt."))

        # TODO:
        # self.assertFalse(este_valid("a@..tt"))
        
        # TODO:
        # self.assertFalse(este_valid("a@@.tt"))

        # TODO:
        self.assertFalse(este_valid("a@-.tt"))



if _name_ == "_main_":
    unittest.main()