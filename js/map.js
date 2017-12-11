var map = new ol.Map({
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    target: 'map',
    view: new ol.View({
        center: [0, 0],
        zoom: 2
    })
});

// https://stackoverflow.com/questions/41877799/get-dynamic-content-using-pyqt
// https://stackoverflow.com/questions/28565254/how-to-use-qt-webengine-and-qwebchannel
// https://snorfalorpagus.net/blog/2014/09/13/embedding-a-leaflet-map-in-a-qt-application/

$(document).ready(function(){
    new QWebChannel(qt.webChannelTransport, function (channel) {
        MyChannel = channel.objects.MyChannel;
        var set_lbl_coord = function () { MyChannel.set_lbl_coord(JSON.stringify(map.getView().getCenter())) };
        map.on('moveend', set_lbl_coord);
        set_lbl_coord();
    });
});

