document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const registerButton = document.querySelector('.register-button');
    const backButton = document.querySelector('.back-button');

    // Ocultar el formulario de registro al principio
    registerForm.style.display = 'none';

    // Cambiar al formulario de registro al hacer clic en "Registrarse"
    registerButton.addEventListener('click', function () {
        loginForm.style.display = 'none';
        registerForm.style.display = 'block';
    });

    // Cambiar al formulario de inicio de sesión al hacer clic en "Volver"
    backButton.addEventListener('click', function () {
        registerForm.style.display = 'none';
        loginForm.style.display = 'block';
    });
});
