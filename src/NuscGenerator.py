from nuscenes.nuscenes import NuScenes
from Dataset import Data, Dataset
from Transform import Transform


class NuscGenerator():
    def __init__(self, nusc: NuScenes, scene: int) -> None:
        self.nusc = nusc
        self.scene = self.nusc.scene[scene]
        self.samples = self.get_samples(self.scene)

    def get_samples(self, scene: dict):
        samples = [self.nusc.get('sample', scene['first_sample_token'])]
        while samples[-1]['next']:
            nxt = self.nusc.get('sample', samples[-1]['next'])
            samples.append(nxt)
        # print(samples[0])
        # print(samples[-1])
        return samples

    def get_annotations(self, inst: dict) -> list:
        fst_tk = inst['first_annotation_token']
        lst_tk = inst['last_annotation_token']

        cur_tk = fst_tk
        ann_tks = [cur_tk]
        while cur_tk != lst_tk:
            cur = self.nusc.get('sample_annotation', cur_tk)
            cur_tk = cur['next']
            # print(cur)
            ann_tks.append(cur_tk)
            # break

        anns = [self.nusc.get('sample_annotation', ann_tk)
                for ann_tk in ann_tks]
        return anns

    def compile_data(self, anns: list):

        ret: Dataset = Dataset()

        for ann in anns:
            sample_tk = ann['sample_token']
            sample = self.nusc.get('sample', sample_tk)
            data_tk = sample['data']['RADAR_FRONT']
            data = self.nusc.get('sample_data', data_tk)
            ego_pos_tk = data['ego_pose_token']
            ego_pos = self.nusc.get('ego_pose', ego_pos_tk)

            ret.append(
                Data(ego_pos['timestamp'],
                     Transform(ego_pos['translation'],
                               ego_pos['rotation']),
                     Transform(ann['translation'],
                               ann['rotation'])
                     )
            )

        return ret[20:]
