function message_error(obj) {
    var html = '';
    if(typeof (obj) === 'object'){
        html= '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    }
    else {
        html = '<p>'+obj+'</p>';
    }
    swal({
        type: 'error',
        title: 'Oops...',
        html: html,
        icon: 'error',
        footer: '<a href>¡Por favor verificar y correguir los errores!</a>',
        buttonsStyling: 'background-color: #000'
    });
}

function submit_with_ajax(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'supervan',
        title: title,
        icon: 'far fa-bell',
        content: content,
        columnClass: 'medium',
        typeAnimated: true,
        type: 'orange',
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "<strong>Si</strong>",
                btnClass: 'orange',
                addClass: 'color: #000',
                action: function () {
                    $.ajax({
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        if(!data.hasOwnProperty('error')){
                            callback();
                            return false;
                        }
                        message_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus+': '+errorThrown);
                    }).always(function (data) {
                    });
                }
            },
            danger: {
                text: "<strong>No</strong>",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    });

}