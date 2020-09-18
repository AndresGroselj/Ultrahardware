$( document ).ready(function() {
    var navHeight = document.getElementById("nav").offsetHeight;
    var sidebarMinHeight = 100 - (navHeight * (100 / document.documentElement.clientHeight));
    //document.getElementById("categorias").style.minHeight = sidebarMinHeight + "vh";

    var style = document.createElement('style');
    style.innerHTML = (
        "@media (min-width: 992px){" +
        "#categorias{"               +
            "min-height: {0}vh;"     +
        "}}").f(sidebarMinHeight);

    document.head.append(style);
});

String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};