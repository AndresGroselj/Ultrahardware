var container = null;
var productsInCart = {};
var cartKeys = [];
var infoProducts = {};

$(document).ready(function(){
    updateProductsInCart();
    container = $("#cart-products");
    if (cartKeys.length > 0)
        getProductsInfo().then(productData => {
            infoProducts = productData;
            printProducts();
        });
    else
        printNoProductCard();
});

async function getProductsInfo(){
    rawProductsData = await Promise.allSettled(cartKeys.map(async k => {
        let response = await fetch(`http://localhost:8000/api/productcard/${k}/`);
        var jsonData = await response.json()
        return jsonData;
    }))
    cleanProductsData = rawProductsData.map(a => a.value)
    var formatedData = {};
    cleanProductsData.forEach(element => {
        var elementId = element["product_id"];
        formatedData[elementId] = element;
        formatedData[elementId]["quantity"] = productsInCart[elementId];
    });
    return formatedData;
}

function printNoProductCard(){
    emptyContainer();
    calculateTotal();
    var card = $("<div></div>");
    card.addClass("product-item card");
    card.text("No hay productos en su carrito.")

    appendCard(card);
}

function printProducts(){
    console.log("printing cards")
    emptyContainer();
    $.each(infoProducts, function(index, product){
        var card = CreateProductCard(product)
        appendCard(card);
        addEventsToCard(index);
    });
    calculateTotal();
}

function appendCard(card){
    container.append(card);
}

function emptyContainer(){
    container.empty();
}

function removeProduct(id){
    RemoveFromCart(id);
    delete infoProducts[id];
    updateProductsInCart();
    if (cartKeys.length > 0)
        printProducts();
    else
        printNoProductCard();
}

function addEventsToCard(id){
    maxQuanity = $("#product-quantity-" + id).attr("max");

    $("#removeProduct-" + id).click(function(){
        console.log(`removing product [${id}] ${infoProducts[id]["nombre"]}`);
        removeProduct(id)
    });
    $("#product-quantity-" + id).bind('keyup mouseup', function(){
        var value = parseInt($("#product-quantity-" + id).val());
        if (isNaN(value))
            return;
        if (infoProducts[id]["quantity"] == value)
            return;
        if (value > maxQuanity){
            value = maxQuanity;
            $("#product-quantity-" + id).val(maxQuanity)
        }

        updateProductQuantity(id, value);
    });
}

function calculateTotal(){
    var total = 0;
    for (i = 0; i < cartKeys.length; i++){
        var info = infoProducts[cartKeys[i]];
        total += info["Price"] * info["quantity"];
    };
    $("#total").text(formatCurrency(total));
}

function updateProductsInCart(){
    productsInCart = GetCart();
    cartKeys = Object.keys(productsInCart);
}

function updateProductQuantity(id, quantity){
    console.log(`changing quantity of [${id}] ${infoProducts[id]["nombre"]}`);
    AddToCart(id, quantity);
    updateProductsInCart();
    infoProducts[id]["quantity"] = quantity; 

    $("#product-total-" + id).text(formatCurrency(infoProducts[id]["Price"] * quantity))
    calculateTotal();
}

function CreateProductCard(product){
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

    var bottomRow = $("<div></div>");
    bottomRow.addClass("row justify-content-between");

    var basePrice = $("<div></div>");
    basePrice.addClass("col-lg-5 col-9 text-left");
    basePrice.text(formatCurrency(product["Price"]));
    if (product["HasDiscount"]){
        var descuento = $("<span> descuento</span>");
        descuento.addClass("descuento");
        basePrice.append(descuento);
    }

    var quantityContainer = $("<div></div>");
    quantityContainer.addClass("col-lg-2 col-3 quantity");
    var quantityInput = $("<input>");
    quantityInput.addClass("form-control");
    quantityInput.attr("id", "product-quantity-" + product["product_id"]);
    quantityInput.attr("type", "number");
    quantityInput.attr("value", product["quantity"]);
    quantityInput.attr("min", "1");
    quantityInput.attr("max", "20");
    quantityContainer.append(quantityInput);

    var total = $("<div></div>");
    total.addClass("col-lg-3 col-9 text-right");
    total.attr("id", "product-total-" + product["product_id"]);
    total.text(formatCurrency(product["Price"] * product["quantity"]))

    topRow.append(nombre);
    topRow.append(removeProduct);
    bottomRow.append(basePrice);
    bottomRow.append(quantityContainer);
    bottomRow.append(total);
    infoContainer.append(topRow);
    infoContainer.append(bottomRow);
    imageContainer.append(image);
    row.append(imageContainer);
    row.append(infoContainer);
    card.append(row);

    return card;
}