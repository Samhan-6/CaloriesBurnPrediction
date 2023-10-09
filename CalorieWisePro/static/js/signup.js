document.addEventListener("DOMContentLoaded", function () {
    // Get the password input element
    var password = document.getElementById("id_password1");

    // Get the password strength element
    var strength = document.getElementById("password-strength");

    // Get the register button element
    var register = document.getElementById("register-button");

    // Define an array of messages for different password strengths
    var messages = [
        "Very weak",
        "Weak",
        "Medium",
        "Strong",
        "Very strong"
    ];

    // Define an array of colors for different password strengths
    var colors = [
        "#ff0000",
        "#ff6600",
        "#ffff00",
        "#66ff00",
        "#00ff00"
    ];

    // Define a function to check the password strength
    function checkPasswordStrength() {
        // Get the value of the password input
        var value = password.value;

        // Initialize a score variable
        var score = 0;

        // Check if the password is empty
        if (value.length == 0) {
            // Set the strength message and color to empty
            strength.innerHTML = "";
            strength.style.backgroundColor = "#ffffff";

            // Disable the register button
            register.disabled = true;
            return;
        }

        // Check if the password has at least 8 characters
        if (value.length >= 8) {
            // Increase the score by 1
            score++;
        }

        // Check if the password has at least one lowercase letter
        if (/[a-z]/.test(value)) {
            // Increase the score by 1
            score++;
        }

        // Check if the password has at least one uppercase letter
        if (/[A-Z]/.test(value)) {
            // Increase the score by 1
            score++;
        }

        // Check if the password has at least one number
        if (/[0-9]/.test(value)) {
            // Increase the score by 1
            score++;
        }

        // Check if the password has at least one special character
        if (/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(value)) {
            // Increase the score by 1
            score++;
        }

        // Set the strength message and color based on the score
        strength.innerHTML = messages[score];
        strength.style.backgroundColor = colors[score];

        // Enable the register button if the score is at least 3
        if (score >= 3) {
            register.disabled = false;
        } else {
            register.disabled = true;
        }
    }

    // Add an event listener to the password input to check the strength on every input
    if (password) {
        password.addEventListener("input", checkPasswordStrength);
    }
});
