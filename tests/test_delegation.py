import pytest

from delegation import Delegator

class TestDelegator(Delegator):
    def method1(self):
        return 0

class Delegatee(object):
    class_attr1 = 'class_attr1'
    class_attr2 = 'class_attr2'

    def method1(self):
        return 1

    def method2(self):
        return 2

delegator = TestDelegator(Delegatee())

def test_delegation():
    assert delegator.method1() == 0
    assert delegator.method2() == 2
    assert delegator.class_attr1 == 'class_attr1'
    with pytest.raises(AttributeError):
        delegator.unknown_method()
    with pytest.raises(AttributeError):
        delegator.unknown_attribute
