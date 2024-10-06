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
        function playGame() {
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
                default:
                    console.log("Something went wrong. Please try again!")
                    break;
            }
            return computerChoice
        }

        const rock = document.getElementById("rock")
        const paper = document.getElementById("paper")
        const scissors = document.getElementById("scissors")

        rock.addEventListener("click", (event) => {
            playerChoice = "rock"
            computerChoice = playGame()
            console.log("You chose: " + playerChoice)
            console.log("Computer chose: " + computerChoice)
            switch (computerChoice) {
                case "rock":
                    alert("It's a draw")
                    break;
                case "paper":
                    alert("The computer has won!")
                    break;
                case "scissors":
                    alert("Congratulations, you won!")
                    break;
                default:
                    console.log("Something went wrong. Please try again!")
                    break;
            }
        })
        paper.addEventListener("click", (event) => {
            playerChoice = "paper"
            computerChoice = playGame()
            console.log("You chose: " + playerChoice)
            console.log("Computer chose: " + computerChoice)
            switch (computerChoice) {
                case "rock":
                    alert("Congratulations, you won!")
                    break;
                case "paper":
                    alert("It's a draw")
                    break;
                case "scissors":
                    alert("The computer has won!")
                    break;
                default:
                    console.log("Something went wrong. Please try again!")
                    break;
            }
        })
        scissors.addEventListener("click", (event) => {
            playerChoice = "scissors"
            computerChoice = playGame()
            console.log("You chose: " + playerChoice)
            console.log("Computer chose: " + computerChoice)
            switch (computerChoice) {
                case "rock":
                    alert("The computer has won!")
                    break;
                case "paper":
                    alert("Congratulations, you won!")
                    break;
                case "scissors":
                    alert("It's a draw")
                    break;
                default:
                    console.log("Something went wrong. Please try again!")
                    break;
            }
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
});