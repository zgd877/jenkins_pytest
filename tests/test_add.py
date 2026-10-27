# tests/test_add.py
import pytest


def add(a, b):
    """被测的加法函数"""
    return a + b


# 基础用例
def test_add_two_positive_numbers():
    assert add(1, 2) == 3


def test_add_positive_and_negative():
    assert add(10, -4) == 6


def test_add_two_negative_numbers():
    assert add(-1, -1) == -2


def test_add_with_zero():
    assert add(0, 0) == 0


# 参数化：一个函数批量覆盖多组输入，失败时能看到具体是哪组数据挂了
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (-5, 5, 0),
    (100, -100, 0),
    (0.1, 0.2, pytest.approx(0.3)),   # 浮点数比较用 approx 避免精度问题
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


# 异常场景：验证传入非法类型时会抛 TypeError
def test_add_invalid_type():
    with pytest.raises(TypeError):
        add("1", 2)   # 字符串 + 整数 → TypeError
