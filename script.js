document.addEventListener("DOMContentLoaded", function () {
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
});