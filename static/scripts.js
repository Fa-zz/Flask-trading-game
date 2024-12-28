const playButton = document.getElementById('play-button');
if (playButton) {
    playButton.addEventListener('click', () => {
        fetch('/api/start_game', { method: 'GET' })
            .then(response => response.json())
            .then(data => {
                console.log('Game started:', data);
                window.location.href = '/play';
            })
            .catch(error => console.error('Error starting game:', error));
    });
}