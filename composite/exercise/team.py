from typing import List
from .entity import Entity

class Team(Entity):

    def __init__(self) -> None:
        self.entities : List[Entity] = []

    def add(self, entity: Entity):
        self.entities.append(entity)

    def deploy(self):
        for entity in self.entities:
            entity.deploy()

            