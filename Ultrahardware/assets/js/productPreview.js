var product_preview = null;
$( document ).ready(function() {
    product_preview = document.getElementById("product-preview") 
    $( "#product-preview-background" ).click(function() {
        hidePreview();
    });
});

function displayPreview(img_id){

    $('#product-preview-images').children('img').each(function () {
        this.classList.remove("d-block");
        this.classList.add("d-none");
        if (this.getAttribute("for") == img_id){
            this.classList.remove("d-none");
            this.classList.add("d-block");
        }
    });

    product_preview.classList.remove("d-none")
    product_preview.classList.add("d-block")
}

function hidePreview(){
    product_preview.classList.remove("d-block")
    product_preview.classList.add("d-none")
}