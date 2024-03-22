function aparecer(){
    let menuMobile = document.querySelector('.mobileMenu');
    if(menuMobile.classList.contains('open')){
        menuMobile.classList.remove('open');
        let icone = document.querySelector('#icone');
        icone.className = "fa-solid fa-bars";
    }else{
        menuMobile.classList.add('open');
        let icone = document.querySelector('#icone');
        icone.className = "fa-solid fa-times"
        
    }
}

// Formulário
let form = document.querySelector('#form')
let nome = document.querySelector('#nome')
let email = document.querySelector('#emailF')
let assunto = document.querySelector('#mensagem')

window.addEventListener('submit', (enviar) => {
    enviar.preventDefault()
    //verificar se o nome esta vazio
    
    if(nome.value === ''){
        alert('Por favor, preencha seu nome!!!')
        return  
    }
    //Verificando se o email esta fazio e esta validando
    else if(email.value === '' || !validaremail(email.value)){
        alert('Por favor, preencha seu email!!!')
        return 
    }
    //Verificando se o assunto esta fazio
    else if(assunto.value === ''){
        alert('Por favor, Informe a Mensagem!!!')
        return 
    }
    form.submit()
})


    
    // função para validar o email
    function validaremail(email){
        let emailRegex = new RegExp(
            // criar uma regex para validar o email
            /^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$/
            )

            if(emailRegex.test(email)){
                return true
            }
                return false
            
        }

