document.addEventListener("DOMContentLoaded", function () {
    // Collapsible content functionality
    const collapsible = document.getElementById("col");
    const content = document.querySelector(".content");
    const homeworkBox = document.getElementById("homework-box");
    const taskHeader = document.getElementById("task");
    const taskCon = document.getElementById("task-con");

    collapsible?.addEventListener("click", function () {
        if (content.style.display === "block") {
            content.style.display = "none";
            homeworkBox.style.height = "auto";
        } else {
            content.style.display = "block";
            homeworkBox.style.height = "auto";
            const height = homeworkBox.scrollHeight;
            homeworkBox.style.height = `${height}px`;
        }
    });

    taskHeader?.addEventListener("click", function () {
        if (taskCon.style.display === "block") {
            taskCon.style.display = "none";
        } else {
            taskCon.style.display = "block";
            homeworkBox.style.height = "auto";
            const height = homeworkBox.scrollHeight;
            homeworkBox.style.height = `${height}px`;
        }
    });

    // Dark mode toggle functionality
    const toggleButton = document.getElementById("toggle-button");

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        toggleButton.textContent = "Light Mode";
    } else {
        toggleButton.textContent = "Dark Mode";
    }

    toggleButton?.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");
        const allElements = document.querySelectorAll(".content, .Note, .list");

        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem('theme', 'dark');
            toggleButton.textContent = "Light Mode";
            allElements.forEach(el => el.classList.add('dark-mode'));
        } else {
            localStorage.setItem('theme', 'light');
            toggleButton.textContent = "Dark Mode";
            allElements.forEach(el => el.classList.remove('dark-mode'));
        }
    });

    // Toggle iframe functionality
    window.openIframe = function() {
        const iframeContainer = document.getElementById('iframe-container');
        const iframe = document.getElementById('pdf-iframe');
        const labBox = document.querySelector('.lab');
        const otherBoxes = document.querySelectorAll('.week-square, .hw-s, .inside-square');
        
        if (iframeContainer.style.display === 'none' || iframeContainer.style.display === '') {
            // Show the iframe and set the source to the PDF URL
            iframeContainer.style.display = 'block';
            iframe.src = "https://www.cs.rit.edu/~csci141/Recitations/10/exercise.pdf";
            labBox.classList.add('open'); // Move the lab box upwards
            otherBoxes.forEach(box => box.classList.add('open')); // Move other boxes out of view to the left
        } else {
            // Hide the iframe and clear the source
            iframeContainer.style.display = 'none';
            iframe.src = "";
            labBox.classList.remove('open'); // Reset the lab box position
            otherBoxes.forEach(box => box.classList.remove('open')); // Reset other boxes
        }
    };
});