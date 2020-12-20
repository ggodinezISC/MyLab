function validarNombreOferta() 
{
    var cad =document.getElementById("nombreOferta").value;
    var patron = /^[a-zA-Z]+[a-zA-Z]/;
    resul="";
    if(cad.includes("0",0) || cad.includes("1",0) || cad.includes("2",0) || cad.includes("3",0) ||cad.includes("4",0) ||cad.includes("5",0) ||cad.includes("6",0) || cad.includes("7",0) ||cad.includes("8",0) ||cad.includes("9",0) )
        resul=" *El nombre de la oferta contiene numeros"
    else if (patron.test(cad)) 
    {
        resul+="";
    }
    else
    {
        resul+=" *Nombre no cumple el formato solo letras";
    } 
    return resul;

}

function validarDescripcion() 
{
    var cad =document.getElementById("descripcion").value;
    var patron = /^[a-zA-Z]+[a-zA-Z]/;
    resul="";
    if (patron.test(cad)) 
    {
        resul+="";
    }
    else
    {
        resul+=" *Descripcion Inválida";
    } 
    return resul;

}

function validarIdOferta() 
{
    var cad =document.getElementById("Idoferta").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>0)
        resul=""
    else
    {
        resul=" *IdOferta No Válido ";
    } 
    return resul;

}

function validarIdEmpresa() 
{
    var cad =document.getElementById("idempresa").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>0)
        resul=""
    else
    {
        resul=" *IdEmpresa No Válido ";
    } 
    return resul;

}

function validarIdReclutador() 
{
    var cad =document.getElementById("Idreclutador").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>0)
        resul=""
    else
    {
        resul=" *IdReclutador No Válido ";
    } 
    return resul;

}

function validarIdCategoria() 
{
    var cad =document.getElementById("Idcategoria").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>0)
        resul=""
    else
    {
        resul=" *IdCategoria No Válido ";
    } 
    return resul;

}

function validarIdTipoContratacion() 
{
    var cad =document.getElementById("IdTContratacion").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>0)
        resul=""
    else
    {
        resul=" *IdTipoContratación No Válido ";
    } 
    return resul;

}

function validarFechaPublicacion() {
    var cad = document.getElementById("fechapublicacion").value;
    cad=cad.split("-");
    var f = new Date();
    resul="";
        if (cad[0]==(f.getYear()+1900) && cad[1]==(f.getMonth()+1) && cad[2]==f.getDate())
        { 
             resul="";
        } 
        else 
        {
             resul+=" *Fecha de Publicación no válida- ";
        }
        return  resul;
}

function validarSalario() {
    var cad = document.getElementById("salario").value;
    cad=Number.parseInt(cad,10);
    resul="";
        if (cad>0) 
        { 
             resul="";
        } 
        else 
        {
             resul+=" *Salario no válido ";
        }
        return  resul;

}

function validarCantidadVacantes() {
    var cad = document.getElementById("cantidadVacantes").value;
    cad=Number.parseInt(cad,10);
    resul="";
        if (cad>0) 
        { 
             resul="";
        } 
        else 
        {
             resul+=" *Cantidad Vacantes no válida ";
        }
        return  resul;

}

function validarEstatus() 
{
    //la hora de fin debe ser mayor que la hora de inicio
    var cad = document.getElementById("estatus").value;
    var cad2 = document.getElementById("fechapublicacion").value;
    resul="";
    cad2=cad2.split("-");
    var f = new Date();
        if (cad2[0]==(f.getYear()+1900) && cad2[1]==(f.getMonth()+1) && cad2[2]==f.getDate()) 
        {
            if (cad=="Activa") 
            { 
                 resul="";
            } 
            else
                resul=" *Estatus Inválido";
            
        }
        else  
        {
            if (cad=="Inactiva") 
            { 
                 resul="";
            } 
            else 
            {
                 resul+=" *Estatus Inválido";
            } 
        }
        
        return  resul;

}




function validarDatos()
{
    cad="";
    cad+=validarIdOferta();
    cad+=validarIdEmpresa();
    cad+=validarIdReclutador();
    cad+=validarIdCategoria();
    cad+=validarIdTipoContratacion();
    cad+=validarFechaPublicacion();
    cad+=validarSalario();
    cad+=validarCantidadVacantes();
    cad+=validarEstatus();
    cad+=validarNombreOferta();
    cad+=validarDescripcion();
    if(cad=="")
        alert("Los datos cumplen las políticas satisfactoriamente");
    else 
        alert(cad);
    return cad;
}