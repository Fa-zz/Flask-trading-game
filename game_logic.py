from random import randint

ITEMS = ["Scrap metals","Scrap electronics","Vodka","Gasoline","Stimpaks","Purified water"]

class JetData:
    def __init__(self):
        self.prices = {
            item: [randint(15000, 29999)] if item == ITEMS[5] 
            else [randint(5000, 13999)] if item == ITEMS[4] 
            else [randint(1000, 4999)] if item == ITEMS[3] 
            else [randint(300, 899)] if item == ITEMS[2] 
            else [randint(90, 249)] if item == ITEMS[1] 
            else [randint(10, 89)] 
            for item in ITEMS
        }

    def get_data(self):
        print(f"Backend prices: {self.prices}")
        return self.prices
    
    # Helper function
    def find_greatest_quotient_within_limit(self, dividend, divisor, upper_bound):
        if divisor <= 0:
            raise ValueError("The divisor must be greater than zero.")
        if upper_bound <= 0:
            raise ValueError("The upper_bound must be greater than zero.")
        while True:
            quotient = dividend // divisor
            if quotient <= upper_bound:
                return quotient
            divisor += 1

    def set_max_buy_vals(self, item_name, user_money, trench_space):
        if len(self.prices[f'{item_name}']) == 1:
            self.prices[f"{item_name}"].append(self.find_greatest_quotient_within_limit(user_money, self.prices[item_name][0], trench_space))
        else:
            self.prices[f"{item_name}"][1] = self.find_greatest_quotient_within_limit(user_money, self.prices[item_name][0], trench_space)
    
def start_game():
    inv = {
        "money": 2_000, 
        "debt": 5_000, 
        "loc": 0,
        "locs": ["Badsprings City", "Prim City", "Vault 19", "The Wasteland", "Hooper Dam", "New Venturas"],
        "item_arr": ITEMS,
        "trench": {item: 0 for item in ITEMS},
        "shopping_cart": {},
        "transac_hist": {},
        "alert_messages": [],
        "main_view": "marketplace"
    }
    inv["trench"]["space"] = 100
    return inv

def jet(game_state, loc):
    game_state["loc"] = loc
    jet_data = JetData()
    for item_name in game_state["item_arr"]:
        jet_data.set_max_buy_vals(item_name, game_state["money"], game_state["trench"]["space"])
    game_state["jet_data"] = jet_data.get_data()
    game_state["jet_data_obj"] = jet_data
    print(f"Backend jet data: {game_state['jet_data']}")
    return game_state

def transaction(state):
    print(f"Transaction state: {state}")
    str_buying = state["shopping_cart"]["item_name"] # Str of bought item
    price = state["jet_data"][str_buying][0] # Price of bought item
    total = price * state["shopping_cart"]["amount"] # Total = price * amount

    # If buying commodity
    if state["shopping_cart"]["buy"] == True:
        state["money"] -= total # Player gives up money to acquire commodity
        state["trench"][str_buying] += state["shopping_cart"]["amount"] # Update trench with amount bought
        state["trench"]["space"] -= state["trench"][str_buying] # Update trench space with amount bought
    
    # If selling commodity
    elif state["shopping_cart"]["buy"] == False:
        state["money"] += total # Player gives up money to part with commodity
        state["trench"][str_buying] -= state["shopping_cart"]["amount"]
        state["trench"]["space"] += state["trench"][str_buying] # Update trench space with amount sold

    # Update max buy vals
    for item_name in state["item_arr"]:
        state["jet_data_obj"].set_max_buy_vals(item_name, state["money"], state["trench"]["space"])
    state["jet_data"] = state["jet_data_obj"].get_data()

    return state