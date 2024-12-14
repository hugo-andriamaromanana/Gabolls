from dataclasses import dataclass


@dataclass
class Seed:
    source: int
    counter: int

    def next(self) -> int:
        new = self.source + self.counter
        self.counter += 1
        return new
