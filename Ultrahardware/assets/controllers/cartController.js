var container = null;
var infoProducts = {};

$(document).ready(function(){
    container = $("#cart-products");
    getProducts();
    PrintProducts();
});

function getProducts(){
    emptyContainer();
    var productsInCart = GetCart();
    console.log(productsInCart);
    $.each(productsInCart, function(productId, quantity){
        //console.log(`${productId} ${quantity}`);
        $.get({
            url: `/api/productcard/${productId}/`,
            dataType: 'json',
            success: function(response){
                //console.log(response);
                infoProducts[response["product_id"]] = response; 
                infoProducts[response["product_id"]]["quantity"] = quantity;
            },
            error: function(error){
                console.error("Error en el servicio de listar productos del carrito");
                console.error(error);
            }
        });
    });
}

function PrintProducts(){
    $.each(infoProducts, function(index, product){
        var card = CreateProductCard(product)
        appendCard(card);
    });
}

function CreateProductCard(product){
    /*
    <div class="product-item card">
            <input type="hidden" value="1" id="productid" name="productid">
            <div class="card-block">
                <div class="row">
                    <div class="col-lg-2 col-3">
                        <img src="https://www.pcfactory.cl/public/foto/38367/1_500.jpg?t=1597845348" alt="telefono-samsung" class="product-image">
                    </div>
                    <div class="col-lg-10 col-9">
                        <div class="row">
                            <div class="col-lg-6 col-10 mr-auto">Telefono Samsung</div>
                            <img src="/static/img/red_trashcan.png" alt="X" class="removeButton">
                        </div>
                        <div class="row justify-content-between">
                            <div class="col-lg-5 col-9 text-left"><span>$500.000</span> <span class="descuento">descuento</span></div>
                            <div class="col-lg-2 col-3 ammount">
                                <input type="number" class="form-control" value="2" max="20" min="1">
                            </div>
                            <div class="col-lg-3 col-9 text-right">$1.000.000</div>
                        </div>
                    </div> 
                </div>
            </div>
        </div>
    */

    var card = $("<div></div>");
    card.addClass("product-item card");
    card.text(product["nombre"]);

    return card;
}

function appendCard(card){
    container.append(card);
}

function emptyContainer(){
    //container.empty();
}

function removeProduct(id){
    RemoveFromCart(id);
    PrintProducts()
}