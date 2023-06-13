<?php

function validar_campo($campo)
{
    $campo = trim($campo);
    $campo = stripslashes($campo);
    $campo = htmlspecialchars($campo);
    return $campo;
}

if(isset($_POST["name"]) && !empty($_POST["name"]) &&
isset($_POST["email"]) && !empty($_POST["email"]) &&
isset($_POST["message"]) && !empty($_POST["message"]))
{
    $destinoMail = "contacto@sundarasaludybelleza.com.mx";
    $name  = validar_campo($_POST["name"]);
    $email = validar_campo($_POST["email"]);
    $message = validar_campo($_POST["message"]);
    
    $contenido = "Nombre: " . $name;
    $contenido .= "\n Email: " . $email;
    $contenido .= "\n Mensaje: " . $message;
    
    mail($destinoMail, "Mensaje de contacto del cliente" . $name,$contenido);

    return print("ok");
}
return print("error");
