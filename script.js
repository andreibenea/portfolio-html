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
});