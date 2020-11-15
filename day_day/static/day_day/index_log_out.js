document.addEventListener('DOMContentLoaded', function() {

    window.scrollTo(0, 0)
    let registerDivs = document.querySelectorAll('#register-div')
    let loginDivs = document.querySelectorAll('#log-in-div')

    var i

    for(i = 0; i < registerDivs.length; i++) {
        registerDivs[i].style.opacity = 0.4
        registerDivs[i].addEventListener('click', registerChange)
    }

    for(i = 0; i < loginDivs.length; i++) {
        loginDivs[i].addEventListener('click', logInChange)
    }

    let buttons_one = document.querySelectorAll('#button-one-next')

    for(i=0; i < buttons_one.length; i++) {
        buttons_one[i].addEventListener('click', buttonOne)
    }

    let buttons_two = document.querySelectorAll('#button-two-next')

    for(i=0; i < buttons_one.length; i++) {
        buttons_two[i].addEventListener('click', buttonTwo)
    }
    
})

function registerChange() {

    let registerDivs = document.querySelectorAll('#register-div')
    let loginDivs = document.querySelectorAll('#log-in-div')

    var i

    for(i = 0; i < registerDivs.length; i++) {
        registerDivs[i].style.opacity = 1
    }

    for(i = 0; i < loginDivs.length; i++) {
        loginDivs[i].style.opacity = 0.4
    }

    let registers = document.querySelectorAll('#register')
    let logins = document.querySelectorAll('#login')

    let lenRegister = registers.length
    let lenLogin = logins.length

    var i

    for (i = 0; i < lenRegister; i++) {
        registers[i].style.display = 'block'
    }

    for (i = 0; i < lenLogin; i++) {
        logins[i].style.display = 'none'
    }

}

function logInChange() {

    let registerDivs = document.querySelectorAll('#register-div')
    let loginDivs = document.querySelectorAll('#log-in-div')

    var i

    for(i = 0; i < registerDivs.length; i++) {
        registerDivs[i].style.opacity = 0.4
    }

    for(i = 0; i < loginDivs.length; i++) {
        loginDivs[i].style.opacity = 1
    }

    let registers = document.querySelectorAll('#register')
    let logins = document.querySelectorAll('#login')

    let lenRegister = registers.length
    let lenLogin = logins.length

    var i

    for (i = 0; i < lenRegister; i++) {
        registers[i].style.display = 'none'
    }

    for (i = 0; i < lenLogin; i++) {
        logins[i].style.display = 'block'
    }

    let nameForms = document.querySelectorAll('.name-register')
    let userMailForms = document.querySelectorAll('.username-mail-register')
    let passwordForms = document.querySelectorAll('.password-register')

    for(i=0; i < nameForms.length; i++) {
        nameForms[i].style.display = 'block'
    } for(i=0; i < userMailForms.length; i++) {
        userMailForms[i].style.display = 'none'
    } for(i=0; i < passwordForms.length; i++) {
        passwordForms[i].style.display = 'none'
    }
    
}

function buttonOne() {

    let nameForms = document.querySelectorAll('.name-register')
    let userMailForms = document.querySelectorAll('.username-mail-register')

    var i
    for (i=0; i < nameForms.length; i++) {
        nameForms[i].style.display = 'none'
    } for (i=0; i < userMailForms.length; i++) {
        userMailForms[i].style.display = 'block'
    }

}

function buttonTwo() {

    let userMailForms = document.querySelectorAll('.username-mail-register')
    let passwordForms = document.querySelectorAll('.password-register')

    var i
    for(i=0; i < userMailForms.length; i++) {
        userMailForms[i].style.display = 'none'
    } for(i=0; i < passwordForms.length; i++) {
        passwordForms[i].style.display = 'block'
    }

}




