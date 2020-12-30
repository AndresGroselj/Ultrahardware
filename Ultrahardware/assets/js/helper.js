function formatCurrency(ammout){
    var ammountArray = ammout.toString().split('').reverse();
    var formatted = "";
    for (i = 0; i < ammountArray.length; i++){
        if (i%3 == 0 && i != 0)
            formatted = "." + formatted;
        formatted = ammountArray[i] + formatted;
    };
    formatted = "$" + formatted;
    return formatted;
}