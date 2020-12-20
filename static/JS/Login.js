function validarEmail() {
    var cad = document.getElementById("inputEmail").value;
    var patron = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
    resul="";
        if (patron.test(cad)) 
        { 
             resul="";
        } 
        else 
        {
             resul+=" -EL correo no cumple el formato- ";
        }
        return  resul;

}

function validarPassword() {
    //Minimo 8 caracteres
    //Maximo 15
    //Al menos una letra mayúscula
    //Al menos una letra minucula
    //Al menos un dígito
    //No espacios en blanco
    //Al menos 1 caracter especial de estos 3: $ % &
    var cad = document.getElementById("inputPassword").value;
    var patron = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$/;
    resul="";
        if (patron.test(cad)) 
        { 
             resul="";
        } 
        else 
        {
             resul+=" -La contraseña no cumple la política- ";
        }
        return  resul;

}
function validarDatos()
{
    cad="";
    cad+=validarEmail();
    cad+=validarPassword();
    if(cad=="")
        alert("Los datos cumplen las políticas satisfactoriamente");
    else 
        alert(cad);
    return cad;
}