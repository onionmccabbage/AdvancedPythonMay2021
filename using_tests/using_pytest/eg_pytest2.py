# write pytest to exercise named tuple
from collections import namedtuple

# e.g. rate tasks containing summary, owner, boolean 'done' and id
t = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
t.__new__.__defaults__ = (None, None, False, None)

# writing pytests to exercise our named tuple
# invoke as follows
# python -m pytest eg_pytest2.py
# or
# pytest -v eg_pytest2.py

def test_default():
    '''Using no parameters should invoke the defaults'''
    t1 = t()
    t2 = t(None, None, False, None)
    assert t1 == t2

def test_member_access():
    '''Check we can use dot-notation to access members of the tuple'''
    t2 = t('Learn Python', 'Ethel')
    assert t2.summary == 'Learn Python'
    assert t2.owner == 'Ethel'
    assert (t2.done, t2.id) == (False, None)

if __name__ == '__main__':
    t1 = t()
    t2 = t('Learn Python', 'Ethel')
    print(t1, t2)