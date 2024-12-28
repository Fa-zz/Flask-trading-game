from random import randint

class JetData:
    def __init__(self):
        self.prices = {
            "item1": randint(15000, 29999),
            "item2": randint(5000, 13999),
            "item3": randint(1000, 4999),
            "item4": randint(300, 899),
            "item5": randint(90, 249),
            "item6": randint(10, 89)
        }
    
    def get_prices(self):
        print(f"Backend prices: {self.prices}")
        return self.prices

def start_game():
    return {
        "money": 2_000, 
        "debt": 5_000, 
        "loc": 0,
        "locs": ["Badsprings", "Prim City", "Pipton", "The Wasteland", "Hooper Dam", "New Venturas"],
        "item_arr": ["Scrap metal","Scrap electronics","Bullets","Cigarettes","Stimpaks","Purified water"],
        "trench": {
            "item1": 0,
            "item2": 0,
            "item3": 0,
            "item4": 0,
            "item5": 0,
            "item6": 0
        },
        "shopping_cart": [],
        "transac_hist": {}
    }

def jet(game_state, loc):
    game_state["loc"] = loc
    jet_data = JetData()
    game_state["jet_data"] = jet_data.get_prices()
    return game_state

def buy(game_state):
    cart = game_state["shopping_cart"]
    str_buying = game_state["item_arr"][game_state["shopping_cart"][0]]
    total = game_state["jet_data"][str_buying] * cart[1] # calc total to buy. price * amount
    game_state["money"] -= total # subtract total from money
    game_state["trench"][str_buying] = cart[1] # update trench with amt bought
    game_state["shopping_cart"] = [] # clear cart
    print(f"\n{game_state}")
    return game_state