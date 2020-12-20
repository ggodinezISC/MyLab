

function validarIdCarrera() 
{
    var cad =document.getElementById("idcarrera").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>=1)
        resul=""
    else
    {
        resul=" *IdCarrera No Válido ";
    } 
    return resul;

}
function validarIdUsuario() 
{
    var cad =document.getElementById("idusuario").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>=1)
        resul=""
    else
    {
        resul=" *IdUsuario No Válido ";
    } 
    return resul;

}
function validarNoControl() 
{
    var cad =document.getElementById("nocontrol").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>=1)
        resul=""
    else
    {
        resul=" *NoControl No Válido ";
    } 
    return resul;

}


function validarPromedio() 
{
    var cad =document.getElementById("promedio").value;
    var patron = /^[0-9]{2,3}/;
    resul="";
    if (patron.test(cad)) 
    {
        resul+="";
    }
    else
    {
        resul+=" *Promedio no cumple el formato (DDD) ";
    } 
    return resul;

}

function validarAnioEgreso() 
{
    var cad =document.getElementById("egreso").value;
    var patron = /^[0-9]{4}/;
    resul="";
    if (patron.test(cad)) 
    {
        resul+="";
    }
    else
    {
        resul+=" *Año de egreso no cumple el formato DDDD ";
    } 
    return resul;

}

function validarCurriculum() 
{
    var cad =document.getElementById("curriculum").value;
    resul="";
    if (cad=="") 
    {
        resul+=" *Curriculum no válido ";
    }
    else
    {
        resul="";
    } 
    return resul;

}


function validarDatos()
{
    cad="";
    cad+=validarNoControl();
    cad+=validarIdUsuario();
    cad+=validarIdCarrera();
    cad+=validarPromedio();
    cad+=validarAnioEgreso();
    cad+=validarCurriculum();
    if(cad=="")
        alert("Los datos cumplen las políticas satisfactoriamente");
    else 
        alert(cad);
    return cad;
}