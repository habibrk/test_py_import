# --
class Bar(object):
    def __init__(self):
        self.attr = 'Hello World from Bar'
        super().__init__()
    def get_attr(self):
        return self.attr
    def set_attr(self, string):
        self.attr = string
# --