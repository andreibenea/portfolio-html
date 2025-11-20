document.addEventListener("DOMContentLoaded", function () {
    if (document.title === "Portfolio :: Contact") {
        const phoneInput = document.getElementById("phone");

        phoneInput.addEventListener("input", function (event) {
            let input = phoneInput.value.replace(/\D/g, '');
            if (input.length > 3 && input.length <= 6) {
                phoneInput.value = input.slice(0, 3) + '-' + input.slice(3);
            } else if (input.length > 6) {
                phoneInput.value = input.slice(0, 3) + '-' + input.slice(3, 6) + '-' + input.slice(6, 10);
            } else {
                phoneInput.value = input;
            }
        });
    }

    if (document.title === "Projects :: Rock Paper Scissors") {
        let playerScore = 0
        let computerScore = 0
        const rock = document.getElementById("rock")
        const paper = document.getElementById("paper")
        const scissors = document.getElementById("scissors")
        const computerScoreElement = document.getElementById("computerScore")
        const playerScoreElement = document.getElementById("playerScore")

        function playGame(playerChoice) {
            function getRandomInt(max) {
                return Math.floor(Math.random() * max);
            }
            let computerChoice = getRandomInt(3)
            switch (computerChoice) {
                case 0:
                    computerChoice = "rock"
                    break;
                case 1:
                    computerChoice = "paper"
                    break;
                case 2:
                    computerChoice = "scissors"
                    break;
            }

            if (computerChoice == playerChoice) {
                alert("It's a draw!")
            }
            else if (computerChoice == "rock" && playerChoice == "paper" ||
                computerChoice == "paper" && playerChoice == "scissors" ||
                computerChoice == "scissors" && playerChoice == "rock") {
                alert("Congratulations, YOU won!")
                playerScore += 1
                playerScoreElement.textContent = "Player: " + playerScore
            }
            else {
                alert("The Computer won. Better luck next time!")
                computerScore += 1
                computerScoreElement.textContent = "Computer: " + computerScore
            }
        }

        rock.addEventListener("click", (event) => {
            playerChoice = "rock"
            playGame(playerChoice)
        })
        paper.addEventListener("click", (event) => {
            playerChoice = "paper"
            playGame(playerChoice)
        })
        scissors.addEventListener("click", (event) => {
            playerChoice = "scissors"
            playGame(playerChoice)
        })
    }

    const caret = document.getElementById("caret")
    caret.addEventListener("click", (event) => {
        const dropdownContent = document.getElementById("dropdown-content")
        const mobileScreen = window.matchMedia("(max-width: 426px)").matches
        if (mobileScreen) {
            if (dropdownContent.style.display == "none") {
                dropdownContent.style.display = "flex"
                dropdownContent.style.flexDirection = "column"
            }
            else {
                dropdownContent.style.display = "none"
            }
        }
    })

    const currentTheme = localStorage.getItem("theme")
    const toggle = document.getElementById("toggle")
    const home = document.getElementById("home")
    const wrapper = document.getElementById("wrapper")
    const dropdown = document.getElementById("dropdown-content")
    const anchors = document.getElementsByTagName("a")
    const footers = document.getElementsByTagName("footer")
    const inputs = document.getElementsByTagName("input")

    if (currentTheme == "dark") {
        document.body.classList.toggle("dark-mode")
        toggle.classList.toggle("dark-mode")
        home.classList.toggle("dark-mode")
        wrapper.classList.toggle("dark-mode")
        dropdown.classList.toggle("dark-mode")
        for (const anchor of anchors) {
            anchor.classList.toggle("dark-mode")
        }
        for (const footer of footers) {
            footer.classList.toggle("dark-mode")
        }
        for (const input of inputs) {
            input.classList.toggle("dark-mode")
        }
    }

    toggle.addEventListener("click", (event) => {
        document.body.classList.toggle("dark-mode")
        toggle.classList.toggle("dark-mode")
        home.classList.toggle("dark-mode")
        wrapper.classList.toggle("dark-mode")
        dropdown.classList.toggle("dark-mode")
        for (const anchor of anchors) {
            anchor.classList.toggle("dark-mode")
        }
        for (const footer of footers) {
            footer.classList.toggle("dark-mode")
        }
        for (const input of inputs) {
            input.classList.toggle("dark-mode")
        }

        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("theme", "dark");
        } else {
            localStorage.setItem("theme", "light");
        }
    })
    // --- Video swapping helpers ---
    function updatePanelVideo() {
        const vLight = document.getElementById("panel-video-light");
        const vDark = document.getElementById("panel-video-dark");
        if (!vLight || !vDark) return;

        const isDark = document.body.classList.contains("dark-mode");

        // Pause the one we don't see, play the active one
        if (isDark) {
            vLight.pause();
            vDark.play().catch(() => { });
        } else {
            vDark.pause();
            vLight.play().catch(() => { });
        }
    }

    // Play/pause when tab visibility changes (saves battery/CPU)
    document.addEventListener("visibilitychange", () => {
        const vLight = document.getElementById("panel-video-light");
        const vDark = document.getElementById("panel-video-dark");
        if (!vLight || !vDark) return;

        const active = document.body.classList.contains("dark-mode") ? vDark : vLight;
        if (document.hidden) active.pause();
        else active.play().catch(() => { });
    });

    // Run once on load
    document.addEventListener("DOMContentLoaded", updatePanelVideo);

    // Re-run after your theme toggle runs
    (function hookThemeToggle() {
        const toggle = document.getElementById("toggle");
        if (!toggle) return;
        toggle.addEventListener("click", () => {
            // your code toggles classes immediately; give the DOM a tick then sync videos
            setTimeout(updatePanelVideo, 0);
        });
    })();
    // --- Demo info dropdown (for iframe instructions) ---
    const demoHeader = document.querySelector(".demo-info-header");
    const demoWrapper = document.querySelector(".demo-info");

    if (demoHeader && demoWrapper) {
        demoHeader.addEventListener("click", () => {
            demoWrapper.classList.toggle("demo-open");
        });
    }

});