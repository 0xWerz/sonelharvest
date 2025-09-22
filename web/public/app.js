const form = document.querySelector('.data-form');
const submitBtn = document.querySelector('.submit-btn');
const statusMessage = document.getElementById('status');
const resultsTextarea = document.getElementById('results');
const copyBtn = document.getElementById('copy-btn');

// Form submission handler
form.addEventListener('submit', (e) => {
    e.preventDefault();

    const country = document.getElementById('country').value.trim() || 'DZ';
    const target = document.getElementById('target').value.trim() || 'power';
    const tagsInput = document.getElementById('tags').value.trim();

    if (!tagsInput) {
        showStatus('Please enter the tags to query', 'error');
        return;
    }

    const tags = tagsInput.replace(/\s+/g, '').split(',').filter(tag => tag.length > 0);

    if (tags.length === 0) {
        showStatus('Please enter valid tags to query', 'error');
        return;
    }

    sendForm(country, target, tags);
});

// Copy button functionality
copyBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(resultsTextarea.value).then(() => {
        copyBtn.textContent = '✓ Copied!';
        setTimeout(() => {
            copyBtn.textContent = '📋 Copy';
        }, 2000);
    }).catch(() => {
        // Fallback for older browsers
        resultsTextarea.select();
        document.execCommand('copy');
        copyBtn.textContent = '✓ Copied!';
        setTimeout(() => {
            copyBtn.textContent = '📋 Copy';
        }, 2000);
    });
});

function showStatus(message, type) {
    statusMessage.textContent = message;
    statusMessage.className = `status-message ${type}`;
}

function hideStatus() {
    statusMessage.className = 'status-message';
}

function setLoading(loading) {
    submitBtn.classList.toggle('loading', loading);
    submitBtn.disabled = loading;

    if (loading) {
        showStatus('Processing your request...', 'loading');
    }
}

function sendForm(country, target, tags) {
    setLoading(true);
    hideStatus();
    copyBtn.style.display = 'none';
    resultsTextarea.value = '';

    fetch('/api/export', {
        method: 'POST',
        body: JSON.stringify({
            country,
            target,
            tags
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(async (res) => {
        const data = await res.json();

        if (res.status !== 200) {
            throw new Error(data.error || 'Unknown error occurred');
        }

        return data;
    })
    .then((data) => {
        setLoading(false);
        showStatus('Data extracted successfully!', 'success');
        resultsTextarea.value = JSON.stringify(data, null, 2);
        copyBtn.style.display = 'block';

        // Auto-hide success message after 3 seconds
        setTimeout(() => {
            hideStatus();
        }, 3000);
    })
    .catch((error) => {
        setLoading(false);
        showStatus(`Error: ${error.message}`, 'error');
        console.error('Error:', error);
    });
}

// Auto-resize textarea based on content
resultsTextarea.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.max(400, this.scrollHeight) + 'px';
});

// Add some interactive features
document.querySelectorAll('input, select').forEach(element => {
    element.addEventListener('focus', () => {
        element.parentElement.classList.add('focused');
    });

    element.addEventListener('blur', () => {
        element.parentElement.classList.remove('focused');
    });
});