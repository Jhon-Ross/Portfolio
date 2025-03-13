function initMenu() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function(event) {
            navMenu.classList.toggle('active');
            event.stopPropagation(); // Impede que o clique se propague para o documento
        });

        // Recolhe o menu ao clicar fora
        document.addEventListener('click', function(event) {
            if (!navMenu.contains(event.target) && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
            }
        });

        // Recolhe o menu ao clicar em um link
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
            });
        });
    } else {
        console.error('navToggle or navMenu not found');
    }
}

document.addEventListener('DOMContentLoaded', initMenu);