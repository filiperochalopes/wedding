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

  $(".presentear-bt").click(function (e) {
    // inicia a instância do checkout
    var checkout = new PagarMeCheckout.Checkout({
      encryption_key: "ek_test_qedtchn5pAnzVpEqetVwP86Cw4FgBc",
      success: function (data) {
        console.log(data);
      },
      error: function (err) {
        console.log(err);
      },
      close: function () {
        console.log("The modal has been closed.");
      },
    });

    console.log(parseFloat($(this).data("price")).toString());

    checkout.open({
      amount: parseFloat($(this).data("price")).toString() + "00",
      customerData: "true",
      createToken: "true",
      items: [
        {
          title: `Valor de ${$(this).data("title")}`,
          unit_price: $(this).data("price"),
          quantity: 1,
          tangible: "false",
        },
      ],
    });
  });
});
