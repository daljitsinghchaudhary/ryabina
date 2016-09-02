$(document).ready(function(){

    function map_init() {
        ryabinaMap = new ymaps.Map('map-container', {
            center:[59.934837, 30.272213],
            zoom:16,
            controls: []
        });

        var fullscreenControl = new ymaps.control.FullscreenControl({
            data: {},
            options:{
                visible: false
            }
        });

        ryabinaMap.controls.add(fullscreenControl);
        fullscreenControl.events.add('fullscreenexit', function(event){
            fullscreenControl.options.set('visible', false);
        });

        myPlacemark = new ymaps.Placemark([59.934837, 30.272213], {
            hintContent: "Стоматологический центр Рябина",
        },{
            iconLayout: 'default#image',
            iconImageHref: '/static/img/logo/map_icon.png',
            iconImageSize: [57, 80],
            iconImageOffset: [-28, -80]
        });

        ryabinaMap.geoObjects.add(myPlacemark);
        ryabinaMap.behaviors.disable("scrollZoom");
        
        $(document).on('map_increase', function(){
            var zoomRange = ryabinaMap.zoomRange.getCurrent(),
                currentZoom = ryabinaMap.getZoom();
            if(currentZoom+1 <= zoomRange[1]){
                $('.map_btn.reduce').removeClass('disabled');
                ryabinaMap.setZoom(currentZoom+1);
                if(currentZoom+1 == zoomRange[1]){
                    $('.map_btn.increase').addClass('disabled');
                }
            }
        });

        $(document).on('map_reduce', function(){
            var zoomRange = ryabinaMap.zoomRange.getCurrent(),
                currentZoom = ryabinaMap.getZoom();
            if(currentZoom-1 >= zoomRange[0]){
                $('.map_btn.increase').removeClass('disabled');
                ryabinaMap.setZoom(currentZoom-1);
                if(currentZoom-1 == zoomRange[0]){
                    $('.map_btn.reduce').addClass('disabled');
                }
            }
        });

        $(document).on('map_fullscreen', function(){
            fullscreenControl.enterFullscreen();
            fullscreenControl.options.set('visible',true);
        });

        $(document).on('map_route', function(){
            var polyline = new ymaps.Polyline([
                    [59.942487, 30.278117],
                    [59.942815, 30.277870],
                    [59.942261, 30.276025],
                    [59.938116, 30.280832],
                    [59.935231, 30.271041],
                    [59.934596, 30.271792],
                    [59.934747, 30.272275]
            ], {
                 hintContent: '1.2 км'
            }, {
                 strokeColor: '#0066ff',
                 strokeWidth: 4,
                 strokeStyle: '3 2'
            });
            ryabinaMap.geoObjects.add(polyline);
            ryabinaMap.setBounds(polyline.geometry.getBounds());
        });
    }

    ymaps.ready(map_init);

    $('.map_btn.increase').click(function(){
        $(document).trigger('map_increase');
    });
    $('.map_btn.reduce').click(function(){
        $(document).trigger('map_reduce');
    });
    $('.map_btn.fullscreen').click(function(){
        $(document).trigger('map_fullscreen');
    });
    $('.map_btn.route').click(function(){
        $(document).trigger('map_route');
    });

    var $grid = $('.contacts_images_isotope_grid').imagesLoaded( function() {
        $grid.isotope({
            itemSelector: '.contacts_images_isotope_item',
            layoutMode: 'cellsByRow',
            cellsByRow: {
//              columnWidth: 110,
              rowHeight: 390
            }
        });
    });
    $(document).on('contacts_images_filter', function(event, filterValue){
        $grid.isotope({ filter: filterValue });
    });

    $('.contacts_images_btn').click(function(){
        $(document).trigger('contacts_images_filter', $(this).data('filter'));
    });

    $('a.fancy').fancybox({
        padding : 0,
        titlePosition : 'inside',
        openEffect  : 'elastic',
        closeBtn: false,
        overlayColor: '#2f4f4f',
        overlayOpacity: 0.8
    });
});