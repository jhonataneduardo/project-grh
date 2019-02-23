function teste(id) {
    console.log(id);
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    $.ajax({
        type: 'POST',
        url: '/hours-extras/teste/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function (resul) {
            console.log(resul);
            $("#mensagem").text('foi!');
        }

    });
}
