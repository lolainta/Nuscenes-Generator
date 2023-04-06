from nuscenes.nuscenes import NuScenes
from copy import deepcopy
from quintic import quintic_polynomials_planner
from Drawer import Drawer
from Dataset import Dataset
from NuscGenerator import NuscGenerator


def main():

    nusc = NuScenes(version='v1.0-mini', dataroot='./data', verbose=True)

    gen = NuscGenerator(nusc, 5)

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
    # print(inst)

    anns = gen.get_annotations(inst)
    dataset: Dataset = gen.compile_data(anns)

    # print([d['time'] for d in data])
    elapse_time = (dataset[-1].timestamp-dataset[0].timestamp)/1000000
    print(f'{elapse_time=}s')
    print('Data compiled successfully.')

    print('Drawing data')
    plt = Drawer()
    # plt.plot_data(dataset)
    print('Data drawn')

    ego = dataset[-1].ego
    atk = deepcopy(ego)
    atk.flip()
    atk.forward(2)
    atk.rotate(20, org=ego.bound[0])
    plt.plot_car(atk)

    res = quintic_polynomials_planner(
        src=dataset[0].npc, sv=5, sa=0.1,
        dst=atk, gv=10, ga=-1,
        frame=len(dataset), dt=0.5)
    # print(res)
    dataset.set_atk(res)
    plt.plot_data(dataset, atk=True)

    plt.show()


if __name__ == '__main__':
    main()
