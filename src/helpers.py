from typing import Dict, Optional, List

import requests

from src.models import Container


def http_get_containers(url: str, key: str, agent: str = "kapellmeister-agent") -> Optional[List[Container]]:
    headers: Dict = {"Authorization": f"Token {key}", "User-Agent": agent, "Accept-Encoding": "gzip"}

    try:
        with requests.get(url, headers=headers, timeout=30) as r:
            if r.ok:
                return [Container.parse_obj(c) for c in r.json()]

    except requests.RequestException as err:
        print(err)
