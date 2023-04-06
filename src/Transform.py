from Rotation import Rotation
from Translation import Translation
from numpy import cos, sin, pi, deg2rad


class Transform():
    def __init__(self, translation: list, rotation) -> None:
        self.translation = Translation(translation)
        self.rotation = Rotation(rotation)
        self.width = 2
        self.length = 4
        self.bound = self.get_bound()

    def get_bound(self):
        x = self.translation.x
        y = self.translation.y
        yaw = self.rotation.yaw
        width = self.width
        length = self.length
        tr = Translation([x+length/2*cos(yaw)+width/2*cos(yaw-pi/2),
                          y+length/2*sin(yaw)+width/2*sin(yaw-pi/2),
                          0])
        tl = Translation([x+length/2*cos(yaw)-width/2*cos(yaw-pi/2),
                          y+length/2*sin(yaw)-width/2*sin(yaw-pi/2),
                          0])
        br = Translation([x-length/2*cos(yaw)+width/2*cos(yaw-pi/2),
                          y-length/2*sin(yaw)+width/2*sin(yaw-pi/2),
                          0])
        bl = Translation([x-length/2*cos(yaw)-width/2*cos(yaw-pi/2),
                          y-length/2*sin(yaw)-width/2*sin(yaw-pi/2),
                          0])
        return [tr, tl, bl, br]

    def flip(self) -> None:
        width = self.width
        length = self.length
        yaw = self.rotation.yaw
        self.translation.x += width*cos(yaw-pi/2)
        self.translation.y += width*sin(yaw-pi/2)
        self.bound = self.get_bound()

    def forward(self, dis: float) -> None:
        yaw = self.rotation.yaw
        self.translation.x += dis*cos(yaw)
        self.translation.y += dis*sin(yaw)
        self.bound = self.get_bound()

    def rotate(self, deg: float, org=None) -> None:
        org = self.translation if org is None else org
        rad = deg2rad(deg)
        self.rotation.yaw += rad
        self.translation = self._rotate_point(self.translation, org, rad)
        self.bound = self.get_bound()

    def _rotate_point(self, p, org=(0, 0), rad=0):
        mat = [[cos(rad), cos(rad+pi/2)],
               [sin(rad),  sin(rad+pi/2)]]
        return (p-org).lmul22(mat) + org

    def __repr__(self):
        return f'Transform:\n\t{self.translation}\n\t{self.rotation}'
