
const BACKEND_URL = "https://whitby-bylaws-ai.fly.dev"; // Fly.io backend URL

function submitQuestion(event) {
    event.preventDefault();
    const query = document.getElementById('question').value.trim();
    if (!query) {
        showInputError('Please enter a question');
        return;
    }
    clearInputError();
    const submitButton = document.getElementById('submitButton');
    submitButton.disabled = true;
    submitButton.innerHTML = '<span>Processing...</span>';
    const loadingIndicator = document.getElementById('loadingIndicator');
    const answerContainer = document.getElementById('answerContainer');
    answerContainer.innerHTML = '';
    answerContainer.style.display = 'none';
    loadingIndicator.classList.add('show');

    fetch(`${BACKEND_URL}/api/ask`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query, bylaw_status: 'active' })
    })
    .then(response => {
        if (!response.ok) throw new Error(`Network error: ${response.status}`);
        return response.json();
    })
    .then(data => {
        setTimeout(() => {
            loadingIndicator.classList.remove('show');
            if (data.error) {
                displayError(data.error);
            } else {
                displayAnswer(data);
            }
            submitButton.disabled = false;
            submitButton.innerHTML = '<span>Get Answer</span>';
        }, 300);
    })
    .catch(error => {
        setTimeout(() => {
            loadingIndicator.classList.remove('show');
            displayError(`Failed to connect to backend: ${error.message}. Please try again later.`);
            submitButton.disabled = false;
            submitButton.innerHTML = '<span>Get Answer</span>';
        }, 300);
    });
}

function displayAnswer(data) {
    const answerContainer = document.getElementById('answerContainer');
    answerContainer.innerHTML = `
        <div class="answer">
            <p>${data.laymans_answer || 'No answer available.'}</p>
        </div>
    `;
    answerContainer.style.display = 'block';
}

function displayError(message) {
    const answerContainer = document.getElementById('answerContainer');
    answerContainer.innerHTML = `<div class="error"><p>${message}</p></div>`;
    answerContainer.style.display = 'block';
}

function showInputError(message) {
    const questionInput = document.getElementById('question');
    questionInput.classList.add('error-input');
    let errorElement = document.querySelector('.input-error-message');
    if (!errorElement) {
        errorElement = document.createElement('div');
        errorElement.className = 'input-error-message';
        questionInput.insertAdjacentElement('afterend', errorElement);
    }
    errorElement.textContent = message;
}

function clearInputError() {
    const questionInput = document.getElementById('question');
    questionInput.classList.remove('error-input');
    const errorElement = document.querySelector('.input-error-message');
    if (errorElement) errorElement.remove();
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('loadingIndicator').classList.remove('show');
    document.getElementById('answerContainer').style.display = 'none';
    document.getElementById('questionForm').addEventListener('submit', submitQuestion);
    document.getElementById('question').focus();
});