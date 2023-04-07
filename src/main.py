from nuscenes.nuscenes import NuScenes
from Generator import Generator
from Drawer import Drawer
from NuscData import NuscData


def main():
    nusc = NuScenes(version='v1.0-mini', dataroot='./data', verbose=False)
    nuscData: NuscData = NuscData(nusc, 5)
    gen: Generator = Generator(nuscData)
    plt: Drawer = Drawer()
    dataCluster = gen.gen_all()
    for dataSet in dataCluster:
        plt.plot_dataset(dataSet, atk=True)


if __name__ == '__main__':
    main()
