function validarNombreCompleto() 
{
    var cad =document.getElementById("nombre").value;
    var patron = /^[a-zA-Z]+[a-zA-Z]/;
    resul="";
    if(cad.includes("0",0) || cad.includes("1",0) || cad.includes("2",0) || cad.includes("3",0) ||cad.includes("4",0) ||cad.includes("5",0) ||cad.includes("6",0) || cad.includes("7",0) ||cad.includes("8",0) ||cad.includes("9",0) )
        resul=" El nombre contiene numeros"
    else if (patron.test(cad)) 
    {
        resul+="";
    }
    else
    {
        resul+="Nombre no cumple el formato";
    } 
    return resul;

}
function validarUsuario() 
{
    var cad =document.getElementById("idusuario").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>=1)
        resul=""
    else
    {
        resul=" IdUsuario No Valido ";
    } 
    return resul;

}


function validarTelefono() {
    var cad = document.getElementById("telefono").value;
    var patron = /^\d{3}-\d{3}-\d{4}/;
    resul="";
        if (patron.test(cad)) 
        { 
             resul="";
        } 
        else 
        {
             resul+=" -EL numero escrito no cumple con el patron DDD-DDD-DDDD ";
        }
        return  resul;
    } 
    




function validarEmail() {
    var cad = document.getElementById("email").value;
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
    var cad = document.getElementById("psw").value;
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
function validarSexo() {
    var cad = document.getElementById("sexo").value;
    resul="";
    cad=cad.toUpperCase()
        if (cad=="H" | cad=="M")
        { 
             resul="";
        } 
        else 
        {
             resul+=" -Elige un sexo válido- ";
        }
        return  resul;

}
function validarFechaNacimiento() {
    var cad = document.getElementById("fechaNacimiento").value;
    cad=cad.split("-");
    cad=cad[0];
    resul="";
        if (cad<=2010) 
        { 
             resul="";
        } 
        else 
        {
             resul+=" -Fecha de Nacimiento no válida- ";
        }
        return  resul;

}
function validarDatos()
{
    cad="";
    cad+=validarUsuario();
    cad+=validarNombreCompleto();
    cad+=validarTelefono();
    cad+=validarEmail();
    cad+=validarPassword();
    cad+=validarSexo();
    cad+=validarFechaNacimiento();
    if(cad=="")
        alert("Los datos cumplen las políticas satisfactoriamente");
    else 
        alert(cad);
    return cad;
}