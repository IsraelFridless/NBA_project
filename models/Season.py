from dataclasses import dataclass, field


@dataclass
class Season:
    playerId: str
    playerName: str
    team: str
    position: str
    season: int
    points: int
    games: int
    turnovers: int
    assists: int
    twoPercent: float
    threePercent: float
