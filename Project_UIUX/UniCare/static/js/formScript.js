const firstName = document.getElementById('firstname');
const lastName = document.getElementById('lastname');
// const dateOfBirth
// const bloodGroup
const contactNumber = document.getElementById('contact-number');
const email = document.getElementById('e-mail');
// const gender = document.getElementById('');
const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirm-password');
const form = document.getElementById('FORM');
const errorElement = document.getElementById('error');



form.addEventListener('submit', (e) => {
    let messages = []
    //    if(password.value.length < 8){
    //     messages.push('Password should be atleast of 8 characters')
    //    }
    if (contactNumber.value.length != 10) {
        messages.push('Enter a Valid 10 Digit number')
    }
    if (password.value !== confirmPassword.value) {
        messages.push('Password entered are not same')
    }
    if (password.value.length < 8 ) {
        messages.push('Password should be atleast 8 digits')
    }
    if (firstName.value === '' || firstName.value == null) {
        messages.push('First Name is Required')
    }
    if (lastName.value === '' || lastName.value == null) {
        messages.push('Last Name is Required')
    }
    if (messages.length > 0) {
        e.preventDefault()
        errorElement.innerHTML = messages.join('<br>')
    }
})