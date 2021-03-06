import os
import pytest
from practice1 import solve, nfa
import io


def test_1():
    test_input = io.StringIO('acb..bab.c.*.ab.ba.+.+*a. abbaa')
    ans = solve(test_input)
    assert ans == 4


def test_2():
    test_input = io.StringIO('ab+ a')
    ans = solve(test_input)
    assert ans == 1


def test_3():
    test_input = io.StringIO('ab+c.aba..bac.+.+* babc')
    ans = solve(test_input)
    assert ans == 2


def test_4():
    test_input = io.StringIO('ab+* aaaaa')
    ans = solve(test_input)
    assert ans == 5


def test_5():
    test_input = io.StringIO('ab. aa')
    ans = solve(test_input)
    assert ans == 0


def test_6():
    test_input = io.StringIO('ab. ab')
    ans = solve(test_input)
    assert ans == 2


def test_7():
    test_input = io.StringIO('a** aaaaa')
    ans = solve(test_input)
    assert ans == 5


def test_8():
    test_input = io.StringIO('abc.. ab')
    ans = solve(test_input)
    assert ans == 0


def test_9():
    test_input = io.StringIO('abc.. abc')
    ans = solve(test_input)
    assert ans == 3


def test_10():
    test_input = io.StringIO('ab+c. ac')
    ans = solve(test_input)
    assert ans == 2


def test_11():
    with pytest.raises(ValueError):
        test_input = io.StringIO('abcd ac')
        solve(test_input)


def test_11():
    with pytest.raises(IndexError):
        test_input = io.StringIO('abc')
        solve(test_input)


def test_12():
    with pytest.raises(IndexError):
        test_input = io.StringIO('.. a')
        solve(test_input)


def test_13():
    test_input = io.StringIO('ab+c. ac')
    test_output = io.StringIO()
    solve(test_input, test_output)
    content = test_output.getvalue()
    assert content == '2\n'


def test_14():
    with pytest.raises(EOFError):
        test_input = io.StringIO('')
        solve(test_input)


def test_15():
    reg = 'ab+c.'
    string = 'ac'
    nfa_global = nfa.NFA(reg)
    nfa_global._make_dump()
    assert True is os.path.isfile('./logs/dump.log')


def test_16():
    reg = 'ab+c.'
    string = 'ac'
    nfa_global = nfa.NFA(reg)
    nfa_global._make_dump()
    assert True is os.path.isfile('./snapshots/dump.log/dump.log')
