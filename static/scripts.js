// Function for formatting money
function formatMoney(amount) {
    return Number(amount).toLocaleString('en-US', {
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

// Function to handle click event on buying or selling buttons
async function handleTransactionButtonClick(event) {
    // Get the clicked button and its parent form
    const buttonElement = event.target;
    const buttonText = event.target.textContent.trim();
    const form = buttonElement.closest('.buy-form');

    // Extract the item ID, amount, and max buy val from the form
    const itemName = form.querySelector('input[name="item-name"]').value;
    const amount = parseInt(form.querySelector('input[name="amt"]').value, 10);
    const maxVal = parseInt(form.querySelector('input[name="max-buy"]').value, 10);
    
    // Validate the input
    if (amount <= 0 || (buttonText == "Buy" && amount > maxVal)) {
        alert('Enter a valid amount for the transaction.');
        return;
    }

    // Construct the POST request payload
    let payload = NaN;
    let operation = NaN;
    if (buttonText == "Buy") {
        payload = {
            item_name: itemName,
            amount: parseInt(amount, 10),
            buy: true
        };
        operation = "bought";
    } else if (buttonText == "Sell") {
        payload = {
            item_name: itemName,
            amount: parseInt(amount, 10),
            buy: false
        };
        operation = "sold";
    }
    console.log("Transaction payload: " + payload.item_name + " " + payload.amount + " " + payload.buy);
    try {
        // Send data to /api/transaction (POST request)
        const response = await fetch('/api/transaction', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        // Get result
        const result = await response.json();
        console.log(result)
        // Update owned values
        const ownedAmounts = document.querySelectorAll('.owned-amt');
        ownedAmounts.forEach((span) => {
            const form = span.closest('.item-row').querySelector('input[name="item-name"]');
            const itemName = form.value;
            span.textContent = result.trench[itemName] || 0;
        });
        // Update max vals
        const maxVals = document.querySelectorAll('.max-val');
        maxVals.forEach((span) => {
            const form = span.closest('.item-row').querySelector('input[name="item-name"]');
            const itemName = form.value;
            span.textContent = result.jet_data[itemName][1] || 0;
        })
        // Update user trench space
        document.getElementById("trench-space").innerHTML = result.trench.space
        // Update user money
        document.getElementById("user-money").innerHTML = formatMoney(result.money);
        form.reset();
        alert(`You ` + operation + ` ${payload.amount} ${payload.item_name}`);
    } catch (error) {
        console.error('Error during the buy operation:', error);
        alert('Failed to buy item. Please try again.');
        form.reset();
    }
}

// Function to handle the changing the view
async function handleViewButtonClick(event) {
    const buttonText = event.target.textContent.trim();

    try {
        // Send an asynchronous POST request to /api/change_view
        const response = await fetch('/api/change_view', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                view: buttonText
            })
        });

        // Check if the request was successful
        if (response.ok) {
            const data = await response.json();
            console.log('View changed successfully:', data);
            location.reload();
        } else {
            console.error('Error changing view:', response.statusText);
        }
    } catch (error) {
        console.error('Network error:', error);
    }
}

// Function to handle the travel button click event
async function handleTravelButtonClick(event) {
    try {
        // Get the clicked button and its parent form
        const buttonElement = event.target;
        const form = buttonElement.closest('.travel-form');

        // Get the current loc and travel-to value from the form
        const currLoc = form.querySelector('input[name="current-loc"]').value;
        const locName = form.querySelector('input[name="travel-to"]').value;

        if (currLoc == locName) {
            alert("You're already in " + locName + "!");
            return;
        }

        // Send the request
        await sendJetRequest({ loc: locName, status: "success" });

        // Reload the page after successful response
        window.location.reload();
    } catch (error) {
        console.error('Error:', error);
        alert("You cannot travel there.");
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
        button.addEventListener('click', handleTransactionButtonClick);
    });
}

// Event listener for each travel button
const travelButtons = document.querySelectorAll('.travel-button');
if (travelButtons) {
    travelButtons.forEach(button => {
        button.addEventListener('click', handleTravelButtonClick);
    });
}

// Event listener for each main view button
const mainViewButtons = document.querySelectorAll('.view-button');
if (mainViewButtons) {
    mainViewButtons.forEach(button => {
        button.addEventListener('click', handleViewButtonClick);
    });
}
