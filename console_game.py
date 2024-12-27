# from random import randint, seed
import requests
from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command
from game_state import GameState

def make_request(endpoint, data):
    if endpoint == "start_game":
        r = requests.get("http://127.0.0.1:5000/start_game", json=data)
    elif endpoint == "jet":
        r = requests.post("http://127.0.0.1:5000/jet", json=data)
    elif endpoint == "buy":
        r = requests.post("http://127.0.0.1:5000/buy", json=data)
    return r.json()

def clear_screen():
    """
    Clears the terminal screen.
    """
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    # Action
    system_call([command])

def format_num(num):
    return f"{num:,d}"

def format_print_trench(trench):
    i = 1
    total_amt = 100
    for name, amt in trench.items():
        print(f"{i}.".ljust(3) + f"{name}:".ljust(15) + f"{amt}".ljust(10))
        i += 1
        total_amt -= amt
    print(f"You have {total_amt} spaces left in your trench.")

def format_print_prices(prices):
    i = 1
    emoji=""
    for name, price in prices.items():
        print(f"{i}.".ljust(3) + f"{name}:".ljust(15) + f"{emoji}${format_num(price)}".ljust(10))
        i += 1

def print_jet_info():
    print(f"\nYou are in {state.get_loc_s()}. You have ${format_num(state.get_money())} on hand.")
    format_print_trench(state.get_trench())
    print('\n"Hey dude, here\'s the prices"')
    format_print_prices(state.get_jet_data())
    print('\nEnter "?" to see a list of commands.\n')

def handle_jet():
    print(f"Jetting to {state.get_loc_s()}...")
    state.over_write(make_request("jet", state.get_state()))
    accepting_deal_commands = True
    print_jet_info()

    while (accepting_deal_commands):
        command = input(">>")
        if (command.isspace()):
            continue
        command = command.split()

        # Help
        if (command[0] == "?"):
            print(f'To buy, enter "b n" where n is the number you want to buy.\nTo sell, enter "s n" where n is the number you want to sell.\nEnter "j 1" to jet to {state.get_locs()[0]}, "j 2" to jet to {state.get_locs()[1]}, "j 3" to jet to {state.get_locs()[2]}, "j 4" to jet to {state.get_locs()[3]}, "j 5" to jet to {state.get_locs()[4]}, "j 6" to jet to {state.get_locs()[5]}.')

        # # Buy commands
        if (command[0] == 'b' and (not(command[1].isspace()) and command[1].isnumeric())):
            int_buying_i = int(command[1])-1
            str_buying = state.get_item_arr()[int_buying_i]
            if len(command) == 2:
                print(f'Buy {str_buying} at ${state.get_jet_data()[str_buying]} apiece?')
                print(f'Enter b {command[1]} x, where x is the amount you want to cop.')
            if len(command) == 3 and (not(command[2].isspace()) and command[2].isnumeric()): # If valid buy command
                # append to cart the drug to buy and amount, then make post request
                state.set_shopping_cart([int_buying_i, int(command[2])])
                state.over_write(make_request("buy", state.get_state()))
                print('"Pleasure doing business!"')
                print_jet_info()

        # # Jet commands
        if (command[0] == 'j' and (not(command[1].isspace()) and command[1].isnumeric())):
            int_dest = int(command[1])-1
            if int_dest >= 0 and int_dest <= 6:
                if state.get_loc_s()[int_dest] == state.get_loc_s():
                    print(f'You\'re already in {state.get_loc_s()}!')
                else:
                    state.set_loc(int_dest)
                    accepting_deal_commands = False
                    break
    return 0

def play_game(playing):
    while playing:
        clear_screen()
        # Jet occurs
        handle_jet()

if __name__ == "__main__": 
    # playing = input("Welcome to Dope Wars. Yes Y to Play.")
    # if playing == 'Y' or playing == 'y':

    state = GameState()
    state.over_write(make_request("start_game", {}))
    play_game(True)