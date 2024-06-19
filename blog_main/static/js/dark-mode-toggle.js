// Function to toggle dark mode and update button icon
function toggleDarkMode() {
    const darkModeStylesheet = document.getElementById('dark-mode-stylesheet');

    // Toggle dark mode stylesheet
    if (darkModeStylesheet.disabled) {
        darkModeStylesheet.href = '/static/css/dark-mode.css';
        darkModeStylesheet.disabled = false;
        localStorage.setItem('darkMode', 'enabled');
        // Change button icon to sun
        document.getElementById('darkModeIcon').classList.remove('fa-moon-o');
        document.getElementById('darkModeIcon').classList.add('fa-regular', 'fa-sun');
    } else {
        darkModeStylesheet.disabled = true;
        localStorage.setItem('darkMode', 'disabled');
        // Change button icon back to moon
        document.getElementById('darkModeIcon').classList.remove('fa-regular', 'fa-sun');
        document.getElementById('darkModeIcon').classList.add('fa-moon-o');
    }
}

// Load the correct mode and update button icon on page load
document.addEventListener('DOMContentLoaded', (event) => {
    const darkModeStylesheet = document.getElementById('dark-mode-stylesheet');
    if (localStorage.getItem('darkMode') === 'enabled') {
        darkModeStylesheet.href = '/static/css/dark-mode.css';
        darkModeStylesheet.disabled = false;
        // Change button icon to sun
        document.getElementById('darkModeIcon').classList.remove('fa-moon-o');
        document.getElementById('darkModeIcon').classList.add('fa-regular', 'fa-sun');
    } else {
        darkModeStylesheet.disabled = true;
        // Change button icon back to moon (default state)
        document.getElementById('darkModeIcon').classList.remove('fa-regular', 'fa-sun');
        document.getElementById('darkModeIcon').classList.add('fa-moon-o');
    }
});
