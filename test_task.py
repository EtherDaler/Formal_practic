from homework import task
import pytest


def test_first_case_from_task():
    regex = "ab+c.aba.*.bac.+.+*"
    x = 'a'
    assert 2 == task(regex, x)

def test_second_case_from_task():
    regex = "acb..bab.c.*.ab.ba.+.+*a."
    x = 'c'
    assert 0 == task(regex, x)

def test_unavailable_operator():
    regex = "ab.c+a-"
    x = 'a'
    with pytest.raises(AttributeError) as e:
        task(regex, x)
    message = e.value.args[0]
    assert 'Unexpected command -!' == message

def test_check_1():
    regex = "1a+b.c+"
    x = 'a'
    assert 1 == task(regex, x)

def test_infinity():
    regex = " ab+*"
    x = 'a'
    assert "INF" == task(regex, x)

def test_b_check_add_space():
    regex = "ab + bc + . ac . * + c ."
    x = 'b'
    assert 2 == task(regex, x)

def test_check_simple_prefix():
    regex = "aa.a.c.aa.a.a.c.+"
    x = 'a'
    assert 4 == task(regex, x)

def test_check_simple_prefix_swapped():
    regex = "aa.a.a.c.aa.a.c.+"
    x = 'a'
    assert 4 == task(regex, x)

def test_no_my_letter():
    regex = 'c*'
    x = 'a'
    assert 0 == task(regex, x)


