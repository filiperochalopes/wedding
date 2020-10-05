$(document).ready(function () {
  $("#convidados").DataTable();

  $(".teste_alerta").on("click", function (e) {
    console.log(e);
    alert("Hello world!");
  });

  $("#toogle_menu").click(function (e) {
    console.log($(this));
    if ($("nav").css("display") === "none") {
      $("nav").css("display", "block");
    } else {
      $("nav").css("display", "none");
    }
  });
});
