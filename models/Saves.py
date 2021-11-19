from dataclasses import dataclass

@dataclass
class Saves:
    failCount: int
    successCount: int
    isStabilized: bool