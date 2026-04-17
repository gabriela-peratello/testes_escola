import pytest
from boletim.calculos import calcular_media


def test_lista_vazia():
    with pytest.raises(ValueError, matc = "A lista de notas não pode estar vazia"):
        calcular_media("")

def test_string_como_lista():
    with pytest.raises(TypeError, match="As notas devem ser uma lista ´numérica"):
        calcular_media(["um", "oito"])

def test_notas_numericas_e_nao_numericas():
    with pytest.raises(TypeError, match="As notas deve ser uma lista numérica")
    calcular_media(10, "cinco", 4)

def test_notas_maiores_dez():
    with pytest.raises(ValueError):
        calcular_media([11, 10])


def test_notas_menoresq_0():
    with pytest.raises(ValueError):
        calcular_media([11, 100])

def test_notas_menoresq_0():
    with pytest.raises(ValueError):
        calcular_media([])