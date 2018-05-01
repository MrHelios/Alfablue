estado_borrar = false;
estado_guardar = false;
$('#nota-borrar').hide();
viejo = $('#contenido-nota').val();

$('#nota-borrar-btn').click(function() {
    if(!estado_borrar)
    {
        $('#nota-editar').hide();
        $('#nota-borrar').show();
        estado_borrar = true;
    }
    else
    {
        $('#nota-editar').show();
        $('#nota-borrar').hide();
        estado_borrar = false;
    }
});

function detectarCambio() {
    actual = $('#contenido-nota').val();
    if(viejo == actual) {
        viejo = actual;
    }
    else {
        $('#titulo-editar').attr('id','titulo-editar-singuardado');
        estado_guardar = true;
    }
};

$("#btn-notaBorrar").click(function() {
    estado_guardar=false
    $.ajax({
        method: 'post',
        url: URL_BORRAR,
        contentType: 'application/json',
        data: {nota_id: NOTA_ID}
    }).done(function(){
        window.location.replace(URL_HOLA);
    });
});

function guardar() {
    if(estado_guardar = true) {
        t = document.getElementById("titulo-nota").value
        c = document.getElementById("contenido-nota").value
        $.ajax({
            method: 'POST',
            url: "",
            contentType: 'application/json',
            data: {titulo: t, contenido: c}
        }).done(function(){
            $('#titulo-editar-singuardado').attr('id','titulo-editar');
            viejo = $('#contenido-nota').val();
            estado_guardar = false;
        });
    }
};

setInterval(guardar, 15000);
setInterval(detectarCambio, 2000);
