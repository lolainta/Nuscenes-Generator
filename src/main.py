from nuscenes.nuscenes import NuScenes
from Generator import Generator
from NuscData import NuscData
import pickle
import os


def main():
    nusc = NuScenes(version='v1.0-mini', dataroot='./data', verbose=False)
    for i in range(len(nusc.scene)):
        nuscData: NuscData = NuscData(nusc, i)
        gen: Generator = Generator(nuscData)
        dataCluster = gen.gen_all()
        print(f'{len(dataCluster)} of data generated in scene[{i}]')
        scene_dir = os.path.join('./records/', dataCluster[0].scene['token'])
        os.makedirs(scene_dir, exist_ok=True)
        for dataset in dataCluster:
            with open(os.path.join(scene_dir, dataset.inst['token']), 'wb') as f:
                pickle.dump(dataset, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
