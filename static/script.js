document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('speak');
    button.addEventListener('click', () => {
        const oldText = document.getElementById('old').innerText;
        const newText = document.getElementById('new').innerText;
        const commentary = document.getElementById('commentary').innerText;
        const utterance = new SpeechSynthesisUtterance(`${oldText}. ${newText}. ${commentary}`);
        window.speechSynthesis.speak(utterance);
    });
});
