const scriptURL = 'https://script.google.com/macros/s/AKfycbxswPTLdDvmXs3EKegd-YOkwIL5aDWr0_JtSA8CfLWvml-0_tPPAwjligsHYUMDik16/exec'            
const form = document.forms['Contacts-form']
form.addEventListener('submit', e => {
  e.preventDefault()
  fetch(scriptURL, { method: 'POST', body: new FormData(form)})
    .then(response => alert("Thank you for contacting us . Our team will get back to you shortly."))
     
     setTimeout(function()
     {
          success.innerHTML="";
     },5000)
     form.reset()
    })
    .catch(error => console.error('Error!', error.message))
