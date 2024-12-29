// Function for formatting money
function formatMoney(amount) {
    return "$" + Number(amount).toLocaleString('en-US', {
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    });
}

// Function to make the GET request to /api/start_game
async function fetchStartGame() {
    const response = await fetch('/api/start_game');
    if (!response.ok) {
        throw new Error('Failed to start the game');
    }
    return await response.json(); // Returns the JSON response
}

// Function to make the POST request to /api/jet
async function sendJetRequest(data) {
    const response = await fetch('/api/jet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    if (!response.ok) {
        throw new Error('Failed to send POST request to /api/jet');
    }
    return await response.json(); // Returns the JSON response
}

// Function to handle the play button click event
async function handlePlayButtonClick() {
    try {
        // 1. Fetch the game start data (GET request)
        const startGameData = await fetchStartGame();
        console.log('Game started:', startGameData);

        // 2. Send the data to /api/jet (POST request)
        const jetResponse = await sendJetRequest(startGameData);
        console.log('POST request to /api/jet completed:', jetResponse);

        // 3. After both requests are successful, redirect to /play
        window.location.href = '/play';
    } catch (error) {
        console.error('Error during game setup:', error);
    }
}

// Function to handle the play button click event
async function handleBuyButtonClick(event) {
    // Get the clicked button and its parent form
    const buttonElement = event.target;
    const form = buttonElement.closest('.buy-form');

    // Extract the item ID and buy amount from the form
    const itemId = form.querySelector('input[name="item-id"]').value;
    const buyAmount = form.querySelector('input[name="buy-amt"]').value;

    // Validate the input
    if (buyAmount <= 0) {
        alert('Please enter a valid amount to buy.');
        return;
    }

    // Construct the POST request payload
    const payload = {
        item_id: itemId,
        buy_amount: parseInt(buyAmount, 10),
    };

    try {
        // Send data to /api/buy (POST request)
        const response = await fetch('/api/buy', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log(result)
        document.getElementById("user-money").innerHTML = "You have " + formatMoney(result.money) + " on hand.";
        alert(`You bought ${payload.buy_amount} ${payload.item_id}`);
    } catch (error) {
        console.error('Error during the buy operation:', error);
        alert('Failed to buy item. Please try again.');
    }
}

// Event listener for the play button
const playButton = document.getElementById('play-button');
if (playButton) {
    playButton.addEventListener('click', handlePlayButtonClick);
}

// Event listener for each buy button
const buyButtons = document.querySelectorAll('.buy-button');
if (buyButtons) {
    buyButtons.forEach(button => {
        button.addEventListener('click', handleBuyButtonClick);
    });
}