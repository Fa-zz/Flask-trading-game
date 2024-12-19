from flask import Flask, request, jsonify, session
import random
import game_logic

app = Flask(__name__)
app.json.sort_keys = False
app.secret_key = 'your_secret_key'

games = {}

def create_state(id):
    state = game_logic.start_game()
    state["game_id"] = id
    return state

@app.route('/start_game', methods=['POST'])
def start_game():
    game_id = len(games)+1
    games[game_id] = create_state(game_id)
    print(f"Game started with id: {game_id}")
    return jsonify(games[game_id])

@app.route('/jet', methods=['POST'])
def jet():
    data = request.get_json()
    game_id = data.get('game_id')
    money = data.get('money')
    debt = data.get('debt')
    loc = data.get('loc')
    print(f"/jet, {loc}, {money}, {debt}")

    # Check if the game ID exists
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    games[game_id] = game_logic.jet(games[game_id], money, debt, loc)
    return jsonify(games[game_id])

"""
@app.route('/take_turn', methods=['POST'])
def take_turn():
    data = request.get_json()
    game_id = data['game_id']
    move = data['move']

    # Check if game exists
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404

    game = games[game_id]
    game['state'] = f'Player made move: {move}'
    return jsonify(game)

@app.route('/game_state/<int:game_id>', methods=['GET'])
def game_state(game_id):
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    return jsonify(games[game_id])

"""
if __name__ == '__main__':
    app.run(debug=True)
