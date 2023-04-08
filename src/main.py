from nuscenes.nuscenes import NuScenes
from Generator import Generator
from NuscData import NuscData
import pickle
import os
import argparse
from tqdm import trange, tqdm


def run(args):
    nusc = NuScenes(version=args.dataset,
                    dataroot='./data',
                    verbose=args.verbose)
    cnt = 0
    print = tqdm.write
    print("Generating data...")
    for i in trange(len(nusc.scene)):
        nuscData: NuscData = NuscData(nusc, i)
        gen: Generator = Generator(nuscData)
        dataCluster = gen.gen_all()
        sz = len(dataCluster)
        cnt += sz
        if args.verbose:
            print(f'{sz} data generated in scene[{i}]')
        if sz == 0:
            if args.verbose:
                print(f"No data generated for scene[{i}], skip")
            continue
        if args.record:
            scene_dir = os.path.join(
                args.record_path, dataCluster[0].scene['token'])
            os.makedirs(scene_dir, exist_ok=True)
            for dataset in dataCluster:
                with open(os.path.join(scene_dir, f'{dataset.inst["token"]}.pickle'), 'wb') as f:
                    pickle.dump(dataset, f, protocol=pickle.HIGHEST_PROTOCOL)
    print('======')
    print(f'{cnt} data generated from {len(nusc.scene)} scenes')


def main():
    parser = argparse.ArgumentParser(
        prog='python3 src/main.py',
        description='Generate data from given nuscene dataset and collision type'
    )
    parser.add_argument('-d', '--dataset',
                        choices=['v1.0-mini', 'v1.0-trainval'],
                        default='v1.0-mini',
                        help='Nuscene dataset version')
    parser.add_argument('--record',
                        action='store_true',
                        help='Whether to record to record path or not)')
    parser.add_argument('--record-path',
                        default='./records',
                        help='The path to store the generated data (create if not exists)'
                        )
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Show log'
                        )
    args = parser.parse_args()
    run(args)


if __name__ == '__main__':
    main()
