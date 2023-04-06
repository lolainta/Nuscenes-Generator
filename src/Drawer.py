import matplotlib.pyplot as plt
import numpy as np
from Dataset import Dataset
from Transform import Transform
from Translation import Translation

data = [{'time': 1538448744431006, 'ego_x': 1871.1632105355122, 'ego_y': 2484.168001779657, 'ego_yaw': 2.2975842944000093, 'atk_x': 1904.106, 'atk_y': 2453.654, 'atk_yaw': 2.2992618500006277}, {'time': 1538448745041182, 'ego_x': 1866.0596160912262, 'ego_y': 2490.0496714097735, 'ego_yaw': 2.283716651657141, 'atk_x': 1897.838, 'atk_y': 2460.219, 'atk_yaw': 2.304246509812588}, {'time': 1538448745566392, 'ego_x': 1861.683096689233, 'ego_y': 2495.220377029238, 'ego_yaw': 2.2749049623919535, 'atk_x': 1892.616, 'atk_y': 2465.688, 'atk_yaw': 2.3083995607683168}, {'time': 1538448746021671, 'ego_x': 1857.8887754008674, 'ego_y': 2499.7431798821476, 'ego_yaw': 2.275350089611816, 'atk_x': 1887.387, 'atk_y': 2471.164, 'atk_yaw': 2.3125573807237103}, {'time': 1538448746551897, 'ego_x': 1853.497403809235, 'ego_y': 2504.9744192825738, 'ego_yaw': 2.2740446768035025, 'atk_x': 1882.247, 'atk_y': 2476.72, 'atk_yaw': 2.3167151425205708}, {'time': 1538448747011864, 'ego_x': 1849.7728640807823, 'ego_y': 2509.4434944587383, 'ego_yaw': 2.2748550848086677, 'atk_x': 1877.169, 'atk_y': 2482.472, 'atk_yaw': 2.3254527886850207}, {'time': 1538448747537064, 'ego_x': 1845.5544041081191, 'ego_y': 2514.4808687967225, 'ego_yaw': 2.2743609641575264, 'atk_x': 1872.017, 'atk_y': 2488.17, 'atk_yaw': 2.3167271579315027}, {'time': 1538448748067927, 'ego_x': 1841.3837643742459, 'ego_y': 2519.439761199228, 'ego_yaw': 2.2786301769012467, 'atk_x': 1866.733, 'atk_y': 2493.822, 'atk_yaw': 2.2294486799208544}, {'time': 1538448748522365, 'ego_x': 1837.7747212273794, 'ego_y': 2523.6961861783584, 'ego_yaw': 2.280870821781225, 'atk_x': 1861.795, 'atk_y': 2499.573, 'atk_yaw': 2.2556236985648055}, {'time': 1538448749052897, 'ego_x': 1833.653602005091, 'ego_y': 2528.565409363614, 'ego_yaw': 2.277657560465937, 'atk_x': 1856.802, 'atk_y': 2505.292, 'atk_yaw': 2.2469019724407975}, {'time': 1538448749582569, 'ego_x': 1829.5377170430816, 'ego_y': 2533.401601690301, 'ego_yaw': 2.281276973251006, 'atk_x': 1851.881, 'atk_y': 2511.116, 'atk_yaw': 2.2294486799208544}, {'time': 1538448750037341, 'ego_x': 1826.0248414900825, 'ego_y': 2537.505688781667, 'ego_yaw': 2.2836245460594577, 'atk_x': 1847.008, 'atk_y': 2516.775, 'atk_yaw': 2.261437532570829}, {'time': 1538448750563041, 'ego_x': 1822.0281889892972, 'ego_y': 2542.264533991602, 'ego_yaw': 2.2751619847201003, 'atk_x': 1842.099, 'atk_y': 2522.572, 'atk_yaw': 2.258535356995005}, {'time': 1538448751017637, 'ego_x': 1818.6001484890826, 'ego_y': 2546.392947405514, 'ego_yaw': 2.26772432491735, 'atk_x': 1837.268, 'atk_y': 2528.298, 'atk_yaw': 2.2469019724407975}, {'time': 1538448751548372, 'ego_x': 1814.5539658070088, 'ego_y': 2551.2952369115947, 'ego_yaw': 2.2719277721246427, 'atk_x': 1832.448, 'atk_y': 2534.157, 'atk_yaw': 2.2527154490978365}, {'time': 1538448752073384, 'ego_x': 1810.5222607297292, 'ego_y': 2556.08990351841, 'ego_yaw': 2.2784812005505817, 'atk_x': 1827.682, 'atk_y': 2539.758, 'atk_yaw': 2.2585355779953176}, {'time': 1538448752528409, 'ego_x': 1806.9871277477664, 'ego_y': 2560.2510357464944, 'ego_yaw': 2.277997093603733, 'atk_x': 1822.944, 'atk_y': 2545.421, 'atk_yaw': 2.264355264960741}, {'time': 1538448753063965, 'ego_x': 1802.8809607128546, 'ego_y': 2565.1078557153724, 'ego_yaw': 2.2762839223738554, 'atk_x': 1818.448, 'atk_y': 2550.972, 'atk_yaw': 2.2469019724407975}, {'time': 1538448753519024, 'ego_x': 1799.3754835929801, 'ego_y': 2569.2959136525096, 'ego_yaw': 2.2717246943180407, 'atk_x': 1813.692, 'atk_y': 2556.546, 'atk_yaw': 2.2454470626297685}, {'time': 1538448754049383, 'ego_x': 1795.27817194466, 'ego_y': 2574.214628566403, 'ego_yaw': 2.26793750171495, 'atk_x': 1809.049, 'atk_y': 2562.22, 'atk_yaw': 2.243990459867108}, {
    'time': 1538448754579403, 'ego_x': 1791.225119014003, 'ego_y': 2579.0990974186993, 'ego_yaw': 2.266537087562566, 'atk_x': 1804.303, 'atk_y': 2567.755, 'atk_yaw': 2.242533892070747}, {'time': 1538448755034537, 'ego_x': 1787.721959266074, 'ego_y': 2583.329528521378, 'ego_yaw': 2.267035678694279, 'atk_x': 1799.589, 'atk_y': 2573.413, 'atk_yaw': 2.264355264960741}, {'time': 1538448755559724, 'ego_x': 1783.6837121814729, 'ego_y': 2588.188541728839, 'ego_yaw': 2.2685539277176483, 'atk_x': 1794.9, 'atk_y': 2579.135, 'atk_yaw': 2.2556235195949963}, {'time': 1538448756020162, 'ego_x': 1780.1294848738783, 'ego_y': 2592.4623619449458, 'ego_yaw': 2.272823491478682, 'atk_x': 1790.195, 'atk_y': 2584.876, 'atk_yaw': 2.24686282840726}, {'time': 1538448756550113, 'ego_x': 1776.0521919004227, 'ego_y': 2597.2608737039736, 'ego_yaw': 2.2780539876082524, 'atk_x': 1785.537, 'atk_y': 2590.56, 'atk_yaw': 2.2381895155658382}, {'time': 1538448757080243, 'ego_x': 1772.029447588098, 'ego_y': 2602.035111702061, 'ego_yaw': 2.271333770214206, 'atk_x': 1780.844, 'atk_y': 2596.289, 'atk_yaw': 2.2294486799208544}, {'time': 1538448757535385, 'ego_x': 1768.6368315887385, 'ego_y': 2606.1052636773907, 'ego_yaw': 2.2669270646867, 'atk_x': 1776.114, 'atk_y': 2602.037, 'atk_yaw': 2.2338130573558477}, {'time': 1538448758065627, 'ego_x': 1764.720290811752, 'ego_y': 2610.862720912205, 'ego_yaw': 2.2613849056173896, 'atk_x': 1771.449, 'atk_y': 2607.758, 'atk_yaw': 2.2381776268795384}, {'time': 1538448758515707, 'ego_x': 1761.403653991183, 'ego_y': 2614.9227769103436, 'ego_yaw': 2.2552094880148505, 'atk_x': 1766.828, 'atk_y': 2613.425, 'atk_yaw': 2.2425375862744996}, {'time': 1538448759050884, 'ego_x': 1757.4839780782318, 'ego_y': 2619.784393036134, 'ego_yaw': 2.249616991416018, 'atk_x': 1762.264, 'atk_y': 2619.019, 'atk_yaw': 2.2469019724407975}, {'time': 1538448759581144, 'ego_x': 1753.5725839637132, 'ego_y': 2624.7108976629206, 'ego_yaw': 2.246543618684896, 'atk_x': 1757.783, 'atk_y': 2624.694, 'atk_yaw': 2.2469019724407975}, {'time': 1538448760031478, 'ego_x': 1750.2133348589527, 'ego_y': 2628.940940276, 'ego_yaw': 2.2458732673450448, 'atk_x': 1753.339, 'atk_y': 2630.323, 'atk_yaw': 2.2469019724407975}, {'time': 1538448760561438, 'ego_x': 1746.2017745614726, 'ego_y': 2634.0367671771273, 'ego_yaw': 2.242982190810974, 'atk_x': 1748.899, 'atk_y': 2635.947, 'atk_yaw': 2.2469019724407975}, {'time': 1538448761016536, 'ego_x': 1742.7959704508287, 'ego_y': 2638.3748071630944, 'ego_yaw': 2.246343154627782, 'atk_x': 1744.464, 'atk_y': 2641.564, 'atk_yaw': 2.2469019724407975}, {'time': 1538448761551848, 'ego_x': 1738.7528949620084, 'ego_y': 2643.468609863526, 'ego_yaw': 2.2466787244316877, 'atk_x': 1740.108, 'atk_y': 2647.084, 'atk_yaw': 2.2469019724407975}, {'time': 1538448762082305, 'ego_x': 1734.7802295412616, 'ego_y': 2648.4908839764494, 'ego_yaw': 2.24630130773457, 'atk_x': 1735.637, 'atk_y': 2652.706, 'atk_yaw': 2.2469019724407975}, {'time': 1538448762537043, 'ego_x': 1731.3808376465913, 'ego_y': 2652.8201122157093, 'ego_yaw': 2.2406291715068027, 'atk_x': 1731.17, 'atk_y': 2658.322, 'atk_yaw': 2.2469019724407975}, {'time': 1538448763062240, 'ego_x': 1727.487203584785, 'ego_y': 2657.7696989931383, 'ego_yaw': 2.2394652106118396, 'atk_x': 1726.699, 'atk_y': 2663.944, 'atk_yaw': 2.2469019724407975}, {'time': 1538448763517391, 'ego_x': 1724.1095065206769, 'ego_y': 2662.089606156278, 'ego_yaw': 2.2349937242200832, 'atk_x': 1722.338, 'atk_y': 2669.645, 'atk_yaw': 2.2469019724407975}, {'time': 1538448764047556, 'ego_x': 1720.2614886066951, 'ego_y': 2667.0719561351943, 'ego_yaw': 2.2290107093844322, 'atk_x': 1717.987, 'atk_y': 2675.333, 'atk_yaw': 2.2469019724407975}]


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

    def plot_data(self, dataset: Dataset):
        for data in dataset:
            plt.cla()
            self.plot_car(dataset[0].ego, col='blue')
            self.plot_car(data.ego, col='blue')
            self.plot_car(dataset[-1].ego, col='blue')

            self.plot_car(dataset[0].atk)
            self.plot_car(data.atk)
            self.plot_car(dataset[-1].atk)
            plt.pause(self.delay)

    def show_animation(self, org: Dataset, res):
        time, rx, ry, ryaw, rv, ra, rj = res
        # print(len(time), time, rx, ry, ryaw, rv, ra, rj)
        assert len(time) == len(org), f'{len(time)=} not equal {len(org)=}'
        last = min(len(time), len(org))
        for i in range(last):
            plt.cla()
            # plt.grid(True)
            # plt.axis("equal")
            # self.plot_arrow(sx, sy, syaw)
            # self.plot_arrow(gx, gy, gyaw)
            self.plot_car(org[0].ego, col='blue')
            self.plot_car(org[i].ego, col='blue')
            self.plot_car(org[-1].ego, col='blue')

            self.plot_car(org[0].atk)
            self.plot_car(org[-1].atk)

            self.plot_car(Transform([rx[0], ry[0], 0], ryaw[0]))
            self.plot_car(Transform([rx[i], ry[i], 0], ryaw[i]))
            self.plot_car(Transform([rx[-1], ry[-1], 0], ryaw[-1]))

            plt.pause(self.delay)

    def show(self):
        plt.show()
