import pytest
from functools import total_ordering


@total_ordering
class Modulo():
    def __init__(self, integer, modulo_number):
        if validate_type_int(modulo_number) and modulo_number > 0:
            self._modulo_number = modulo_number
        else:
            raise TypeError("arg must be an integer")
        if validate_type_int(integer):
            self._integer = integer
        else:
            raise TypeError("arg must be an integer")

    @property
    def modulo_number(self):
        return self._modulo_number

    @property
    def integer(self):
        return self._integer

    @property
    def remainder(self):
        return self._integer % self._modulo_number

    def __add__(self, other):
        if validate_type_modulo(other):
            if same_modulus(self, other):
                mod_rep = (self._integer +
                           other._integer)
                return Modulo(mod_rep, self._modulo_number)
        if validate_type_int(other):
            mod_rep = (self._integer + other)
            return Modulo(mod_rep, self._modulo_number)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if validate_type_modulo(other):
            if same_modulus(self, other):
                self._integer = (
                    self._integer + other._integer)
                return self
        if validate_type_int(other):
            self._integer = (self._integer + other)
            return self

    def __sub__(self, other):
        if validate_type_modulo(other):
            if same_modulus(self, other):
                mod_rep = (self._integer -
                           other._integer)
                return Modulo(mod_rep, self._modulo_number)
        if validate_type_int(other):
            mod_rep = (self._integer - other)
            return Modulo(mod_rep, self._modulo_number)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        if validate_type_modulo(other):
            if same_modulus(self, other):
                self._integer = (
                    self._integer - other._integer)
                return self
        if validate_type_int(other):
            self._integer = (self._integer - other)
            return self

    def __mul__(self, other):
        if validate_type_modulo(other):
            if same_modulus(self, other):
                mod_rep = (self._integer *
                           other._integer)
                return Modulo(mod_rep, self._modulo_number)
        if validate_type_int(other):
            mod_rep = (self._integer * other)
            return Modulo(mod_rep, self._modulo_number)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        if validate_type_modulo(other):
            if same_modulus(self, other):
                self._integer = (
                    self._integer * other._integer)
                return self
        if validate_type_int(other):
            self._integer = (self._integer * other)
            return self

    def __pow__(self, other):
        if validate_type_modulo(other):
            if same_modulus(self, other):
                mod_rep = (self._integer **
                           other._integer)
                return Modulo(mod_rep, self._modulo_number)
        if validate_type_int(other):
            mod_rep = (self._integer ** other)
            return Modulo(mod_rep, self._modulo_number)

    def __rpow__(self, other):
        if validate_type_modulo(other):
            if same_modulus(self, other):
                mod_rep = (other._integer **
                           self._integer)
                return Modulo(mod_rep, self._modulo_number)
        if validate_type_int(other):
            mod_rep = (other ** self._integer)
            return Modulo(mod_rep, self._modulo_number)

    def __ipow__(self, other):
        if validate_type_modulo(other):
            if same_modulus(self, other):
                self._integer = (
                    self._integer ** other._integer)
                return self
        if validate_type_int(other):
            self._integer = (self._integer ** other)
            return self

    def __gt__(self, other):
        if validate_type_modulo(other):
            if same_modulus(self, other):
                return self._integer % self._modulo_number > other._integer % other._modulo_number

        if validate_type_int(other):
            return self._integer % self._modulo_number > other

    def __ge__(self, other):
        return self > other or self == other

    def __int__(self):
        return self._integer % self._modulo_number

    def __repr__(self):
        return f"Modulo Residue = {self._integer % self._modulo_number}"

    def __hash__(self):
        return hash(self.integer)

    def __eq__(self, other):
        if validate_type_modulo(other):
            return self._modulo_number == other._modulo_number and self._integer % self.modulo_number == other._integer % other._modulo_number
        if validate_type_int(other):
            return self._integer % self.modulo_number == other % self._modulo_number
        return False


def validate_type_int(value):
    return isinstance(value, int)


def validate_type_modulo(value):
    return isinstance(value, Modulo)


def same_modulus(modulo1, modulo2):
    if validate_type_modulo(modulo1) and validate_type_modulo(modulo2):
        return modulo1.modulo_number == modulo2.modulo_number
