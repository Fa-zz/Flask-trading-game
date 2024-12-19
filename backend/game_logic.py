from random import randint


class JetData:
    def __init__(self):
        self.prices = {
            "cocaine": randint(15000, 29999), # cocaine
            "heroin": randint(5000, 13999), # heroin
            "acid": randint(1000, 4999), # acid
            "shrooms": randint(300, 899), # shrooms
            "adderall": randint(90, 249), # adderall
            "weed": randint(10, 89) # weed
        }
    
    def get_prices(self):
        print(f"Backend prices: {self.prices}")
        return self.prices

def start_game():
    return {
        "money": 2_000, 
        "debt": 5_000, 
        "loc": 0,
        "locs": ["the Bronx", "Queens", "Central Park", "Manhattan", "Coney Island", "Brooklyn"],
        "trench": {
            "cocaine": 0,
            "heroin": 0,
            "acid": 0,
            "shrooms": 0,
            "adderall": 0,
            "weed": 0
        }
    }

def jet(game_state, money, debt, loc):
    jet_data = JetData()
    game_state["deb"] = debt
    game_state["loc"] = loc
    game_state["money"] = money
    game_state["jet_data"] = jet_data.get_prices()
    return game_state