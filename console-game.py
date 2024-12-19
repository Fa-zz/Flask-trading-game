from random import randint, seed
import requests
from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command

def clear_screen():
    """
    Clears the terminal screen.
    """
    
    # Clear screen command as function of OS
    command = 'cls' if system_name().lower().startswith('win') else 'clear'

    # Action
    system_call([command])

transac_history = []
game_id = -1

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

def jet_commands(game_data):
    accepting_deal_commands = True
    jet_data = game_data["jet_data"]
    trench = game_data["trench"]
    curr_loc = game_data['locs'][game_data['loc']]
    print(f"\nYou are in {curr_loc}. You have ${format_num(game_data['money'])} on hand.")
    format_print_trench(trench)
    print('\n"Hey dude, here\'s the prices"')
    format_print_prices(jet_data)

    while (accepting_deal_commands):
        print('\nEnter "?" to see a list of commands.\n')
        command = input(">>")
        if (command.isspace()):
            continue
        command = command.split()

        # Help
        if (command == "?"):
            print(f'To buy, enter "b n" where n is the number you want to buy.\nTo sell, enter "s n" where n is the number you want to sell.\nEnter "j 1" to jet to {game_data["locs"][0]}, "j 2" to jet to {game_data["locs"][1]}, "j 3" to jet to {game_data["locs"][2]}, "j 4" to jet to {game_data["locs"][3]}, "j 5" to jet to {game_data["locs"][4]}, "j 6" to jet to {game_data["locs"][5]}.')
        # Jet commands
        if (command[0] == 'j' and (command[1] != '' and command[1] != ' ' and command[1].isnumeric())):
            int_dest = int(command[1])-1
            print(f"Int_dest:{int_dest}")
            if int_dest >= 0 and int_dest <= 6:
                if int_dest == game_data['loc']:
                    print(f'You\'re already in {curr_loc}!')
                else:
                    game_data['loc'] = int_dest
                    accepting_deal_commands = False
    return

def play_game(playing, game_data):
    first_turn = True

    while playing:
        clear_screen()
        # Jet occurs
        print(f"Jetting to {game_data['locs'][game_data['loc']]}...")
        r = requests.post("http://127.0.0.1:5000/jet", json=game_data)
        game_data = r.json()

        jet_commands(game_data)


# playing = input("Welcome to Dope Wars. Yes Y to Play.")
# if playing == 'Y' or playing == 'y':
r = requests.post("http://127.0.0.1:5000/start_game", data={})
# TODO: Gracefully exit if request doesn't work
game_data = r.json()
print(game_data)
# game_id = game_data[game_id]
play_game(True, game_data)