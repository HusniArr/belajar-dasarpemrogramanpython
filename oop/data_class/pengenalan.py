from dataclasses import dataclass

@dataclass
class Planet:
    name: str
    diameter: float
    natural_sattelites: list[str]

planets = [
    Planet("Mercury", 4879, []),
    Planet("Venus", 12104, []),
    Planet("Earth", 12742, ["Moon"]),
]

for p in planets:
    print(f"{p.name} | {p.diameter} km | {len(p.natural_sattelites)} moons")
