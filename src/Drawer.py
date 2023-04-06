import matplotlib.pyplot as plt
import numpy as np
from Dataset import Dataset
from Transform import Transform
from Translation import Translation


class Drawer():
    def __init__(self) -> None:
        # plt.gcf().canvas.mpl_connect('key_release_event',
        #                              lambda event: [exit(0) if event.key == 'escape' else None])
        self.fig, self.ax = plt.subplots(figsize=(20, 20))
        self.delay = 0.01
        self.ax.set_xticks(range(1720, 1723), fontsize=20)
        self.ax.set_yticks(range(2668, 2672), fontsize=20)

    def plot_arrow(self, x, y, yaw, length=2.0, width=1, fc="r", ec="k"):
        self.ax.arrow(x, y, length * np.cos(yaw), length * np.sin(yaw),
                      fc=fc, ec=ec, head_width=width, head_length=width)
        self.ax.plot(x, y)

    def plot_seg(self, p1: Translation, p2: Translation, col='green'):
        self.ax.plot([p1.x, p2.x], [p1.y, p2.y], 'o--', color=col)
        self.ax.scatter(p1.x, p1.y, c=col)
        self.ax.scatter(p2.x, p2.y, c=col)

    def plot_box(self, bound, col='green'):
        for i in range(4):
            self.plot_seg(bound[i], bound[(i+1) % 4], col=col)

    def plot_car(self, d: Transform, col='green'):
        x = d.translation.x
        y = d.translation.y
        yaw = d.rotation.yaw
        bnd = d.bound
        self.plot_box(bnd, col=col)
        self.plot_arrow(x, y, yaw, fc=col)

    def plot_single_data(self, data: Transform):
        # self.plot_car(data.translation.x)
        pass

    def plot_data(self, dataset: Dataset, atk=False):
        for data in dataset:
            plt.cla()
            self.plot_car(dataset[0].ego, col='blue')
            self.plot_car(data.ego, col='blue')
            self.plot_car(dataset[-1].ego, col='blue')

            self.plot_car(dataset[0].npc)
            self.plot_car(data.npc)
            self.plot_car(dataset[-1].npc)
            if atk:
                self.plot_car(dataset[0].atk)
                self.plot_car(data.atk)
                self.plot_car(dataset[-1].atk)

            plt.pause(self.delay)

    def show(self):
        plt.show()
