import pytest


def div(a, b):
    #todo：健壮性、异常处理
    return a/b


# @pytest.mark.happy
# def test_div_int():
#     assert div(10,2) == 5
#     assert div(10,5) == 2
#     assert div(100.1,5) == 2
#
# @pytest.mark.exception
# @pytest.mark.parametrize()
# def test_div_float():
#     assert div(10,3) == 3.3333333333333335
#     assert div(10.2,0.2) == 50.99999999999999
#
#
#
# @pytest.mark.exception
# def test_div_expection():
#     assert div(1,3)
#
# @pytest.mark.exception
# def test_div_zero():
#     assert div(10,0) ==None

@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,expection",{
    (10,2,5),
    (8,4,2),
    (10.1,0.2,50.49999999999999)

})
def test_div_int_param(number1,number2,expection):
    assert div(number1,number2) == expection

    x=2
    print(x)