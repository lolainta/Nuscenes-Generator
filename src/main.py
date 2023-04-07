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
    scene = nusc.scene[5]
    samples = gen.get_samples(scene)
    # nusc.render_scene(scene['token'])

    ann_tk = samples[30]['anns'][7]
    ann = nusc.get('sample_annotation', ann_tk)
    print(f'{ann_tk=}')
    # nusc.render_annotation(ann_tk)
    # inst_tk = 69385845cb9747b7afe095177cc405b5
    inst_tk = ann['instance_token']
    print(f'{inst_tk=}')
    inst = nusc.get('instance', inst_tk)
    print(inst)
    cat = nusc.get('category', inst['category_token'])
    print(cat)
    anns = gen.get_annotations(inst)
    ego_data: Datalist = gen.get_ego_data()
    npc_data: Datalist = gen.get_npc_data(anns)

    dataset: Dataset = Dataset(ego_data)
    dataset.set_npc(npc_data)

    plt = Drawer()
    print('Drawing data')
    plt.plot_dataset(dataset)
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
    plt.plot_dataset(dataset, atk=True)
    plt.show()


if __name__ == '__main__':
    main()
