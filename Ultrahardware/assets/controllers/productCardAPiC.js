var productLik = "/product/"

$(document).ready(function(){
    GetProductList();
});

function GetProductList(){
    $.get({
        url: "/api/productcard/",
        dataType: 'json',
        success: function(response){
            var productList = response["results"]
            console.log(productList)
            AppendProductCards(productList);
            AppendProductPreview(productList);
        },
        error: function(error){
            console.error("Error en el servicio de listar productos");
            console.error(error);
        }
    });
}

//#region cards
function AppendProductCards(products){
    var cardContainer = $("#cardGallery");
    cardContainer.empty();

    $.each(products, function(i, product){
        console.log(product);
        var card = GenerateCard(product)
        cardContainer.append(card);
    });

    AppendDummys(cardContainer);
}

function GenerateCard(product){
    var hyperlink = $("<a></a>");
    hyperlink.addClass("product-space col-xl-3 col-md-4 col-sm-6 col-6")
    hyperlink.attr("href", `javascript:displayPreview(${product['product_id']})`)

    var card = $("<div></div>");
    card.addClass("card browse-result");

    var img = $("<img>");
    img.addClass("card-img-top");
    img.attr("src", product['imagen_principal']);
    img.attr("alt", product['nombre']);

    var cardBody = $("<div></div>");
    cardBody.addClass("card-body");

    var nombre = $("<h5></h5>");
    nombre.text(product['nombre']);

    var price = $("<h6></h6>");
    price.text(product['Price']);

    if (product['HasDiscount']){
        var discount = $("<div></div>");
        discount.addClass("discount");
        var originalPrice = $("<span></span>"); //contenedor prcio original para usar en css
        originalPrice.text(product['PriceBeforeDiscount']);
        discount.append(originalPrice);
        //% descuento
        discount.append(` ${product['Dicount']}%`);
    }

    cardBody.append(nombre);
    if (product['HasDiscount']) cardBody.append(discount);
    cardBody.append(price);

    card.append(img);
    card.append(cardBody);
    
    hyperlink.append(card);
    
    return hyperlink;
}

function AppendDummys(container){
    var dummy = "<div class='browse-dummy col-xl-3 col-md-4 col-sm-6 col-6'>&nbsp;</div>";
    for (i = 0; i < 3; i++) {
        container.append(dummy);
      } 
}

//#endregion

//#region previews
function AppendProductPreview(products){
    var previewContainer = $("#product-preview-products");
    previewContainer.empty();

    $.each(products, function(i, product){
        var preview = GeneratePreview(product)
        previewContainer.append(preview);
    });

    AppendDummys(cardContainer);
}
function GeneratePreview(product){

    var preview = $("<div></div>");
    preview.addClass("d-block");
    preview.attr("slot", product["product_id"]);

    var XButton = $("<a href='javascript:hidePreview()' class='float-right'>X</a>");

    var title = $("<h4></hh4>");
    title.text(product["nombre"]);

    var Hyperlink = $("<a></a>");
    Hyperlink.attr("href", `${productLik}${product["product_id"]}/`);

    var productImg = $("<img>");
    productImg.addClass("preview-image");
    productImg.attr("src", product['imagen_principal']);
    productImg.attr("alt", product['nombre']);

    var productFooter = $("<div></div>")
    productFooter.addClass("row align-self-end container");

    var description = $("<p></p>");
    description.addClass("col-lg-9 col-12");
    description.append(product["CleanDescription"]);
    
    var priceContainer = $("<div></div>");
    priceContainer.addClass("col-lg-12 col-6");

    if (product['HasDiscount']){
        var discount = $("<div></div>");
        discount.addClass("discount");
        var originalPrice = $("<span></span>"); //contenedor prcio original para usar en css
        originalPrice.text(product['PriceBeforeDiscount']);
        discount.append(originalPrice);
        //% descuento
        discount.append(` ${product['Dicount']}%`);
    }

    var price = $("<span></span>")
    price.text(product["Price"])
    
    var button = $("<button></button>");
    button.addClass("btn btn-success col-lg-12 col-6");
    button.attr("onclick", `AddToCart('${product.product_id}', 1)`)

    var previewImg = $("<img>")
    previewImg.attr("src", "/static/img/cart.png")
    previewImg.attr("alt", "add to cart")

    button.append(previewImg);
    if (product['HasDiscount']) priceContainer.append(discount);
    priceContainer.append(price);
    productFooter.append(description);
    productFooter.append(priceContainer);
    productFooter.append(button);
    Hyperlink.append(productImg);
    preview.append(XButton);
    preview.append(title);
    preview.append(Hyperlink);
    preview.append(productFooter);

    return preview;
}
//#endregion
