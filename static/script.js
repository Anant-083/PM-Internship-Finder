// Loading state on form submit
document.addEventListener('DOMContentLoaded', function () {

    const form = document.querySelector('form');

    if (form) {
        form.addEventListener('submit', function () {
            const btn = document.querySelector('.btn-submit');
            btn.textContent = '🔍 Finding your matches...';
            btn.disabled = true;
            btn.style.opacity = '0.7';
        });
    }
});
