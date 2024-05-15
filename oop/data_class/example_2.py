# attribute default value
from dataclasses import dataclass

@dataclass
class Country:
    name = "Indonesia"
    seasons = ["Rainy", "Dry"]
    number_of_populations = 275.5

    def info(self) -> str:
        return f"{self.name} | {len(self.seasons)} seasons | {self.number_of_populations} million populations"
    
c = Country()
print(c.info())