import pytest
import math as m
@pytest.mark.parametrize("list", [[5,5,98], [-3.155,0,100], [0,2.5,0], [-5,-5,0.1]])
def test_checkListElemOnDigit(list):
    for i in list:
        assert type(i) == int or type(i) == float

@pytest.mark.parametrize("list", [[5,5,5], [-100,0,100], [0,0,0], [-5,-5,-5]])
def test_checkListOnPositiveSummElem(list):
    summ = 0
    for i in list:
        summ += i
    assert summ > 0

@pytest.mark.parametrize("list", [[5,5,5], [-100,0,100], [0,0,0], [-5,-5,-5]])
def test_checkListElemHaveIntegerEvolution(list):
    for i in list:
        try:
            assert int(i ** (1/2))
        except ValueError:
            pass

@pytest.mark.parametrize("val", ["123", "175.5", "asdasda"])
def test_checkInputValueOnFloatType(val):
    assert float(val)

@pytest.mark.parametrize("val", [10, 105])
def test_squareOfCircle(val):
    assert (val ** 2 * m.pi) > 90

@pytest.mark.parametrize("val", [20])
def test_checkSin(val):
    assert m.sin(val) > 0.5