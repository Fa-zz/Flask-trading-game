from flask import Flask, request, jsonify, render_template, redirect, url_for, session
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

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():
    if 'game_id' not in session:
        return redirect(url_for('index'))  # Redirect to home if no game is active
    state = games[session['game_id']]
    state['alert_messages'].append(f"You jet to { state['locs'][state['loc']] }")
    return render_template("play.html", state=state)

@app.route('/api/start_game', methods=['GET'])
def start_game():
    game_id = len(games)+1
    games[game_id] = create_state(game_id)
    session['game_id'] = game_id
    print(f"Game started with id: {game_id}")
    return jsonify(games[game_id])

@app.route('/api/jet', methods=['POST'])
def jet():
    data = request.get_json()
    game_id = data['game_id']
    loc = data['loc']

    #Check if the game ID exists
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    games[game_id] = game_logic.jet(games[game_id], loc)
    return jsonify(games[game_id])

@app.route('/api/buy', methods=['POST'])
def buy():
    game_data = request.get_json()
    print(game_data)

    # Check if the game ID exists
    if game_data['game_id'] not in games:
        return jsonify({'error': 'Game not found'}), 404

    games[game_data['game_id']] = game_logic.buy(game_data)
    return jsonify(game_data)
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
