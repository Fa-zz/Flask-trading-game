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
        "drugs_arr": ["cocaine","heroin","acid","shrooms","adderall","weed"],
        "trench": {
            "cocaine": 0,
            "heroin": 0,
            "acid": 0,
            "shrooms": 0,
            "adderall": 0,
            "weed": 0
        },
        "shopping_cart": []
    }

def jet(game_state, money, debt, loc):
    jet_data = JetData()
    game_state["debt"] = debt
    game_state["loc"] = loc
    game_state["money"] = money
    game_state["jet_data"] = jet_data.get_prices()
    return game_state

def buy(game_state):
    cart = game_state["shopping_cart"]
    str_buying = game_state["drugs_arr"][game_state["shopping_cart"][0]]
    total = game_state["jet_data"][str_buying] * cart[1] # calc total to buy. price * amount
    game_state["money"] -= total # subtract total from money
    game_state["trench"][str_buying] = cart[1] # update trench with amt bought
    game_state["shopping_cart"] = [] # clear cart
    return game_state