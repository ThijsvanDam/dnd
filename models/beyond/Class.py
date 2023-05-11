from pydantic import BaseModel

class ClassDefinition(BaseModel):
    name: str

class Class(BaseModel):
    level: int
    definition: ClassDefinition

    @property
    def name(self):
        return self.definition.name
