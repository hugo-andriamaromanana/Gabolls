from dataclasses import dataclass


@dataclass(slots=True)
class Seed:
    source: int
    counter: int

    def next(self) -> int:
        new = self.source + self.counter
        self.counter += 1
        return new

    @property
    def as_dict(self) -> dict[str, int]:
        return {"source": self.source, "counter": self.counter}
