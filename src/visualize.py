import pickle
import sys
from Drawer import Drawer


def main():
    if len(sys.argv) == 1:
        print(f'Usage: python3 {sys.argv[0]} <piklefile>')
        exit(1)
    print(f'Loading file: {sys.argv[1]}')
    with open(sys.argv[1], 'rb') as f:
        dataset = pickle.load(f)
    plt = Drawer()
    plt.plot_dataset(dataset)
    plt.plot_dataset(dataset, atk=True)


if __name__ == '__main__':
    main()
