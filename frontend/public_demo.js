// In frontend/public_demo.js
fetch('https://whitby-bylaws-ai.onrender.com/api/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: query, bylaw_status: 'active' })
})