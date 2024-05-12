// funciones.js

document.addEventListener('DOMContentLoaded', function () {
    var email = document.getElementById('email');
    var nombre = document.getElementById('user');
    var password = document.getElementById('password');
    var passwordRepeat = document.getElementById('password-repeat');
    var errorEmail = document.getElementById('error-email');
    var errorUser = document.getElementById('error-user');
    var errorPassword = document.getElementById('error-password');
    var errorPasswordRepeat = document.getElementById('error-password-repeat');
    var errorEdad = document.getElementById('error-edad');
    var registroMensaje = document.getElementById('registro-mensaje');
    
    function validarEmail() {
        var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!regex.test(email.value)) {
            errorEmail.textContent = 'Ingresa un correo electrónico válido';
            email.classList.add('incorrect');
        } else {
            errorEmail.textContent = '';
            email.classList.remove('incorrect');
            email.classList.add('correct');
        }
    }

    function validarUsuario() {
        if (nombre.value === null || nombre.value === '') {
            errorUser.textContent = 'Ingresa tu nombre de usuario';
            nombre.classList.add('incorrect');
        } else {
            errorUser.textContent = '';
            nombre.classList.remove('incorrect');
            nombre.classList.add('correct');
        }
    }

    function validarPassword() {
        if (password.value === null || password.value === '') {
            errorPassword.textContent = 'Ingresa tu contraseña';
            password.classList.add('incorrect');
        } else {
            errorPassword.textContent = '';
            password.classList.remove('incorrect');
            password.classList.add('correct');
        }
    }

    function validarPasswordRepetida() {
        if (passwordRepeat.value === null || passwordRepeat.value === '') {
            errorPasswordRepeat.textContent = 'Repite tu contraseña';
            passwordRepeat.classList.add('incorrect');
        } else if (password.value !== passwordRepeat.value) {
            errorPasswordRepeat.textContent = 'Las contraseñas no coinciden';
            passwordRepeat.classList.add('incorrect');
        } else {
            errorPasswordRepeat.textContent = '';
            passwordRepeat.classList.remove('incorrect');
            passwordRepeat.classList.add('correct');
        }
    }

    function validarEdad() {
        var edadInput = parseInt(document.getElementById('edad').value);
        if (isNaN(edadInput) || edadInput < 18 || edadInput > 99) {
            errorEdad.textContent = 'Ingresa una edad válida (entre 18 y 99 años)';
        } else {
            errorEdad.textContent = '';
        }
    }

    document.getElementById('form-login').addEventListener('submit', function (event) {
        event.preventDefault();
        validarEmail();
        validarUsuario();
        validarPassword();
        validarPasswordRepetida();
        validarEdad();

        var edadInput = parseInt(document.getElementById('edad').value);
        if (email.value !== '' && nombre.value !== '' && password.value !== '' && password.value === passwordRepeat.value && !isNaN(edadInput) && edadInput >= 18 && edadInput <= 99) {
            registroMensaje.textContent = 'Usuario registrado';
            registroMensaje.classList.add('registro-exito');
            console.log('Formulario válido. Enviando...');
        } else {
            console.log('Formulario inválido. Por favor, completa todos los campos correctamente.');
        }
    });
});
