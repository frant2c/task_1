import re
from dataclasses import dataclass


@dataclass
class Entry:
    websites: str
    popularity: int
    frontend: str
    backend: str
    database: str
    other: str

    @staticmethod
    def parse_popularity(popularity_str: str) -> int:
        """
        Parses string value to integer.
        Cuts non digit characters.
        :param popularity_str: popularity example 516,000,000 (Total, not unique)[13]
        :return: parsed popularity value as integer
        """
        cleaned_str = re.sub(r"[,.]", "", popularity_str)
        return int(re.match(r"^\d+", cleaned_str).group(0))

    @staticmethod
    def from_table_row(row):
        return Entry(
            websites=row[0],
            popularity=Entry.parse_popularity(row[1]),
            frontend=row[2],
            backend=row[3],
            database=row[4],
            other=row[5]
        )
