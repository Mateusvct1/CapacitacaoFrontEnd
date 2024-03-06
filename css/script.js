function aparecer(){
    let menuMobile = document.querySelector('.mobile-menu');
    if(menuMobile.classList.contains('open')){
        menuMobile.classList.remove('open');
        let icone = document.querySelector('.icon');
        icone.src = "/FlexBox/Desafios/assets/img/menu_white_36dp.svg"
    }else{
        menuMobile.classList.add('open');
        let icone = document.querySelector('.icon');
        icone.src = "/FlexBox/Desafios/assets/img/close_white_36dp.svg"
        
    }
}