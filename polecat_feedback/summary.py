from . import codes
from .utils import ansi_clean


class Summary:
    def __init__(self, title):
        self.title = title

    def render_header(self, renderer):
        t = renderer.t
        string = (
            t.bright_black(codes.HORIZONTAL_CODE)*4 +
            ' ' + self.title + ' '
        )
        string += t.bright_black(codes.HORIZONTAL_CODE)*(renderer.w - len(ansi_clean(string)))
        renderer.writeln(string)


class ListSummary(Summary):
    def __init__(self, title, items, empty=None):
        super().__init__(title)
        self.items = items
        self.empty = empty

    def render(self, renderer):
        self.render_header(renderer)
        renderer.list(self.items, self.empty)
