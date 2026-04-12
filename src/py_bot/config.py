import os
from dataclasses import dataclass


@dataclass
class Config:
    token: str

    def get_token(self) -> str:
        return self.token


def load_config() -> Config:
    return Config(
        token=os.getenv("TOKEN", ""),
    )
