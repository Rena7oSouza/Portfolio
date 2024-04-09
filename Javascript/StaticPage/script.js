const open_btn = document.querySelector('.open-btn')
const close_btn = document.querySelector('.close-btn')
const nav = document.querySelectorAll('.nav')
const mainContent = document.getElementById('main-content');

open_btn.addEventListener('click', () => {
    nav.forEach(nav_el => nav_el.classList.add('visible'));
    mainContent.classList.add('menu-open');
});

close_btn.addEventListener('click', () => {
    nav.forEach(nav_el => nav_el.classList.remove('visible'));
    mainContent.classList.remove('menu-open');
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




