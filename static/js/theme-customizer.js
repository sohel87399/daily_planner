/* ========================================
   THEME CUSTOMIZER - DYNAMIC COLOR SYSTEM
   ======================================== */

// Predefined color themes
const colorThemes = [
    { name: 'Professional Blue', primary: '#2563EB', hover: '#1E40AF' },
    { name: 'Ocean Teal', primary: '#0891B2', hover: '#0E7490' },
    { name: 'Success Green', primary: '#16A34A', hover: '#15803D' },
    { name: 'Royal Purple', primary: '#7C3AED', hover: '#6D28D9' },
    { name: 'Sunset Orange', primary: '#EA580C', hover: '#C2410C' },
    { name: 'Rose Pink', primary: '#E11D48', hover: '#BE123C' },
    { name: 'Indigo Deep', primary: '#4F46E5', hover: '#4338CA' },
    { name: 'Emerald', primary: '#059669', hover: '#047857' }
];

let currentTheme = {
    primary: '#2563EB',
    hover: '#1E40AF'
};

// Initialize theme customizer
document.addEventListener('DOMContentLoaded', function() {
    initializeCustomizer();
    loadSavedTheme();
});

function initializeCustomizer() {
    const toggleBtn = document.querySelector('.customizer-toggle');
    const panel = document.querySelector('.customizer-panel');
    
    if (!toggleBtn || !panel) return;
    
    // Toggle panel
    toggleBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        panel.classList.toggle('active');
    });
    
    // Close panel when clicking outside
    document.addEventListener('click', function(e) {
        if (!panel.contains(e.target) && !toggleBtn.contains(e.target)) {
            panel.classList.remove('active');
        }
    });
    
    // Color selection
    const colorOptions = document.querySelectorAll('.color-option');
    colorOptions.forEach((option, index) => {
        option.addEventListener('click', function() {
            selectColor(index);
        });
    });
    
    // Mode selection
    const modeBtns = document.querySelectorAll('.mode-btn');
    modeBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const mode = this.dataset.mode;
            switchMode(mode);
        });
    });
    
    // Reset button
    const resetBtn = document.querySelector('.reset-btn');
    if (resetBtn) {
        resetBtn.addEventListener('click', resetToDefault);
    }
    
    // Save button
    const saveBtn = document.querySelector('.save-btn');
    if (saveBtn) {
        saveBtn.addEventListener('click', saveThemePreference);
    }
}

function selectColor(index) {
    const theme = colorThemes[index];
    currentTheme = theme;
    
    // Update active state
    document.querySelectorAll('.color-option').forEach(opt => {
        opt.classList.remove('active');
    });
    document.querySelectorAll('.color-option')[index].classList.add('active');
    
    // Apply theme
    applyTheme(theme.primary, theme.hover);
    
    // Update center display
    const center = document.querySelector('.color-wheel-center');
    if (center) {
        center.style.background = theme.primary;
        center.textContent = theme.name;
    }
    
    // Update preview
    updatePreview(theme.primary, theme.hover);
}

function applyTheme(primaryColor, hoverColor) {
    const root = document.documentElement;
    
    // Set CSS variables
    root.style.setProperty('--primary-color', primaryColor);
    root.style.setProperty('--primary-hover', hoverColor);
    
    // Apply to various elements
    applyToElements(primaryColor, hoverColor);
}

function applyToElements(primaryColor, hoverColor) {
    // Navbar brand
    const navBrand = document.querySelector('.nav-brand');
    if (navBrand && !document.body.classList.contains('dark-mode')) {
        navBrand.style.color = primaryColor;
    }
    
    // Buttons
    const buttons = document.querySelectorAll('.btn:not(.btn-secondary)');
    buttons.forEach(btn => {
        btn.style.background = `linear-gradient(135deg, ${hoverColor}, ${primaryColor})`;
    });
    
    // Links
    const links = document.querySelectorAll('a:not(.nav-links a)');
    links.forEach(link => {
        if (!link.classList.contains('btn')) {
            link.style.color = primaryColor;
        }
    });
    
    // Progress bar
    const progressFill = document.querySelector('.progress-fill');
    if (progressFill) {
        progressFill.style.background = `linear-gradient(90deg, ${hoverColor}, ${primaryColor})`;
    }
    
    // Stat values
    const statValues = document.querySelectorAll('.stat-value');
    statValues.forEach(stat => {
        stat.style.color = primaryColor;
    });
    
    // Calendar header
    const calendarHeader = document.querySelector('.calendar-header');
    if (calendarHeader) {
        calendarHeader.style.background = primaryColor;
    }
    
    // Day links
    const dayLinks = document.querySelectorAll('.day-link');
    dayLinks.forEach(link => {
        link.style.color = primaryColor;
    });
    
    // Quote text
    const quoteText = document.querySelector('.quote-card p');
    if (quoteText && !document.body.classList.contains('dark-mode')) {
        quoteText.style.color = primaryColor;
    }
    
    // Comparison cards
    const comparisonCards = document.querySelectorAll('.comparison-card');
    comparisonCards.forEach(card => {
        card.style.background = `linear-gradient(135deg, ${hoverColor}, ${primaryColor})`;
    });
    
    // Active mode button
    const activeMode = document.querySelector('.mode-btn.active');
    if (activeMode) {
        activeMode.style.background = primaryColor;
        activeMode.style.borderColor = primaryColor;
    }
}

function switchMode(mode) {
    // Update active state
    document.querySelectorAll('.mode-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`[data-mode="${mode}"]`).classList.add('active');
    
    // Apply mode
    if (mode === 'dark') {
        document.body.classList.add('dark-mode');
        localStorage.setItem('theme-mode', 'dark');
    } else if (mode === 'light') {
        document.body.classList.remove('dark-mode');
        localStorage.setItem('theme-mode', 'light');
    } else if (mode === 'custom') {
        // Custom mode uses current theme
        localStorage.setItem('theme-mode', 'custom');
    }
    
    // Reapply current color theme
    applyTheme(currentTheme.primary, currentTheme.hover);
}

function updatePreview(primaryColor, hoverColor) {
    const previewItems = document.querySelectorAll('.preview-color');
    if (previewItems.length >= 2) {
        previewItems[0].style.background = primaryColor;
        previewItems[1].style.background = hoverColor;
    }
}

function resetToDefault() {
    const defaultTheme = colorThemes[0]; // Professional Blue
    currentTheme = defaultTheme;
    
    // Reset to light mode
    document.body.classList.remove('dark-mode');
    localStorage.setItem('theme-mode', 'light');
    
    // Update mode buttons
    document.querySelectorAll('.mode-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector('[data-mode="light"]').classList.add('active');
    
    // Apply default theme
    selectColor(0);
    
    // Clear saved theme
    localStorage.removeItem('theme-color');
    
    // Show success message
    showSuccessMessage('Reset to default theme!');
}

function saveThemePreference() {
    const username = document.body.dataset.username;
    
    if (!username) {
        showSuccessMessage('Please login to save theme!');
        return;
    }
    
    const themeData = {
        primary_color: currentTheme.primary,
        hover_color: currentTheme.hover,
        theme_name: currentTheme.name,
        mode: localStorage.getItem('theme-mode') || 'light'
    };
    
    // Save to localStorage
    localStorage.setItem('theme-color', currentTheme.primary);
    localStorage.setItem('theme-hover', currentTheme.hover);
    localStorage.setItem('theme-name', currentTheme.name);
    
    // Save to database via AJAX
    fetch('/api/save-theme', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(themeData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showSuccessMessage('Theme saved successfully!');
        } else {
            showSuccessMessage('Failed to save theme');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showSuccessMessage('Theme saved locally!');
    });
}

function loadSavedTheme() {
    // Load from localStorage first
    const savedPrimary = localStorage.getItem('theme-color');
    const savedHover = localStorage.getItem('theme-hover');
    const savedName = localStorage.getItem('theme-name');
    const savedMode = localStorage.getItem('theme-mode');
    
    if (savedPrimary && savedHover) {
        currentTheme = {
            name: savedName || 'Custom',
            primary: savedPrimary,
            hover: savedHover
        };
        
        applyTheme(savedPrimary, savedHover);
        
        // Find and activate matching color
        const matchingIndex = colorThemes.findIndex(t => t.primary === savedPrimary);
        if (matchingIndex !== -1) {
            selectColor(matchingIndex);
        }
    }
    
    // Apply saved mode
    if (savedMode === 'dark') {
        document.body.classList.add('dark-mode');
        const darkBtn = document.querySelector('[data-mode="dark"]');
        if (darkBtn) darkBtn.classList.add('active');
    } else if (savedMode === 'custom') {
        const customBtn = document.querySelector('[data-mode="custom"]');
        if (customBtn) customBtn.classList.add('active');
    }
    
    // Load from server if logged in
    const username = document.body.dataset.username;
    if (username) {
        fetch('/api/get-theme')
            .then(response => response.json())
            .then(data => {
                if (data.theme_color) {
                    currentTheme = {
                        name: data.theme_name || 'Custom',
                        primary: data.theme_color,
                        hover: data.hover_color || data.theme_color
                    };
                    
                    applyTheme(currentTheme.primary, currentTheme.hover);
                    
                    // Find and activate matching color
                    const matchingIndex = colorThemes.findIndex(t => t.primary === currentTheme.primary);
                    if (matchingIndex !== -1) {
                        selectColor(matchingIndex);
                    }
                }
            })
            .catch(error => console.error('Error loading theme:', error));
    }
}

function showSuccessMessage(message) {
    const successDiv = document.querySelector('.save-success');
    if (successDiv) {
        successDiv.textContent = message;
        successDiv.classList.add('show');
        
        setTimeout(() => {
            successDiv.classList.remove('show');
        }, 3000);
    }
}

// Keyboard shortcut: Ctrl+Shift+T to toggle customizer
document.addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.shiftKey && e.key === 'T') {
        e.preventDefault();
        const panel = document.querySelector('.customizer-panel');
        if (panel) {
            panel.classList.toggle('active');
        }
    }
});
