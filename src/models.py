from typing import List, Optional, Dict

from pydantic import BaseModel


class ContainerParameters(BaseModel):
    name: str
    image: str
    environment: List[str] = []


class Container(BaseModel):
    auth: str
    slug: str
    digest: str
    parameters: ContainerParameters
