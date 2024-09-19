from dataclasses import dataclass, field


@dataclass
class Season:
    player_id: str
    player_name: str
    team: str
    position: str
    season: int
    points: int
    games: int
    turnovers: int
    assists: int
    two_percent: float
    three_percent: float
