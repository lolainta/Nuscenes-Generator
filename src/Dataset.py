from Transform import Transform


class Data():
    def __init__(self, ts, ego: Transform, npc: Transform) -> None:
        self.timestamp = ts
        self.ego: Transform = ego
        self.npc: Transform = npc

    def set_atk(self, atk: Transform) -> None:
        self.atk = atk


class Dataset():
    def __init__(self) -> None:
        self.dataset = list()

    def __getitem__(self, key: int) -> Data:
        return self.dataset[key]

    def __len__(self):
        return len(self.dataset)

    def append(self, d: Data):
        self.dataset.append(d)

    def set_atk(self, ds) -> None:
        assert len(self) == len(ds), f'{len(self)=} not equal {len(ds)=}'
        for org, new in zip(self, ds):
            org.atk = new.atk
