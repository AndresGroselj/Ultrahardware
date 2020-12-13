$(document).ready(function(){
    PrintProducts();
});

function PrintProducts(){
    var container = $("#cart-products");
    var productsInCart = GetCart();
    console.log(productsInCart);
    $.each(productsInCart, function(productId, quantity){
        console.log(`${productId} ${quantity}`);
        $.get({
            url: `/api/productcard/${productId}/`,
            dataType: 'json',
            success: function(response){
                var card = CreateProductCard(response, quantity);
                appendCard(card, container);
            },
            error: function(error){
                console.error("Error en el servicio de listar productos del carrito");
                console.error(error);
            }
        });
    });
}

function CreateProductCard(product, quantity){
    /*
    <div class="product-item card">
        <input type="hidden" value="1" id="productid" name="productid">
        <div class="card-block">
        <div class="row">
            <div class="col-lg-1 col-2">
                <img src="https://www.pcfactory.cl/public/foto/38367/1_500.jpg?t=1597845348" alt="telefono-samsung" class="product-image">
            </div>
            <div class="col-lg-6 col-10 text-center">Telefono Samsung</div>
            <div class="col-lg-2 col-3 ammount">
                <input type="number" class="form-control" value="2" max="20" min="1">
            </div>
            <div class="col-lg-3 col-9 text-right">$1.000.000</div>
        </div>
        </div>
    </div>
    */

    var card = $("<div></div>");
    card.addClass("product-item card");
    card.text(product["nombre"]);

    return card;
}

function appendCard(card, container){
    container.append(card);
}