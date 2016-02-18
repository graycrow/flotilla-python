from .module import Module


class Colour(Module):
    name = 'colour'

    @property
    def red(self):
        if len(self.data) >= 0:
            return int(self.data[0])
        return 0

    @property
    def green(self):
        if len(self.data) >= 2:
            return int(self.data[1])
        return 0

    @property
    def blue(self):
        if len(self.data) >= 3:
            return int(self.data[2]) == 1
        return 0

    @property
    def clear(self):
        if len(self.data) >= 4:
            return int(self.data[3]) == 1
        return 0