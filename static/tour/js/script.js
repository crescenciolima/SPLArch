/***** def popovers ******/
$(document).ready(function() {
    // --- popover padrões relacionados
    $(".field-padroesRelacionados .col-md-3").append("<div id='popover_padrao_relacionado'></div>");
    $("#id_padroesRelacionados").change(function() {
        $("#id_padroesRelacionados option:selected").each(function() {
            titlePadraoRelacionado = $(this).text();
            padraoRelacionado = $(this).val();
        });
        $.getJSON('http://127.0.0.1:8000/api/padroes-relacionados/' + padraoRelacionado, function(resposta) {
            dados = resposta[0];
            campoPadraoRelacionado = dados.fields.aliase;
            conteudo = {
                title:  titlePadraoRelacionado,
                content: campoPadraoRelacionado,
                placement: 'bottom',
                trigger: 'manual'
            };
            $("#popover_padrao_relacionado").popover('destroy');
            $("#popover_padrao_relacionado").popover(conteudo).popover('show');
            $(".popover-title").append("<button type='button' id='close' class='close'>&times;</button>");
            $(document).on('click', '#close', function(event) {
                $("#popover_padrao_relacionado").popover('hide');
            });
            $("#close").click(function(event) {
               $("#popover_padrao_relacionado").popover('hide');
            });
        });
    });
    // next popover
});