from dataclasses import dataclass
from typing import List

from models.Player import Player


@dataclass
class FantasyTeam:
    team_name: str
    player_ids: List[str]
    id: int = None