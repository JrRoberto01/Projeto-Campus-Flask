const menuItem = document.getElementById('menu-item');
const hamburg = document.getElementById('hamburg-icone');

function mostrarMenu(){
    if (menuItem.style.display === 'block'){
        menuItem.style.display = 'none';
        menuItem.style.transition = '0.5s';
    }else{
        menuItem.style.display = 'block';
        menuItem.style.transition = '0.5s';
    }
}