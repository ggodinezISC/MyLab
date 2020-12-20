function validarIdEntrevista() 
{
    var cad =document.getElementById("Identrevista").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>=1)
        resul=""
    else
    {
        resul=" *IdEntrevista No Válido ";
    } 
    return resul;

}

function validarIdPostulacion() 
{
    var cad =document.getElementById("Idpostulacion").value;
    cad=Number.parseInt(cad,10);
    resul="";
    if(cad>=1)
        resul=""
    else
    {
        resul=" *IdPostulacion No Válido ";
    } 
    return resul;

}

function validarFechaRegistro() {
    var cad = document.getElementById("fecharegistro").value;
    cad=cad.split("-");
    var f = new Date();
    resul="";
        if (cad[0]==(f.getYear()+1900) && cad[1]==(f.getMonth()+1) && cad[2]==f.getDate()) 
        { 
             resul="";
        } 
        else 
        {
             resul+=" *Fecha de Registro no válida- ";
        }
        return  resul;

}
function validarFechaEntrevista() {
    var cad = document.getElementById("fechaentrevista").value;
    cad=cad.split("-");
    var f = new Date();
    resul="";
        if (cad[0]>=(f.getYear()+1900) && cad[1]>=(f.getMonth()+1) && cad[2]>=f.getDate()) 
        { 
             resul="";
        } 
        else 
        {
             resul+=" *Fecha de Entrevista no válida- ";
        }
        return  resul;

}

function validarHoraInicio() 
{
    //la hora de inicio debe ser mayor o igual que la hora del sistema
    var cad = document.getElementById("horainicio").value;
    cad=cad.split(":");
    var f = new Date();
    resul="";
        if(cad[0]>=f.getHours() && cad[1]>f.getMinutes()) 
        { 
             resul="";
        } 
        else 
        {
             resul+=" *Hora de Inicio no válida ";
        }
        return  resul;

}

function validarHoraFin() 
{
    //la hora de fin debe ser mayor que la hora de inicio
    var cad = document.getElementById("horainicio").value;
    var cad2 = document.getElementById("horafin").value;
    cad=cad.split(":");
    cad2=cad2.split(":");
    resul="";
        if (cad2[0]>cad[0]) 
        { 
             resul="";
        } 
        else 
        {
             resul+=" *Hora de Fin no válida ";
        }
        return  resul;

}

function validarEstatus() 
{
    //la hora de fin debe ser mayor que la hora de inicio
    var cad = document.getElementById("estatus").value;
    var cad2 = document.getElementById("fechaentrevista").value;
    resul="";
    cad2=cad2.split("-");
    var f = new Date();
        if (cad2[0]>=(f.getYear()+1900) && cad2[1]>=(f.getMonth()+1) && cad2[2]>=f.getDate()) 
        {
            if (cad=="Pendiente") 
            { 
                 resul="";
            } 
            else 
            {
                 resul+=" *Estatus Inválido(Pendiente)";
            } 
        }
        else  
        {
            if (cad=="Realizada") 
            { 
                 resul="";
            } 
            else 
            {
                 resul+=" *Estatus Inválido(Realizada)";
            } 
        }
        
        return  resul;

}



function validarDatos()
{
    cad="";
    cad+=validarIdEntrevista();
    cad+=validarIdPostulacion();
    cad+=validarFechaRegistro();
    cad+=validarFechaEntrevista();
    cad+=validarHoraInicio();
    cad+=validarHoraFin();
    cad+=validarEstatus(); 
    if(cad=="")
        alert("Los datos cumplen las políticas satisfactoriamente");
    else 
        alert(cad);
    return cad;
}