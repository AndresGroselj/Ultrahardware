$( document ).ready(function() {
    UpdateNavCart();
});

function GetCart(){
    var cart_list = Cookies.get('cart');
    if (cart_list == undefined)
        cart_list = {};
    else
        cart_list = JSON.parse(cart_list);
    
    return cart_list;
}

function AddToCart(product_id, ammount){
    var cart_list = GetCart();

    cart_list[product_id] = ammount;
    Cookies.set('cart', JSON.stringify(cart_list), {"SameSite":"lax"});
    console.log((Cookies.get('cart')));

    UpdateNavCart();
}

function RemoveFromCart(product_id){
    var cart_list = GetCart();
    
    delete cart_list[product_id];
    Cookies.set('cart', JSON.stringify(cart_list), {"SameSite":"lax"});
    console.log((Cookies.get('cart')));

    UpdateNavCart();
}

function UpdateNavCart(){
    var cart_list = GetCart();

    document.getElementById("cart-number").innerHTML = Object.keys(cart_list).length;
}