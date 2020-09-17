var product_preview = null;
$( document ).ready(function() {
    product_preview = document.getElementById("product-preview") 
    $( "#product-preview-background" ).click(function() {
        hidePreview();
    });
});

function displayPreview(){
    product_preview.classList.remove("d-none")
    product_preview.classList.add("d-block")
}

function hidePreview(){
    product_preview.classList.remove("d-block")
    product_preview.classList.add("d-none")
}