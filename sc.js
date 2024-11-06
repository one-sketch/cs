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

document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("toggle-button");

    toggleButton.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode"); // Toggle dark mode class
        if (document.body.classList.contains("dark-mode")) {
            toggleButton.textContent = "Light Mode"; // Update button text
        } else {
            toggleButton.textContent = "Dark Mode"; // Reset button text
        }
    });
});

    
    

