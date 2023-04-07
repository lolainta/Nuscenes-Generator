from nuscenes.nuscenes import NuScenes
from copy import deepcopy
from quintic import quintic_polynomials_planner
from Drawer import Drawer
from Data import Data
from Datalist import Datalist
from Dataset import Dataset
from NuscData import NuscData


def main():
    nusc = NuScenes(version='v1.0-mini', dataroot='./data', verbose=False)
    gen: NuscData = NuscData(nusc, 5)
    inst_tks: set = gen.instances

    for inst_tk in inst_tks:
        inst = nusc.get('instance', inst_tk)
        anns = gen.get_annotations(inst)

        ego_data: Datalist = gen.get_ego_data()
        npc_data: Datalist = gen.get_npc_data(anns)

        dataset: Dataset = Dataset(ego_data)
        dataset.set_npc(npc_data)

        # plt = Drawer()
        # plt.plot_dataset(dataset)
        ego_final: Data = dataset.ego[-1]
        atk_final: Data = deepcopy(ego_final)
        atk_final.flip()
        atk_final.forward(2)
        atk_final.rotate(20, org=ego_final.bound[0])
        # plt.show()
        res = quintic_polynomials_planner(
            src=dataset.npc,
            dst=atk_final.transform, gv=dataset.npc[-1].velocity, ga=dataset.npc[-1].accelerate)

        dataset.set_atk(res)
        # plt.plot_dataset(dataset, atk=True)
        # plt.show()


if __name__ == '__main__':
    main()
