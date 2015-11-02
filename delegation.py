class Delegator(object):
    def __init__(self, delegatee):
        self._delegatee = delegatee

    def __getattr__(self, name):
        return getattr(self._delegatee, name)