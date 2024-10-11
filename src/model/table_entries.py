from dataclasses import dataclass, field
from src.model.entry import Entry


@dataclass
class TableEntries:
    entries: list[Entry] = field(default_factory=list)

    def add_entry(self, entry: Entry):
        self.entries.append(entry)
