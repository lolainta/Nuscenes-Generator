import matplotlib.pyplot as plt
import numpy as np
from Dataset import Transform

show_animation = False


class QuinticPolynomial:

    def __init__(self, xs, vxs, axs, xe, vxe, axe, time):
        # calc coefficient of quintic polynomial
        # See jupyter notebook document for derivation of this equation.
        self.a0 = xs
        self.a1 = vxs
        self.a2 = axs / 2.0

        A = np.array([[time ** 3, time ** 4, time ** 5],
                      [3 * time ** 2, 4 * time ** 3, 5 * time ** 4],
                      [6 * time, 12 * time ** 2, 20 * time ** 3]])
        b = np.array([xe - self.a0 - self.a1 * time - self.a2 * time ** 2,
                      vxe - self.a1 - 2 * self.a2 * time,
                      axe - 2 * self.a2])
        x = np.linalg.solve(A, b)

        self.a3 = x[0]
        self.a4 = x[1]
        self.a5 = x[2]

    def calc_point(self, t):
        xt = self.a0 + self.a1 * t + self.a2 * t ** 2 + \
            self.a3 * t ** 3 + self.a4 * t ** 4 + self.a5 * t ** 5
        return xt

    def calc_first_derivative(self, t):
        xt = self.a1 + 2 * self.a2 * t + 3 * self.a3 * \
            t ** 2 + 4 * self.a4 * t ** 3 + 5 * self.a5 * t ** 4
        return xt

    def calc_second_derivative(self, t):
        xt = 2 * self.a2 + 6 * self.a3 * t + 12 * \
            self.a4 * t ** 2 + 20 * self.a5 * t ** 3
        return xt

    def calc_third_derivative(self, t):
        xt = 6 * self.a3 + 24 * self.a4 * t + 60 * self.a5 * t ** 2
        return xt


def quintic_polynomials_planner(src: Transform, sv, sa, dst: Transform, gv, ga, total_time, dt):
    sx = src.translation.x
    sy = src.translation.y
    syaw = src.rotation.yaw

    gx = dst.translation.x
    gy = dst.translation.y
    gyaw = dst.rotation.yaw

    vxs = sv * np.cos(syaw)
    vys = sv * np.sin(syaw)
    vxg = gv * np.cos(gyaw)
    vyg = gv * np.sin(gyaw)

    axs = sa * np.cos(syaw)
    ays = sa * np.sin(syaw)
    axg = ga * np.cos(gyaw)
    ayg = ga * np.sin(gyaw)

    time, rx, ry, ryaw, rv, ra, rj = [], [], [], [], [], [], []

    T = total_time
    xqp = QuinticPolynomial(sx, vxs, axs, gx, vxg, axg, T)
    yqp = QuinticPolynomial(sy, vys, ays, gy, vyg, ayg, T)

    time, rx, ry, ryaw, rv, ra, rj = [], [], [], [], [], [], []

    for t in np.arange(0.0, T + dt, dt):
        time.append(t)
        rx.append(xqp.calc_point(t))
        ry.append(yqp.calc_point(t))

        vx = xqp.calc_first_derivative(t)
        vy = yqp.calc_first_derivative(t)
        v = np.hypot(vx, vy)
        yaw = np.arctan2(vy, vx)
        rv.append(v)
        ryaw.append(yaw)

        ax = xqp.calc_second_derivative(t)
        ay = yqp.calc_second_derivative(t)
        a = np.hypot(ax, ay)
        if len(rv) >= 2 and rv[-1] - rv[-2] < 0.0:
            a *= -1
        ra.append(a)

        jx = xqp.calc_third_derivative(t)
        jy = yqp.calc_third_derivative(t)
        j = np.hypot(jx, jy)
        if len(ra) >= 2 and ra[-1] - ra[-2] < 0.0:
            j *= -1

    return time, rx, ry, ryaw, rv, ra, rj


def plot_arrow(x, y, yaw, length=1.0, width=0.5, fc="r", ec="k"):  # pragma: no cover
    """
    Plot arrow
    """

    if not isinstance(x, float):
        for (ix, iy, iyaw) in zip(x, y, yaw):
            plot_arrow(ix, iy, iyaw)
    else:
        plt.arrow(x, y, length * np.cos(yaw), length * np.sin(yaw),
                  fc=fc, ec=ec, head_width=width, head_length=width)
        plt.plot(x, y)


def main():
    print(__file__ + " start!!")

    sx = 10.0  # start x position [m]
    sy = 10.0  # start y position [m]
    syaw = np.deg2rad(10.0)  # start yaw angle [rad]
    sv = 1.0  # start speed [m/s]
    sa = 0.1  # start accel [m/ss]
    gx = 30.0  # goal x position [m]
    gy = -10.0  # goal y position [m]
    gyaw = np.deg2rad(20.0)  # goal yaw angle [rad]
    gv = 1.0  # goal speed [m/s]
    ga = 0.1  # goal accel [m/ss]
    max_accel = 1.0  # max accel [m/ss]
    max_jerk = 0.5  # max jerk [m/sss]
    dt = 0.1  # time tick [s]

    # 可以沒有a 但v不能為0 (數字再小都無所謂 <0就反方向) 角度+-180
    # sx = 2.17  # start x position [m]
    # sy = 67.48  # start y position [m]
    # syaw = np.deg2rad(-90.0)  # start yaw angle [rad]
    # sv = 0.1  # start speed [m/s]
    # sa = 0.0  # start accel [m/ss]
    # gx = 10.0  # goal x position [m]
    # gy = 47.4  # goal y position [m]
    # gyaw = np.deg2rad(0.0)  # goal yaw angle [rad]
    # gv = 0.1  # goal speed [m/s]
    # ga = 0.0  # goal accel [m/ss]
    # max_accel = 100.0  # max accel [m/ss]
    # max_jerk = 5  # max jerk [m/sss]
    # dt = 0.1  # time tick [s]

    time, x, y, yaw, v, a, j = quintic_polynomials_planner(
        sx, sy, syaw, sv, sa, gx, gy, gyaw, gv, ga, max_accel, max_jerk, dt)
    # print(time, x, y, yaw, v, a, j)
    pos = np.array((x, y)).T
    print("pos:", pos.shape, pos)
    if show_animation:  # pragma: no cover
        plt.plot(x, y, "-r")

        # """
        plt.subplots()
        plt.plot(time, [np.rad2deg(i) for i in yaw], "-r")
        plt.xlabel("Time[s]")
        plt.ylabel("Yaw[deg]")
        plt.grid(True)

        plt.subplots()
        plt.plot(time, v, "-r")
        plt.xlabel("Time[s]")
        plt.ylabel("Speed[m/s]")
        plt.grid(True)

        plt.subplots()
        plt.plot(time, a, "-r")
        plt.xlabel("Time[s]")
        plt.ylabel("accel[m/ss]")
        plt.grid(True)

        plt.subplots()
        plt.plot(time, j, "-r")
        plt.xlabel("Time[s]")
        plt.ylabel("jerk[m/sss]")
        plt.grid(True)
        # """

        plt.show()


if __name__ == '__main__':
    main()
