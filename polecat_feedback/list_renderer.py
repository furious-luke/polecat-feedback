from . import codes


class ListRenderer:
    def __init__(self, renderer):
        self.r = renderer
        self.t = renderer.t

    def render(self, items, empty=None):
        r = self.r
        if items:
            for item in items:
                r.writeln(' ' + codes.BULLET_CODE + ' ' + item)
        else:
            empty = empty or 'No items'
            self.writeln(f'  {empty}')
