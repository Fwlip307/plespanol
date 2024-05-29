function validarUsuario() {
    let user = document.querySelector("#user");
    let username = user.value;
    let errorUser = document.querySelector("#error-user");
    
    // Verifica si la primera letra es mayúscula y no contiene símbolos
    let firstLetterUpperCase = /^[A-Z][a-zA-Z0-9]*$/;
    
    if(username.length >= 6 && firstLetterUpperCase.test(username)) {
        user.classList.add("correct");
        user.classList.remove("incorrect");
        errorUser.innerHTML = "&nbsp;";
    } else {
        user.classList.remove("correct");
        user.classList.add("incorrect");
        errorUser.innerHTML = "El usuario debe tener al menos 6 caracteres, comenzar con mayúscula y no contener símbolos.";
    }
}

function validarPassword() {
    let password = document.querySelector("#password");
    let passValue = password.value;
    let errorPassword = document.querySelector("#error-password");
    
    // Verifica si la contraseña tiene al menos 8 caracteres, 1 mayúscula, 2 números y 1 símbolo
    let passRegex = /^(?=.*[A-Z])(?=.*\d{2,})(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$/;
    
    if(passRegex.test(passValue)) {
        password.classList.add("correct");
        password.classList.remove("incorrect");
        errorPassword.innerHTML = "&nbsp;";
    } else {
        password.classList.remove("correct");
        password.classList.add("incorrect");
        errorPassword.innerHTML = "La contraseña debe tener al menos 8 caracteres, incluyendo 1 mayúscula, 2 números y 1 símbolo.";
    }
}

function iniciarSesion() {
    validarUsuario();
    validarPassword();
    // Agregar lógica para iniciar sesión aquí
}
