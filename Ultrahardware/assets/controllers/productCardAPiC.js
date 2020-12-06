$(document).ready(function(){
    GetProductList();
});

function GetProductList(){
    $.get({
        url: "/api/productcard/3/",
        dataType: 'json',
        success: function(productList){
            var jsonlist = $.parseJSON(JSON.stringify(productList));
            console.log(jsonlist);
        },
        error: function(error){
            console.error("Error en el servicio de listar productos");
            console.error(error);
        }
    });
}