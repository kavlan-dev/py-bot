import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    token: str
    proxy_host: Optional[str]

    def get_token(self) -> str:
        return self.token

    def get_proxy_url(self) -> Optional[str]:
        if self.proxy_host != "":
            return f"socks5://{self.proxy_host}"


def load_config() -> Config:
    return Config(token=os.getenv("TOKEN", ""), proxy_host=os.getenv("PROXY_HOST"))
