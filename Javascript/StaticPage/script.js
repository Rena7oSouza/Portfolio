const open_btn = document.querySelector('.open-btn');
const close_btn = document.querySelector('.close-btn');
const nav = document.querySelectorAll('.nav');
const mainContent = document.getElementById('main-content');

open_btn.addEventListener('click', () => {
    nav.forEach(nav_el => nav_el.classList.add('visible'));
    document.body.classList.add('menu-open'); // Adiciona a classe ao corpo
});

close_btn.addEventListener('click', () => {
    nav.forEach(nav_el => nav_el.classList.remove('visible'));
    document.body.classList.remove('menu-open'); // Remove a classe do corpo
    mainContent.classList.add('menu-closing'); // Adiciona a classe quando o menu começa a fechar
});

mainContent.addEventListener('transitionend', function() {
  mainContent.classList.remove('menu-closing'); // Remove a classe quando a transição terminar
});



// Seleciona todos os itens do menu
const menuItems = document.querySelectorAll('.list li a');

// Seleciona todas as seções
const sections = document.querySelectorAll('.section');

// Mapeamento entre o texto do item do menu e o ID da seção

const idMap = {
    'About Me': 'about',
    'Skills': 'skills',
    'Graduations': 'graduations',
    'Projects': 'projects',
    'HTML/CSS': 'html-css',
    'Python': 'python',
    'Javascript': 'javascript',
    'Unity': 'unity',
    'Contact Me': 'contact'
};

// Função para alterar o conteúdo
function changeContent(e) {
    e.preventDefault();
    const contentId = idMap[this.textContent];
    const contentElement = document.getElementById(contentId);
    if (contentElement) {
        // Esconde todas as seções
        sections.forEach(section => {
            section.style.display = 'none';
        });
        // Mostra a seção correspondente
        contentElement.style.display = 'block';
    }
}

// Adiciona o evento de clique a cada item do menu
menuItems.forEach(item => {
    item.addEventListener('click', changeContent);
});


// Adiciona o evento de clique a cada item do menu
menuItems.forEach(item => {
    item.addEventListener('click', changeContent);
});




let titles = ['Hello, I\'m Renato Souza', 'Welcome to my portfolio!'];
let i = 0;
let titleIndex = 0;

function typeWriter() {
    if (i < titles[titleIndex].length) {
        document.getElementById('text').innerHTML += titles[titleIndex].charAt(i);
        i++;
        setTimeout(typeWriter, 100);
    } else {
        document.getElementById('text').style.animation = 'none';
        let delayBeforeNextTitle = titles[titleIndex] === 'Hello, I\'m Renato Souza' ? 0 : 2000;
        setTimeout(() => {
            document.getElementById('text').innerHTML = '';
            document.getElementById('text').style.animation = '';
            i = 0;
            titleIndex = (titleIndex + 1) % titles.length;
            let newTitle = document.getElementById('text').cloneNode(true);
            document.getElementById('text').parentNode.replaceChild(newTitle, document.getElementById('text'));
            setTimeout(typeWriter, delayBeforeNextTitle);
        }, 3000);
    }
}

setTimeout(typeWriter, 4000);




