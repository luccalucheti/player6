//Testando o botão INSCREVA-SE

const btnIncricao = document.getElementById("btn-inscreva-se")
const paginaPopUp = document.getElementById("pagina-pop-up")

const dialogPopUp = document.getElementById("pop-up")
const closeBtn = document.getElementById("close-button")

const chaveamentoPopUp = document.getElementById("chaveamento-pop-up")
const closeChaveamento = document.getElementById("close-chaveamento")

const inputNomeTime = document.getElementById("btn-chaveamento")

//mostrar o menu
document.getElementById('menu').addEventListener('mouseover', function () {
    document.getElementById('menu').style.width = '14vw';
    document.getElementById('menu').style.boxShadow = '1px 1px 5px black';
});

document.getElementById('menu').addEventListener('mouseout', function () {
    document.getElementById('menu').style.width = '2vw';
    document.getElementById('menu').style.boxShadow = '';
});

//botoes no menu de navegação e no passo 1

const item_list1 = document.getElementById("menu-home")
const item_list2 = document.getElementById("menu-como-funciona")
const item_list3 = document.getElementById("menu-torneios")
const passo1 = document.getElementById("passo-1")

//botoes do menu de navegação e passo 1 scrollam a pagina:

item_list1.addEventListener("click", () => {
    document.getElementById("home").scrollIntoView({ behavior: 'smooth' });
});

item_list2.addEventListener("click", () => {
    document.getElementById("passo-2").scrollIntoView({ behavior: 'smooth', block: 'center' });
});

item_list3.addEventListener("click", () => {
    document.getElementById("inscricao-torneios").scrollIntoView({ behavior: 'smooth', block: 'center' });

});

passo1.addEventListener("click", () => {
    document.getElementById('inscricao-torneios').scrollIntoView({ behavior: 'smooth', block: 'center' });
});

btnIncricao.addEventListener("click", () => {
    dialogPopUp.showModal()
    document.body.classList.add('tira-rolagem');

})

dialogPopUp.addEventListener("keydown", (e) => {
    if (e.keyCode === 27) {
        document.body.classList.remove('tira-rolagem');
    }

})

closeBtn.addEventListener("click", () => {
    dialogPopUp.close()
    document.body.classList.remove('tira-rolagem')
})

inputNomeTime.addEventListener("click", () => {
    chaveamentoPopUp.showModal()
    document.body.classList.add('tira-rolagem')
})

closeChaveamento.addEventListener("click", function () {
    chaveamentoPopUp.close()
    document.body.classList.remove('tira-rolagem')

})

closeChaveamento.addEventListener("keydown", (e) => {
    if (e.keyCode === 27) {
        document.body.classList.remove('tira-rolagem');
    }

})