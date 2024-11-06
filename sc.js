document.addEventListener("DOMContentLoaded", function () {
    const collapsible = document.getElementById("col");
    const content = document.querySelector(".content");
    const homeworkBox = document.getElementById("homework-box");
    const taskHeader = document.getElementById("task");
    const taskCon = document.getElementById("task-con");

    collapsible.addEventListener("click", function () {
        // Check the current display status
        if (content.style.display === "block") {
            content.style.display = "none"; // Hide the content
            homeworkBox.style.height = "auto"; // Set to auto to shrink
        } else {
            content.style.display = "block"; // Show the content
            // Force a reflow to enable the transition
            homeworkBox.style.height = "auto"; // Reset height
            const height = homeworkBox.scrollHeight; // Get the new height
            homeworkBox.style.height = `${height}px`; // Set height to the new height
        }
    });



    taskHeader.addEventListener("click", function () {
        // Toggle the display of the task content
        if (taskCon.style.display === "block") {
            taskCon.style.display = "none"; // Hide the task content
        } else {
            taskCon.style.display = "block"; // Show the task content
            homeworkBox.style.height = "auto"; // Reset height
            const height = homeworkBox.scrollHeight; // Get the new height
            homeworkBox.style.height = `${height}px`; // Set height to the new height
        }
    });
});



// Create a theme manager module
const ThemeManager = {
    // Initialize theme management
    init() {
        this.toggleButton = document.getElementById("toggle-button");
        this.setupTheme();
        this.setupEventListeners();
    },

    // Apply the saved theme or default theme
    setupTheme() {
        const savedTheme = localStorage.getItem('theme') || 'light';
        if (savedTheme === 'dark') {
            this.enableDarkMode();
        } else {
            this.disableDarkMode();
        }
    },

    // Setup event listeners
    setupEventListeners() {
        if (this.toggleButton) {
            this.toggleButton.addEventListener("click", () => this.toggleTheme());
        }
    },

    // Toggle between light and dark themes
    toggleTheme() {
        if (document.body.classList.contains("dark-mode")) {
            this.disableDarkMode();
        } else {
            this.enableDarkMode();
        }
    },

    // Enable dark mode
    enableDarkMode() {
        document.body.classList.add("dark-mode");
        
        // Update themed elements
        const themedElements = document.querySelectorAll(
            '.navbar, .week-square, .inside-square, .hw-s, ' +
            '.collapse, .content, .Note, .list, .inside-rec1, ' +
            '.inside-rec11'
        );
        
        themedElements.forEach(element => {
            element.classList.add("dark-mode");
        });

        // Update button text
        if (this.toggleButton) {
            this.toggleButton.textContent = "Light Mode";
        }

        localStorage.setItem('theme', 'dark');
    },

    // Disable dark mode
    disableDarkMode() {
        document.body.classList.remove("dark-mode");
        
        // Update themed elements
        const themedElements = document.querySelectorAll(
            '.navbar, .week-square, .inside-square, .hw-s, ' +
            '.collapse, .content, .Note, .list, .inside-rec1, ' +
            '.inside-rec11'
        );
        
        themedElements.forEach(element => {
            element.classList.remove("dark-mode");
        });

        // Update button text
        if (this.toggleButton) {
            this.toggleButton.textContent = "Dark Mode";
        }

        localStorage.setItem('theme', 'light');
    }
};

// Initialize theme manager when DOM is loaded
document.addEventListener("DOMContentLoaded", () => ThemeManager.init());