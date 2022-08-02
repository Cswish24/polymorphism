from main import Modulo, validate_type_int, validate_type_modulo
import pytest
import unittest


def test_validate_int():
    assert validate_type_int(5) is True


def test_validate_str():
    assert validate_type_int('hi') is False


def test_validate_float():
    assert validate_type_int(1.1) is False


def test_validate_modulo():
    assert validate_type_modulo(Modulo(3, 5))


def test_validate_modulo_int():
    assert validate_type_modulo(5) == False


class Test__init__(unittest.TestCase):

    modulo = Modulo(5, 3)
    modulo2 = Modulo(8, 3)
    modulo3 = Modulo(7, 3)

    def test_instance_modulo_number_true(self):
        assert self.modulo.modulo_number == 3

    def test_instance_modulo_number_false(self):
        assert self.modulo.modulo_number != 2

    def test_instance_modulo_number_true(self):
        assert self.modulo.modulo_number == 3

    def test_instance_modulo_number_false(self):
        assert self.modulo.modulo_number != 2

    def test_modulos_equal_true(self):
        assert self.modulo == self.modulo2

    def test_modulos_equal_false(self):
        assert self.modulo != self.modulo3

    def test_modulus_not_eq_but_mod_eq(self):
        assert self.modulo != Modulo(6, 4)

    def test_modulus_eq_to_int(self):
        assert self.modulo == 8

    def test_modulus_not_eq_to_int(self):
        assert self.modulo != 7

    def test_add_modulos(self):
        the_sum = self.modulo + Modulo(7, 3)
        assert the_sum == 0

    def test_add_modulo_to_int(self):
        the_sum = self.modulo + 5
        assert the_sum == 1

    def test_radd_int_to_modulo(self):
        the_sum = 5 + self.modulo
        assert the_sum == 1

    def test_iadd_int_to_modulo(self):
        new_modulo = Modulo(5, 3)
        new_modulo += 1
        assert new_modulo == 0

    def test_sub_modulos(self):
        the_sum = self.modulo - Modulo(8, 3)
        assert the_sum == 0

    def test_sub_int_from_modulo(self):
        the_sum = self.modulo - 7
        assert the_sum == 1

    def test_rsub_modulo_from_int(self):
        the_sum = 5 - self.modulo
        assert the_sum == 0

    def test_isub_int_to_modulo(self):
        new_modulo = Modulo(5, 3)
        new_modulo -= 1
        assert new_modulo == 1

    def test_mul_int_from_modulo(self):
        the_sum = self.modulo * 2
        assert the_sum == 1

    def test_rmul_modulo_from_int(self):
        the_sum = 2 * self.modulo
        assert the_sum == 1

    def test_imul_int_to_modulo(self):
        new_modulo = Modulo(5, 3)
        new_modulo *= 2
        assert new_modulo == 1

    def test_pow_int_from_modulo(self):
        the_sum = self.modulo ** 2
        assert the_sum == 1

    def test_rpow_modulo_from_int(self):
        the_sum = 2 ** self.modulo
        assert the_sum == 2

    def test_ipow_int_to_modulo(self):
        new_modulo = Modulo(5, 3)
        new_modulo **= 2
        assert new_modulo == 1

    def test_int(self):
        assert int(self.modulo) == 2

    def test_gt_other_modulo(self):
        assert self.modulo > Modulo(4, 3)

    def test_lt_other_modulo(self):
        assert Modulo(4, 3) < self.modulo

    def test_lt_eq_other_modulo(self):
        assert Modulo(4, 3) <= self.modulo

    def test_gt_other_int(self):
        assert self.modulo > 1

    def test_lt_other_int(self):
        assert Modulo(4, 3) < 2

    def test_lt_eq_other_int(self):
        assert Modulo(4, 3) <= 1

    def test_hash_it(self):
        the_hash = hash(self.modulo)
        assert isinstance(the_hash, int)
