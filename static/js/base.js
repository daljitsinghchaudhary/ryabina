Ryabina.randomString = function(length) {
    var chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz'.split('');

    if (! length) {
        length = Math.floor(Math.random() * chars.length);
    }

    var str = '';
    for (var i = 0; i < length; i++) {
        str += chars[Math.floor(Math.random() * chars.length)];
    }
    return str;
};

Ryabina.App.show_modal = function(name){
    var modal_form = bootbox.dialog({
        message: $('#'+name+'_dialog_template').text(),
        closeButton: false
    });
    modal_form.find('.masked_input_mobile').mask("+7 (999) 999-9999", {placeholder: "_"});

    if(name=='visit'){
        modal_form.on("shown.bs.modal", function() {
            var visit_time_handler = $('.bootbox #id_visit_time'),
                visit_date_handler = $('.bootbox #id_visit_date'),
                visit_date = Ryabina.App.current_date_moment.format('YYYY-MM-DD'),
                visit_time = Ryabina.App.current_date_moment.format('HH:mm'),
                minDate, minDate_moment;

            if(Ryabina.App.current_date_moment.hour()>21){
                minDate_moment = Ryabina.App.current_date_moment.clone();
                minDate = minDate_moment.add(1, 'day');
                visit_date = minDate.format('YYYY-MM-DD');
                visit_time = '09:00';
            }
            visit_date_handler.val(visit_date);
            visit_time_handler.val(visit_time);

            visit_time_handler.datetimepicker({
                format: 'HH:mm',
                disabledTimeIntervals: [[moment({ h: 0 }), moment({ h: 9 })], [moment({ h: 21 }), moment({ h: 24 })]]
            });

            visit_date_handler.datetimepicker({
                format: 'YYYY-MM-DD',
                locale: 'ru',
                minDate: minDate,
                viewMode: 'months'
            });
        });
    }
};

$(document).ready(function(){
    Ryabina.App.current_date_moment = moment(Ryabina.App.current_date, 'DD.MM.YYYY HH:mm');
    setInterval(function(){
        Ryabina.App.current_date_moment.add(1, 's');
    }, 1000);

    $('a.btn[data-target=#modalCallback]').click(function(e){
        Ryabina.App.show_modal('callback');
        e.preventDefault();
    });
    $('a.btn[data-target=#modalQuestion]').click(function(e){
        Ryabina.App.show_modal('question');
        e.preventDefault();
    });
    $('a.btn[data-target=#modalVisit]').click(function(e){
        Ryabina.App.show_modal('visit');
        e.preventDefault();
    });
    if ($('.masked_input_mobile').length) {
        $('.masked_input_mobile').mask("+7 (999) 999-9999", {placeholder: "_"});
    }

    $(document).on('click', 'img.captcha', function(){
          var self=$(this);
        $.getJSON('/captcha/refresh/?'+Ryabina.randomString(5), {}, function(json) {
            self.attr('src', json['image_url']);
            self.parent().parent().parent().find('input[name=captcha_0]').val(json['key']);
        });
    });

    $(document).on('click', '.bootbox button.submit', function(){
        var self = $(this),
            form = self.parent().parent();
        $.ajax(form.attr('action'),{
            dataType: 'json',
            data: form.serialize(),
            method: 'POST'
        }).always(function(){
            bootbox.hideAll();
        }).done(function(data){
            if(data['success_message']){
                var success_template = _.template($('#success_dialog_template').text()),
                    success_dialog = bootbox.dialog({
                        message: success_template(data),
                        closeButton: false
                    });
                var timeout = window.setTimeout(function(){
                    window.clearInterval(timeout);
                    success_dialog.modal('hide');
                }, 3000);
            }
        }).fail(function(){
            console.log('error');
        });
    });

    if(Ryabina.App.messages&&Ryabina.App.messages.length){
        var success_template = _.template($('#success_dialog_template').text()),
            success_dialog = bootbox.dialog({
                message: success_template({'success_message': Ryabina.App.messages.join('<br>')}),
                closeButton: false
            });
        var timeout = window.setTimeout(function(){
            window.clearInterval(timeout);
            success_dialog.modal('hide');
        }, 3000);
    }
    if(!Ryabina.debug){
        setInterval(function(){
            if(console&&console.clear&&console.log){
                console.clear();
                console.log('%c♥ Рябина', "color: #E1085D; font-size: 30px; font-weight:bold; font-family:Arial;");
                console.log('твоя стоматология');
            }
        }, 2000);
    }
});