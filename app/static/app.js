$(document).ready(function () {
  console.log("Documento carregado.");
  console.log($("#convidados"));
  $("#convidados").DataTable({
    pageLength: 50,
  });

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

  $("#mais_informacoes_convidados_bt").click(function () {
    if ($("#mais_informacoes_convidados_div").css("display") === "none") {
      $("#mais_informacoes_convidados_div").css("display", "block");
    } else {
      $("#mais_informacoes_convidados_div").css("display", "none");
    }
  });

  $(".presentear-bt").click(function (e) {
    let id = $(this).data("presente-id"),
      title = $(this).data("title"),
      price = $(this).data("price");

    if (!$(this).hasClass("adicionado")) {
      if (!localStorage.getItem("carrinho")) {
        localStorage.setItem(
          "carrinho",
          JSON.stringify([
            {
              id,
              title,
              price,
            },
          ])
        );
      } else {
        let itens = JSON.parse(localStorage.getItem("carrinho")),
          itensIds = itens.reduce((acc, cur) => {
            return [...acc, cur.id];
          }, []);

        if (!itensIds.includes(id)) {
          localStorage.setItem(
            "carrinho",
            JSON.stringify([
              ...itens,
              {
                id,
                title,
                price,
              },
            ])
          );
        }
      }

      $(this).text("Adicionado");
      $(this).addClass("adicionado");
    } else {
      localStorage.setItem(
        "carrinho",
        JSON.stringify(
          JSON.parse(localStorage.getItem("carrinho")).filter(
            (item) => item.id !== id
          )
        )
      );

      $(this).text("Presentear");
      $(this).removeClass("adicionado");
    }

    $("#itens_carrinho").text(
      JSON.parse(localStorage.getItem("carrinho")).length
    );
    $("#preco_carrinho").text(
      `R$ ${parseFloat(
        JSON.parse(localStorage.getItem("carrinho")).reduce(
          (acc, cur) => acc + parseFloat(cur.price),
          0
        )
      ).toFixed(2)}`
    );
  });

  $("#enviar_mensagem").click(function () {
    $("#modal_mensagem").css("display", "block");
  });

  $(".close_modal_mensagem").click(function () {
    $("#modal_mensagem").css("display", "none");
  });

  $("#checkout").click(function () {
    $("#modal_presente").show();
    pagar_teste()
  });

  $(".close_modal_presente").click(function () {
    $("#modal_presente").hide();
  });

  $("[data-paroller-factor]").paroller();

  function pagar() {
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
  }

  function pagar_teste() {
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
      amount: "12000",
      customerData: "true",
      createToken: "true",
      items: [
        {
          id: "PRESENTE_01",
          title: `Valor de Presente`,
          unit_price: "6000",
          quantity: 2,
          tangible: "false",
        },
      ],
    });
  }

  /* -------------------------
  --------- GRÁFICOS ---------
  ---------------------------- */
});
