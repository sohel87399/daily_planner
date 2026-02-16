// Theme Toggle Functionality
document.addEventListener('DOMContentLoaded', function() {
    const themeSwitch = document.getElementById('theme-switch');
    const body = document.body;
    
    // Check for saved theme preference or default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Apply saved theme on page load
    if (currentTheme === 'dark') {
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
        if (themeSwitch) {
            themeSwitch.checked = true;
        }
    } else {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
        if (themeSwitch) {
            themeSwitch.checked = false;
        }
    }
    
    // Theme toggle event listener
    if (themeSwitch) {
        themeSwitch.addEventListener('change', function() {
            if (this.checked) {
                // Switch to dark mode
                body.classList.remove('light-mode');
                body.classList.add('dark-mode');
                localStorage.setItem('theme', 'dark');
                
                // Add smooth transition effect
                body.style.transition = 'all 0.3s ease';
                
                // Show notification
                showThemeNotification('🌙 Dark mode activated');
            } else {
                // Switch to light mode
                body.classList.remove('dark-mode');
                body.classList.add('light-mode');
                localStorage.setItem('theme', 'light');
                
                // Add smooth transition effect
                body.style.transition = 'all 0.3s ease';
                
                // Show notification
                showThemeNotification('☀️ Light mode activated');
            }
        });
    }
    
    // Function to show theme change notification
    function showThemeNotification(message) {
        // Remove existing notification if any
        const existingNotification = document.querySelector('.theme-notification');
        if (existingNotification) {
            existingNotification.remove();
        }
        
        // Create notification element
        const notification = document.createElement('div');
        notification.className = 'theme-notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 80px;
            right: 20px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            z-index: 10000;
            animation: slideInRight 0.3s ease;
            font-size: 14px;
            font-weight: 500;
        `;
        
        // Add animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideInRight {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            @keyframes slideOutRight {
                from {
                    transform: translateX(0);
                    opacity: 1;
                }
                to {
                    transform: translateX(100%);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
        
        // Append to body
        document.body.appendChild(notification);
        
        // Remove after 2 seconds
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 2000);
    }
    
    // Keyboard shortcut: Ctrl/Cmd + Shift + D to toggle theme
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'D') {
            e.preventDefault();
            if (themeSwitch) {
                themeSwitch.checked = !themeSwitch.checked;
                themeSwitch.dispatchEvent(new Event('change'));
            }
        }
    });
});

// Auto theme based on system preference (optional)
function detectSystemTheme() {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        return 'dark';
    }
    return 'light';
}

// Listen for system theme changes
if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        const newTheme = e.matches ? 'dark' : 'light';
        const savedTheme = localStorage.getItem('theme');
        
        // Only auto-switch if user hasn't manually set a preference
        if (!savedTheme) {
            const themeSwitch = document.getElementById('theme-switch');
            const body = document.body;
            
            if (newTheme === 'dark') {
                body.classList.remove('light-mode');
                body.classList.add('dark-mode');
                if (themeSwitch) themeSwitch.checked = true;
            } else {
                body.classList.remove('dark-mode');
                body.classList.add('light-mode');
                if (themeSwitch) themeSwitch.checked = false;
            }
        }
    });
}
