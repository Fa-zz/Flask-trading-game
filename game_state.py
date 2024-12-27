class GameState:
    def __init__(self):
        self.state = {}

    def get_state(self):
        return self.state
    def over_write(self, state):
        self.state = state

    def get_game_id(self):
        return self.state["game_id"]
    
    def get_money(self):
        return self.state["money"]
    def set_money(self, new_money):
        self.state["money"] = new_money

    def get_debt(self):
        return self.state["debt"]
    def set_debt(self, new_debt):
        self.state["debt"] = new_debt

    def get_loc(self):
        return self.state["loc"]
    def set_loc(self, new_loc):
        self.state["loc"] = new_loc

    def get_loc_s(self):
        return self.state["locs"][self.state["loc"]]

    def get_locs(self):
        return self.state["locs"]
    def set_locs(self, new_locs):
        self.state["locs"] = new_locs

    def get_item_arr(self):
        return self.state["item_arr"]
    def set_candy_arr(self, new_item_arr):
        self.state["item_arr"] = new_item_arr

    def get_jet_data(self):
        return self.state["jet_data"]
    def set_jet_data(self, new_jet_data):
        self.state["jet_data"] = new_jet_data

    def get_trench(self):
        return self.state["trench"]
    def set_trench(self, new_trench):
        self.state["trench"] = new_trench

    def get_shopping_cart(self):
        return self.state["shopping_cart"]
    def set_shopping_cart(self, new_shopping_cart):
        self.state["shopping_cart"] = new_shopping_cart

    def get_transac_hist(self):
        return self.state["transac_hist"]
    def set_transac_hist(self, new_transac_hist):
        self.state["transac_hist"] = new_transac_hist