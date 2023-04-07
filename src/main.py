from nuscenes.nuscenes import NuScenes
from Drawer import Drawer
from Generator import Generator
from NuscData import NuscData


def main():
    nusc = NuScenes(version='v1.0-mini', dataroot='./data', verbose=False)
    for i in range(len(nusc.scene)):
        nuscData: NuscData = NuscData(nusc, i)
        gen: Generator = Generator(nuscData)
        dataCluster = gen.gen_all()
        print(f'{len(dataCluster)} of data generated in scene[{i}]')
        for dataset in dataCluster:
            plt: Drawer = Drawer()
            plt.plot_dataset(dataset)
            plt.plot_dataset(dataset, atk=True)


if __name__ == '__main__':
    main()
