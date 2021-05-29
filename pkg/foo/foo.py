# --
from ..bar.bar import Bar
# --
class Foo(object):
    def __init__(self):
        self.attr = 'Hello World from Foo'
        self.bar = Bar()
        super().__init__()
    def get_attr(self):
        return self.attr
    def set_attr(self, string):
        self.attr = string
# --