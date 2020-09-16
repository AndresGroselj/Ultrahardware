$( document ).ready(function() {
    var navHeight = document.getElementById("nav").offsetHeight;
    var sidebarMinHeight = 100 - (navHeight * (100 / document.documentElement.clientHeight));
    document.getElementById("categorias").style.minHeight = sidebarMinHeight + "vh";
});