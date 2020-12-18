var container = null;
var productsInCart = {};
var keys = [];
var infoProducts = {};

$(document).ready(function(){
    productsInCart = GetCart();
    keys = Object.keys(productsInCart);
    container = $("#cart-products");
    getProductsInfo();
});

function getProductsInfo(){
    console.log(productsInCart);
    $.each(productsInCart, function(productId, quantity){
        //console.log(`${productId} ${quantity}`);
        $.get({
            url: `/api/productcard/${productId}/`,
            dataType: 'json',
            success: function(response){
                infoProducts[response["product_id"]] = response; 
                infoProducts[response["product_id"]]["quantity"] = quantity;
                
                tryPrinting();
            },
            error: function(error){
                console.error("Error en el servicio de listar productos del carrito");
                console.error(error);
            }
        });
    });
}

function printProducts(){
    console.log("printing cards")
    emptyContainer();
    $.each(infoProducts, function(index, product){
        var card = CreateProductCard(product)
        appendCard(card);
    });
}

function CreateProductCard(product){
    /*
    <div class="product-item card" id="product-1">
        <div class="row">
            <div class="col-lg-2 col-3">
                <img src="https://www.pcfactory.cl/public/foto/38367/1_500.jpg?t=1597845348" alt="telefono-samsung" class="product-image">
            </div>
            <div class="col-lg-10 col-9">
                <div class="row">
                    <div class="col-11 mr-auto nombre-producto"> Samsung® Smartphone Galaxy A10s Octa Core 32GB 6.2" 4G Android Negro Movistar QR </div>
                    <img src="/static/img/red_trashcan.png" alt="X" class="removeProduct" id="removeProduct-1">
                </div>
                <div class="row justify-content-between">
                    <div class="col-lg-5 col-9 text-left"><span>$500.000</span> <span class="descuento">descuento</span></div>
                    <div class="col-lg-2 col-3 ammount">
                        <input type="number" class="form-control" value="2" max="20" min="1" id="product-quantity-1">
                    </div>
                    <div class="col-lg-3 col-9 text-right" id="product-total-1">$1.000.000</div>
                </div>
            </div> 
        </div>
    </div>
    */

    var card = $("<div></div>");
    card.addClass("product-item card");

    var row = $("<div></div>");
    row.addClass("row");

    var imageContainer = $("<div></div>");
    imageContainer.addClass("col-lg-2 col-3");

    var image = $("<img></img>");
    image.addClass("product-image");
    image.attr("src", product["imagen_principal"]);

    var infoContainer = $("<div></div>");
    infoContainer.addClass("col-lg-10 col-9");

    var topRow = $("<div></div>");
    topRow.addClass("row");

    var nombre = $("<div></div>");
    nombre.addClass("col-11 mr-auto");
    nombre.text(product["nombre"]);

    var removeProduct = $("<img></img>");
    removeProduct.addClass("removeProduct")
    removeProduct.attr("src", "/static/img/red_trashcan.png");
    removeProduct.attr("alt", "X");
    removeProduct.attr("id", "removeProduct-" + product["product_id"]);


    topRow.append(nombre);
    topRow.append(removeProduct);
    infoContainer.append(topRow);
    //infoContainer.append(bottomRow);
    imageContainer.append(image);
    row.append(imageContainer);
    row.append(infoContainer);
    card.append(row);

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
    printProducts()
}

// checkea que ya se tenga toda la informacion de los productos y si es asi, los imprime
function tryPrinting(){ 
    var hasAll = true;
    for (i = 0; i < keys.length; i++){
        if(!infoProducts.hasOwnProperty(keys[i])){
            hasAll = false;
            break;
        };
    };
    if (hasAll){
        printProducts();
    };
}