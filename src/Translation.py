
class Translation():
    def __init__(self, trans: list) -> None:
        self.set_translation(trans)

    def set_translation(self, trans: list) -> None:
        self.raw_trans = trans
        self.x = trans[0]
        self.y = trans[1]
        self.z = trans[2]

    def lmul22(self, mat22):
        return Translation([(self.x*mat22[0][0])+(self.y*mat22[0][1]),
                            (self.x*mat22[1][0])+(self.y*mat22[1][1]),
                            self.z])

    def __add__(self, o):
        return Translation([self.x+o.x, self.y+o.y, self.z+o.z])

    def __sub__(self, o):
        return Translation([self.x-o.x, self.y-o.y, self.z-o.z])

    # def __mul__(self, o):
    #     return Translation([self.x*o, self.y*o, self.z*o])

    # def __rmul__(self, o):
    #     return Translation([self.x*o, self.y*o, self.z*o])

    def __repr__(self) -> str:
        return f'Translation: [{self.x}, {self.y}, {self.z}]'
