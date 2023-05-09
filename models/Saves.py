from pydantic import BaseModel, Field


class Saves(BaseModel):
    fail_count: int = Field(alias="failCount")
    success_count: int = Field(alias="successCount")
    is_stabilized: bool = Field(alias="isStabilized")
