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

// Event listener for the play button
const playButton = document.getElementById('play-button');
if (playButton) {
    playButton.addEventListener('click', handlePlayButtonClick);
}
