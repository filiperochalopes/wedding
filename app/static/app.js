$(document).ready( function () {
    $('#convidados').DataTable();

    $('.teste_alerta').on("click", function (e){
        console.log(e)
        alert("Heelo world!")
    })
} );