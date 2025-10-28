function showToast(a, b, c = 'normal', d = 3000) {
    let title, message, type = 'normal', duration = 3000;
    if (arguments.length === 1) {
        message = a;
    } else if (arguments.length === 2) {
        if (b === 'success' || b === 'error' || b === 'normal') {
            message = a; type = b;
        } else {
            title = a; message = b;
        }
    } else {
        title = a; message = b; type = c; duration = d;
    }
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');

    // If toast markup isn't present, fall back to alert and console.warn
    if (!toastComponent) {
        console.warn('Toast component not found, falling back to alert.');
        if (message) alert(message);
        return;
    }

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-green-50', 'border-green-500', 'text-green-600',
        'bg-white', 'border-gray-300', 'text-gray-800'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-green-50', 'border-green-500', 'text-green-600');
        toastComponent.style.border = '1px solid #2a5bd9ff';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
        toastComponent.style.border = '1px solid #ef4444';
    } else {
        toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-800');
        toastComponent.style.border = '1px solid #d1d5db';
    }

    // If title not provided, hide title element (if exists)
    if (toastTitle) {
        if (title) {
            toastTitle.textContent = title;
            toastTitle.style.display = '';
        } else {
            toastTitle.style.display = 'none';
        }
    }
    if (toastMessage) toastMessage.textContent = message || '';

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}