import pytest
import random


# tests for list
@pytest.fixture
def empty_list():
    return list()


def some_list():
    lst = list()
    n = random.choice(range(1, 21))
    for i in range(n):
        lst.append(random.random() * random.randint(0, 10000))
    return lst


def test_empty(empty_list):
    assert len(empty_list) == 0


@pytest.mark.parametrize("const,lst", [(1, some_list()), ("tEsT009", some_list()), (-190.4, some_list())])
def test_add(const, lst):
    ln0 = len(lst)
    lst.append(const)
    assert len(lst) == ln0 + 1
    assert lst[-1] == const


def test_remove(empty_list):
    const, const1 = 9, 10
    lst = empty_list
    lst.append(const1)
    ln0 = len(lst)
    with pytest.raises(ValueError):
        lst.remove(const)
    assert len(lst) == ln0
    lst.remove(const1)
    assert ln0 - 1 == len(lst)


@pytest.mark.parametrize("test_input, expected", [([], []), ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), ([0], [0]), ([900, -100,
                                                                                                              2343,
                                                                                                              6348,
                                                                                                              -190.23,
                                                                                                              98, 555],
                                                                                                             [-190.23,
                                                                                                              -100, 98,
                                                                                                              555, 900,
                                                                                                              2343,
                                                                                                              6348])])
def test_sort(test_input, expected):
    test_input.sort()
    assert test_input == expected


def test_tricky_sort():
    with pytest.raises(TypeError):
        [-190.23, -100, 98, 555, 900, 2343, 6348, 'TEST'].sort()


# tests for tuple
@pytest.fixture
def empty_tuple():
    return tuple()


@pytest.fixture
def some_tuple():
    lst = list()
    n = random.choice(range(1, 21))
    for i in range(n):
        lst.append(random.random() * random.randint(0, 10000))
    return tuple(lst)


def test_empty(empty_list):
    assert len(empty_list) == 0


@pytest.mark.parametrize("test_input,expected", [(tuple(), ()), (tuple([1, 2, -1]), (1, 2, -1)),
                                                 (tuple(['1', 290, -146.7]), ('1', 290, -146.7))])
def test_add(test_input, expected):
    assert test_input == expected


def test_change_tuple(some_tuple):
    with pytest.raises(TypeError):
        some_tuple[0] = 100
