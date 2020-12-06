$(document).ready(function(){
    GetProductList();
});

function GetProductList(){
    $.get({
        url: "/api/productcard/",
        dataType: 'json',
        success: function(productList){
            var jsonlist = $.parseJSON(JSON.stringify(productList));
            AppendProductCards(productList["results"]);
        },
        error: function(error){
            console.error("Error en el servicio de listar productos");
            console.error(error);
        }
    });
}

function AppendProductCards(products){
    console.log(products);
    var cardContainer = $("#cardGallery");
    //cardContainer.empty();

    $.each(products, function(i, product){
        console.log(product);
        var card = GenerateCard(product)

        cardContainer.append(card);
    });

    AppendDummys(cardContainer);
}

function GenerateCard(product){

    /*
    <a href="javascript:displayPreview(9)" class="product-space col-xl-3 col-md-4 col-sm-6 col-6">
        <div class="card browse-result">
            <img src="/media/1_511.jpg" class="card-img-top" alt="Huawei p40 Black">
            <div class="card-body">
                <h5 class="card-title">Huawei p40 Black</h5>
                
                    <div class="discount"><span>$399,990</span> 25%</div>
                
                <h6>$299,992</h6>
            </div>
        </div>
    </a>
    */
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