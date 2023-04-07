from NuscData import NuscData
from Dataset import Dataset
from Datalist import Datalist
from Data import Data
from copy import deepcopy
from quintic import quintic_polynomials_planner


class Generator:
    def __init__(self, nuscData: NuscData) -> None:
        self.nuscData = nuscData

    def gen_by_inst(self, inst: dict) -> Dataset:
        anns = self.nuscData.get_annotations(inst)

        dataset: Dataset = Dataset(self.nuscData.scene, inst)
        ego_data: Datalist = self.nuscData.get_ego_data()
        npc_data: Datalist = self.nuscData.get_npc_data(anns)

        dataset.set_ego(ego_data)
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
            dst=atk_final.transform,
            gv=dataset.npc[-1].velocity,
            ga=dataset.npc[-1].accelerate
        )

        dataset.set_atk(res)

        return dataset

    def gen_all(self) -> list:
        ret = list()
        inst_tks: set = self.nuscData.instances
        for inst_tk in inst_tks:
            inst = self.nuscData.get('instance', inst_tk)
            ret.append(self.gen_by_inst(inst))
        return ret
