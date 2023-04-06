from Transform import Transform


class Data():
    def __init__(self, ts, ego, atk) -> None:
        self.timestamp = ts
        self.ego: Transform = ego
        self.atk: Transform = atk


class Dataset():
    def __init__(self) -> None:
        self.dataset = list()

    def __getitem__(self, key: int) -> Data:
        return self.dataset[key]

    def __len__(self):
        return len(self.dataset)

    def append(self, d: Data):
        self.dataset.append(d)
