from dataclasses import dataclass


@dataclass
class Config:
    api_url: str
    table_name: str
