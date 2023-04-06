
from Data import Data
from Datalist import Datalist
from collections import defaultdict


class Dataset():
    def __init__(self, ego: Datalist) -> None:
        self.ego: Datalist = ego
        self.npc: Datalist = list()
        self.atk: Datalist = list()

    def set_npc(self, npc: Datalist) -> None:
        self.npc = npc
        self.compile()

    def set_atk(self, atk: Datalist) -> None:
        self.atk = atk
        self.compile()

    def compile(self) -> None:
        self.get_timelist()
        self.gen_time2data()

    def gen_time2data(self) -> None:
        ret = defaultdict(dict)
        for d in self.ego:
            ret[d.timestamp]['ego'] = d
        for d in self.npc:
            ret[d.timestamp]['npc'] = d
        for d in self.atk:
            ret[d.timestamp]['atk'] = d
        self.time2data: dict[int, dict[str, Data]] = ret

    def get_timelist(self) -> None:
        ret = set()
        for d in self.ego:
            ret.add(d.timestamp)
        for d in self.npc:
            ret.add(d.timestamp)
        ret = list(ret)
        ret = sorted(ret)
        self.timelist = ret
