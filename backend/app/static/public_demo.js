document.getElementById('query-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const query = document.getElementById('query').value;
    const responseDiv = document.getElementById('response');
    responseDiv.textContent = 'Loading...';
    try {
        const res = await fetch('/api/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });
        const data = await res.json();
        responseDiv.textContent = data.answer || 'No answer found.';
    } catch (err) {
        responseDiv.textContent = 'Error: ' + err.message;
    }
});
