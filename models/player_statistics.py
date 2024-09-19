from dataclasses import dataclass

@dataclass
class PlayerStatistics:
    player_id: str
    ATR: float
    PPGRatio: float