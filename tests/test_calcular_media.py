import pytest 

from boletim.calculos import calcular_media

def test_string():
    with pytest.raises(TypeError, match="Digite um número."):
        calcular_media(["nota"])

def test_inteiro():
    assert calcular_media([8,10]) == 9.0

def decimais():
    assert calcular_media([4.5, 7.8, 5.9])

def test_negativos():
    with pytest.raises(ValueError, match="Valor incorreto."):
        calcular_media([-15])
        
def test_uma_nota():
    with pytest.raises(ValueError, match="Adicione mais de uma nota."):
        calcular_media([8])


def test_maiores_dez():
       with pytest.raises(ValueError, match="Valor Incorreto"):
        calcular_media([20])

   


def test_decint():
    assert calcular_media([4.8, 7]) == 5.9