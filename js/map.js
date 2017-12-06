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

// https://stackoverflow.com/questions/39544089/how-can-i-access-python-code-from-javascript-in-pyqt-5-7
new QWebChannel(qt.webChannelTransport, function (channel) {
                window.handler = channel.objects.handler;
});

// https://snorfalorpagus.net/blog/2014/09/13/embedding-a-leaflet-map-in-a-qt-application/
map.on('moveend',
       window.handler.set_lbl_coord(JSON.stringify(map.getCenter()))
);

