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


