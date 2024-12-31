from random import randint

class JetData:
    def __init__(self):
        self.prices = {
            "Purified water": randint(15000, 29999),
            "Stimpaks": randint(5000, 13999),
            "Cigarettes": randint(1000, 4999),
            "Bullets": randint(300, 899),
            "Scrap electronics": randint(90, 249),
            "Scrap metal": randint(10, 89)
        }
    
    def get_prices(self):
        print(f"Backend prices: {self.prices}")
        return self.prices

def start_game():
    return {
        "money": 2_000, 
        "debt": 5_000, 
        "loc": 0,
        "locs": ["Badsprings City", "Prim City", "Vault 19", "The Wasteland", "Hooper Dam", "New Venturas"],
        "item_arr": ["Scrap metal","Scrap electronics","Bullets","Cigarettes","Stimpaks","Purified water"],
        "trench": {                 # TODO: Combine trench and price dictionaries
            "Purified water": 0,
            "Stimpaks": 0,
            "Cigarettes": 0,
            "Bullets": 0,
            "Scrap electronics": 0,
            "Scrap metal": 0
        },
        "shopping_cart": {},
        "transac_hist": {},
        "alert_messages": [],
        "main_view": "marketplace"
    }

def jet(game_state, loc):
    game_state["loc"] = loc
    jet_data = JetData()
    game_state["jet_data"] = jet_data.get_prices()
    return game_state

def transaction(state):
    print(f"Transaction state: {state}")
    str_buying = state["shopping_cart"]["item_name"] # Str of bought item
    price = state["jet_data"][str_buying] # Price of bought item
    total = price * state["shopping_cart"]["amount"] # Total = price * amount

    if state["shopping_cart"]["buy"] == True:
        state["money"] -= total # Player gives up money to acquire
        state["trench"][str_buying] += state["shopping_cart"]["amount"] # Update trench with amount bought
    elif state["shopping_cart"]["buy"] == False:
        state["money"] += total # Player gives up money to part with
        state["trench"][str_buying] -= state["shopping_cart"]["amount"]
    return state