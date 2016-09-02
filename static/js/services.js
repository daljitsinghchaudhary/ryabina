Ryabina.App.photoMessageCenter = function(){
    var photo_container_handler = $('#photo_container'),
        photo_handler = photo_container_handler.find('div.photo'),
        photo_message = photo_handler.find('div.change_photo'),
        top = photo_handler.height()/2 - photo_message.height()/2,
        left = photo_handler.width()/2 - photo_message.width()/2;

    photo_message.css('top', top+'px').css('left', left+'px');
};


Ryabina.App.photoDeleteSuccess = function(data){
    var photo_container_handler = $('#photo_container'),
        photo_handler = photo_container_handler.find('div.photo'),
        delete_handler = photo_container_handler.find('div.delete_photo'),
        input_photo_handler = $('#id_photo');

    if(data['delete']){
        photo_handler.css('background-image', Ryabina.App.defaultPhotoBackground);
        delete_handler.hide();
        input_photo_handler.val('');
    }
};


Ryabina.App.deletePhoto = function(){
    var input_photo_handler = $('#id_photo'),
        file_id = input_photo_handler.val();
    if(file_id){
        $.ajax(Ryabina.App.deletePhotoUrl, {
            success : Ryabina.App.photoDeleteSuccess,
            data: {
              'file_id': file_id
            },
            error : function() {
                console.log('Неизвестная ошибка. Не удалось удалить аватар.');
            },
            type : 'POST',
            dataType : 'json',
            beforeSend : function(jqXHR) {
                jqXHR.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            }
        });
    }
};


Ryabina.App.photoLoaded = function(id, fileName, responseJSON){
    var photo_container_handler = $('#photo_container'),
        photo_handler = photo_container_handler.find('div.photo'),
        input_photo_handler = $('#id_photo'),
        delete_handler = photo_container_handler.find('div.delete_photo');

    if(responseJSON['upload']){
        input_photo_handler.val(responseJSON['file_id']);
        photo_handler.css('background-image', 'url("'+responseJSON['filename']+'?'+Ryabina.randomString(10)+'")');
        delete_handler.show();
    }
};


Ryabina.App.show_modal_comment = function(){
    var modal_form = bootbox.dialog({
        message: $('#comment_dialog_template').text(),
        closeButton: false
    });

    if(Ryabina.App.category_id){
        modal_form.find('#id_category').val(Ryabina.App.category_id);
    }
    modal_form.on("shown.bs.modal", function() {

        var photo_container_handler = $('#photo_container'),
        photo = photo_container_handler.find('div.photo'),
        delete_photo = photo_container_handler.find('div.delete_photo'),
        change_photo = photo_container_handler.find('div.change_photo');


        var uploader = new qq.FileUploaderBasic({
            button: photo[0],
            action: Ryabina.App.uploadPhotoUrl,
            multiple: false,
            sizeLimit: 1024 * 512,
            onSubmit: function(id, fileName) {
                change_photo.hide();
            },
            onComplete: function(id, fileName, responseJSON) {
                Ryabina.App.photoLoaded(id, fileName, responseJSON);
            },
            allowedExtensions : ['png', 'gif', 'bmp', 'jpg', 'jpeg', 'pcx'],
            messages: {
                typeError: "Изображение {file} недоступно для загрузки.",
                sizeError: "Размер изображения {file} превышает допустимый размер {sizeLimit}.",
                minSizeError: "{file} очень мал, минимальный размер {minSizeLimit}.",
                emptyError: "{file} пустой, пожалуйста выберите файл снова.",
                onLeave: "Файлы в процессе загрузки, если вы уйдете загрузка будет прекращена."
            }
        });
    
    
        photo.mousemove(function(e){
            var input_handler = photo.find('input'),
                left = e.pageX - photo.offset().left - input_handler.outerWidth()+140,
                top = e.pageY - photo.offset().top;
    
            input_handler.css({
                'left': left, //position right side 20px right of cursor X)
                'top': top
            });
        });
    
        photo.mouseover(function(){
             change_photo.show();
        });
    
        photo.mouseout(function(){
             change_photo.hide();
        });
    
        photo.ready(function(){
            Ryabina.App.photoMessageCenter();
        });
    
        delete_photo.click(function(){
            Ryabina.App.deletePhoto();
        });
        
        
    });
};

$(document).ready(function(){
    $('ul.menu_flex').flexMenu({
        linkText: '...',
        linkTextAll: 'Открыть список услуг',
        linkTitleAll: 'Услуги стоматологического центра',
        linkTitle: 'Открыть/Скрыть другие услуги',
        popupAbsolute: true,
        cutoff: 1,
        threshold: 1
    });

    $('.discounts_isotope_grid').imagesLoaded( function() {
        $('.discounts_isotope_grid').isotope({
            itemSelector: '.discounts_isotope_item',
            layoutMode: 'masonry',
            transitionDuration: 0
        });
    });

    $('a.btn[data-target=#modalComment]').click(function(e){
        Ryabina.App.show_modal_comment();
        e.preventDefault();
    });

    $(document).on('shown.bs.tab', 'a[data-toggle="tab"]', function (e) {
        Ryabina.App.category_id=$(this).data('category_id');
    });

    if($(".gallery > div").length>1){
        $(".gallery").flipping_gallery({
            direction: "forward", // This is will set the flipping direction when the gallery is clicked. Options available are "forward", or "backward". The default value is forward.
            selector: "> div", // This will let you change the default selector which by default, will look for <a> tag and generate the gallery from it. This option accepts normal CSS selectors.
            spacing: 10, // You can set the spacing between each photo in the gallery here. The number represents the pixels between each photos. The default value is 10.
            showMaximum: 15, // This will let you limit the number of photos that will be in the viewport. In case you have a gazillion photos, this is perfect to hide all those photos and limit only a few in the viewport.
            enableScroll: false, // Set this to false if you don't want the plugin to override your scrolling behavior. The default value is true.
            flipDirection: "bottom", // You can now set which direction the picture will flip to. Available options are "left", "right", "top", and "bottom". The default value is bottom.
            autoplay: false // You can set the gallery to autoplay by defining the interval here. This option accepts value in milliseconds. The default value is false.
        });
    }
});