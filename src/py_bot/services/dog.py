from typing import Optional

import requests


class DogService:
    def get_random_dog(self) -> Optional[str]:
        content = requests.get("https://random.dog/woof.json")
        if content.status_code == 200:
            return content.json()["url"]
        return None
