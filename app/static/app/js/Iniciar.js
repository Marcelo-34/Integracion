// Obtener los elementos del formulario
const form = document.querySelector('form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const submitButton = document.getElementById('submit-btn');

// Agregar un event listener al botón de enviar
submitButton.addEventListener('click', function(event) {
  
  event.preventDefault();

  // Validar el correo electrónico y la contraseña
  if (!validateEmail(emailInput.value)) {
    alert('Por favor, ingrese un correo electrónico válido');
    return;
  }

  if (!validatePassword(passwordInput.value)) {
    alert('La contraseña debe tener al menos 8 caracteres');
    return;
  }

  // Alerta de iniciar sesion
  
  window.location = "pagprincipal.html";
  
});

// Función para validar el correo electrónico
function validateEmail(email) {
  // Expresión regular para validar el correo electrónico
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

// Función para validar la contraseña
function validatePassword(password) {
  return password.length >= 8;
}
