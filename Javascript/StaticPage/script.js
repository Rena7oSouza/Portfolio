const open_btn = document.querySelector('.open-btn')
const close_btn = document.querySelector('.close-btn')
const nav = document.querySelectorAll('.nav')

open_btn.addEventListener('click', () => {
    nav.forEach(nav_el => nav_el.classList.add('visible'))
})

close_btn.addEventListener('click', () => {
    nav.forEach(nav_el => nav_el.classList.remove('visible'))
})

const textElement = document.getElementById('text');
const textContent = "Mobile Navigation";
const cursor = document.createElement('span');
cursor.classList.add('cursor');

function typeWriter() {
    let i = 0;
    const typing = setInterval(() => {
        if (i < textContent.length) {
            textElement.innerHTML += textContent[i];
            i++;
        } else {
            clearInterval(typing);
            textElement.parentNode.insertBefore(cursor, textElement.nextSibling); // Adicionando o cursor após o texto
            cursor.style.visibility = 'visible'; // Mostra o cursor
            setTimeout(() => {
                textElement.innerHTML = ''; // Limpa o texto
                cursor.style.visibility = 'hidden'; // Esconde o cursor
                i = 0;
                typeWriter();
            }, 5000); // Digita novamente após 5 segundos
        }
    }, 100);
}

typeWriter();
