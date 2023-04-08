import pickle
import sys
import os
import random
from Drawer import Drawer


def main():
    if len(sys.argv) == 1:
        print(f'Usage: python3 {sys.argv[0]} <picklefile>')
        print(f'No argument given, randomly pick one from ./records')
        scenes = os.listdir('./records')
        scene = random.sample(scenes, 1)[0]
        insts = os.listdir(os.path.join('./records', scene))
        inst = random.sample(insts, 1)[0]
        record = os.path.join('./records', scene, inst)
    else:
        record = sys.argv[1]
    print(f'Loading file: {record}')
    with open(record, 'rb') as f:
        dataset = pickle.load(f)
    plt = Drawer()
    plt.plot_dataset(dataset)
    plt.plot_dataset(dataset, atk=True)


if __name__ == '__main__':
    main()
