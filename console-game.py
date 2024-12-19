from random import randint, seed
import requests
transac_history = []
game_id = -1

def format_print_prices(prices):
    for name, price in prices.items():
        print(f"{name}: ${price}")
        # print(f"{name}:".ljust(15) + f"${price}".ljust(10))

def format_num(num):
    return f"{num:,d}"

def play_game(playing, game_data):
    first_turn = True

    while playing:
        # Jet occurs
        r = requests.post("http://127.0.0.1:5000/jet", json=game_data)
        game_data = r.json()

        jet_data = game_data["jet_data"]
        print(f"\nYou are in {game_data["loc"]}. You have ${game_data["money"]} on hand.\n")
        prices = format_print_prices(jet_data)

        input()


playing = input("Welcome to Dope Wars. Yes Y to Play.")
if playing == 'Y' or playing == 'y':
    r = requests.post("http://127.0.0.1:5000/start_game", data={})
    # TODO: Gracefully exit if request doesn't work
    game_data = r.json()
    print(game_data)
    # game_id = game_data[game_id]
    play_game(True, game_data)