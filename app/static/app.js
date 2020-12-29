function preencherBarraCarrinho() {
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
}

function limparCarrinho() {
  $("#preco_carrinho").text("");
  $("#itens_carrinho").text("0");
  $("button[id^=presentear-bt-]").removeClass("adicionado");
  localStorage.removeItem("carrinho");
}

$(document).ready(function () {
  console.log("Documento carregado.");
  console.log($("#convidados"));
  // Carregando presentes
  console.log(localStorage.getItem("carrinho"));
  if (
    localStorage.getItem("carrinho") &&
    JSON.parse(localStorage.getItem("carrinho"))
  ) {
    carrinho = JSON.parse(localStorage.getItem("carrinho"));
    carrinho.forEach((item) => {
      $(`#presentear-bt-${item.id}`).addClass("adicionado");
    });
    preencherBarraCarrinho();
  }

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

    preencherBarraCarrinho(false);
  });

  /** MODAIS */
  $("#appendix").on("click", ".close", function () {
    $("#cortina").hide();
    $(".modal").hide();
  });

  function open_modal(id) {
    $("#cortina").show();
    $(`#${id}`).show();
  }

  $("#enviar_mensagem").click(function () {
    open_modal("envio_mensagens");
  });

  $(".close_modal_mensagem").click(function () {
    $("#modal_mensagem").css("display", "none");
  });

  $("#checkout").click(function () {
    $("#modal_presente").show();
  });

  $("#pagar").click(function () {
    // Procede para pagamento
    pagar_teste();
    // Envia mensagem com alguns dados a mais do pagamento
    if (
      localStorage.getItem("carrinho") &&
      JSON.parse(localStorage.getItem("carrinho"))
    ) {
      var carrinho = JSON.parse(localStorage.getItem("carrinho"));
      var valorTotal = String(
        carrinho.reduce((acc, cur) => {
          return acc + parseFloat(cur.price);
        }, 0)
      );
      $("#input_mensagem_presente_preco").val(valorTotal);
    }
    var nome = $("#input_mensagem_presente_nome").val(),
      mensagem = $("#input_mensagem_presente_mensagem").val(),
      preco = $("#input_mensagem_presente_preco").val();
    email = "naoresponda@filipeelore.love";
    text = `
    ${
      nome || "Não identificado"
    } acabou de te mandar um presente referente ao valor de R$${preco} com a seguinte mensagem: <br/><br/>
    ${mensagem}`;

    $.post(
      "enviar_email",
      {
        nome,
        email,
        mensagem: text,
      },
      function () {
        console.log("Mensagem enviada");
      }
    );
  });

  $(".close_modal_presente").click(function () {
    $("#modal_presente").hide();
  });

  // Acionando todos os parallax scrollers
  $("[data-paroller-factor]").paroller();

  /** FORMS */
  $("#envio_mensagens").on("click", "button", function (e) {
    e.preventDefault();
    var form = $("#envio_mensagens_form");

    $.ajax({
      type: form.attr("method"),
      url: form.attr("action"),
      dataType: "html",
      data: form.serialize(),
      beforeSend: function () {
        // $('#insere_aqui').html(iconCarregando);
        console.log("carregando...");
        $("#carregando").show();
        $("#cortina_permanente").show();
      },
      complete: function () {
        $("#carregando").hide();
        $("#cortina_permanente").hide();
        $("#envio_mensagens").hide();
      },
      success: function (data, textStatus) {
        console.log("ok");
        console.log(data);
        console.log(textStatus);
        $("#sucesso_mensagem").show();
      },
      error: function (xhr, er) {
        $("#erro").show();
        console.log(
          `Error ${xhr.status} - ${xhr.statusText} \n Tipo de erro: ${er}`
        );
      },
    });
  });

  $("#relogio_contagem_regressiva").countdown("2021/03/07", function (event) {
    $(this).html(event.strftime("%D dias %H:%M:%S"));
  });

  function pagar_teste() {
    // inicia a instância do checkout
    var checkout = new PagarMeCheckout.Checkout({
      encryption_key: "ek_test_qedtchn5pAnzVpEqetVwP86Cw4FgBc",
      success: function (data) {
        console.log(data);
        $("#modal_presente").hide();
        limparCarrinho();
      },
      error: function (err) {
        console.log(err);
      },
      close: function () {
        console.log("The modal has been closed.");
      },
    });

    var carrinho, items;

    if (
      localStorage.getItem("carrinho") &&
      JSON.parse(localStorage.getItem("carrinho"))
    ) {
      carrinho = JSON.parse(localStorage.getItem("carrinho"));
      items = carrinho.reduce((acc, cur) => {
        return [
          ...acc,
          {
            id: `PRESENTE_${cur.id}`,
            title: cur.title,
            unit_price: String(
              parseInt(parseFloat(cur.price).toFixed(2) * 100)
            ),
            quantity: 1,
            tangible: "false",
          },
        ];
      }, []);
    }

    console.log(items);

    checkoutObj = {
      amount: String(
        items.reduce((acc, cur) => {
          return acc + parseInt(cur.unit_price);
        }, 0)
      ),
      customerData: "true",
      createToken: "true",
      items,
    };

    console.log(checkoutObj);
    checkout.open(checkoutObj);
  }

  /* -------------------------
  --------- GRÁFICOS ---------
  ---------------------------- */
});
