import math
import os
import pytest

from src.lotto import lotto
from src.kalkulator import dodaj, odejmij, pomnoz, podziel,pole_kola, obwod_kola, zapisz_do_pliku
from src.suma_listy import suma_z_listy, suma_z_pliku
from src.r_kwadratowe import rownanie_kwadratowe


def test_lotto():
    wynik = lotto()
    assert isinstance(wynik, list)
    assert len(wynik) == 6
    assert all(1 <= x <= 49 for x in wynik)
    assert len(set(wynik)) == 6
    assert wynik == sorted(wynik)


def test_kalkulator_operacje():
    assert dodaj(2, 3) == 5
    assert odejmij(5, 2) == 3
    assert pomnoz(2, 4) == 8
    assert podziel(8, 2) == 4


def test_kalkulator_kolo():
    assert pole_kola(1) == round(math.pi, 2)
    assert obwod_kola(1) == round(2 * math.pi, 2)


def test_suma_z_listy():
    assert suma_z_listy([1, 2, 3]) == 6
    assert suma_z_listy([]) == 0


def test_suma_z_pliku(tmp_path):
    plik = tmp_path / "liczby.txt"
    plik.write_text("1\n2\n3\n")
    assert suma_z_pliku(str(plik), suma_z_listy) == 6


def test_zapis_do_pliku(tmp_path):
    plik = tmp_path / "wynik.txt"
    zapisz_do_pliku(str(plik), "2+2", 4)
    assert "2+2 = 4" in plik.read_text()


def test_rownanie_kwadratowe(tmp_path):
    os.chdir(tmp_path)
    wynik = rownanie_kwadratowe(1, -3, 2)  # x^2 - 3x + 2 = 0
    assert sorted(wynik) == [1.0, 2.0]
    assert os.path.exists("result.txt")
    assert "1.0" in open("result.txt").read()
