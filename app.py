from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import random
import game_logic

app = Flask(__name__)
# app.json.sort_keys = False
app.secret_key = 'your_secret_key'

games = {}

def get_state_and_id():
    game_id = session['game_id']
    state = games[session['game_id']]
    return state, game_id

def create_state(id):
    state = game_logic.start_game()
    state["game_id"] = id
    return state

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():
    try:
        state = games[session['game_id']]
    except KeyError:
        return redirect(url_for('index'))
    else:
        return render_template("play.html", state=state)

    # if 'game_id' not in session:
          # Redirect to home if no game is active
    #state['alert_messages'].append(f"You jet to { state['locs'][state['loc']] }")

@app.route('/api/start_game', methods=['GET'])
def start_game():
    game_id = len(games)+1
    state = create_state(game_id)
    games[game_id] = state
    session['game_id'] = game_id
    print(f"Backend Server: Game started with id: {game_id}")
    return jsonify({"status": "success", "game_id": game_id, "loc": state["loc"]}), 200

@app.route('/api/jet', methods=['POST'])
def jet():
    jet = request.get_json()
    state, game_id = get_state_and_id()
    if jet['status'] == 'success':
        #Check if the game ID exists
        if game_id not in games:
            return jsonify({'error': 'Game not found'}), 404
        # Perform jet functions and return
        state = game_logic.jet(state, jet['loc'])
        return jsonify({"status": "success", "jet_data": state["jet_data"]}), 200
    else:
        return jsonify({"status": "error", "message": "location data missing or invalid"}), 400

@app.route('/api/transaction', methods=['POST'])
def transaction():
    transac_data = request.get_json()
    state, game_id = get_state_and_id()

    if transac_data is not None:
        # Check if the game ID exists
        if game_id not in games:
            return jsonify({'error': 'Game not found'}), 404
        
        state["shopping_cart"] = transac_data
        # Error case - user cannot sell an item for more than they own
        if not(state["shopping_cart"]["buy"]) and (state["shopping_cart"]["amount"] > state["trench"][state["shopping_cart"]["item_name"]]):
            return jsonify({"status": "error", "message": "transaction data invalid or missing"}), 400
        state = game_logic.transaction(state)
        return jsonify({"status": "success", "money": state["money"], "trench": state["trench"], "item_arr": state["item_arr"], "jet_data": state["jet_data"]}), 200
    else:
        return jsonify({"status": "error", "message": "transaction data invalid or missing"}), 400

@app.route('/api/change_view', methods=['POST'])
def change_view():
    try:
        data = request.get_json()
        view = data.get('view')
        state, game_id = get_state_and_id()

        if view is not None:
            state["main_view"] = view.lower()
            return jsonify({"status": "success", "view": state["main_view"]}), 200
        else:
            return jsonify({"status": "error", "message": "Issue with view"}), 400            

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
