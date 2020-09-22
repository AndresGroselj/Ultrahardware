$( document ).ready(function() {
    $("#contactForm").validate({
        rules: {
            inputNombre: "required",
            inputApellido: "required",
            inputEmail: {
                required: true,
                email: true
            },
            inputAsunto: "required",
            inputMensaje: "required",
        },
        messages: {
            inputNombre:{
                required: "Debe ingresar su nombre"
            },
            inputApellido:{
                required: "Debe ingresar su apellido"
            },
            inputEmail:{
                required: "Debe ingresar su email",
                email: "El email debe ser valido"
            },
            inputAsunto:{
                required: "Debe ingresar un asunto"
            },
            inputMensaje:{
                required: "Debe escribir un mensaje"
            },
        }
    })
});