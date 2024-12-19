from random import randint

trench = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

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
    return {"money": 2_000, "debt": 5_000, "loc": "the Bronx"}

def jet(game_state, money, debt, loc):
    jet_data = JetData()
    game_state["deb"] = debt
    game_state["loc"] = loc
    game_state["money"] = money
    game_state["jet_data"] = jet_data.get_prices()
    return game_state