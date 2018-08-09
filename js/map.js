var map = new ol.Map({
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    target: 'map',
    view: new ol.View({
		projection: 'EPSG:4326',
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
        var set_lbl_coord = function () {
			var center_coord = map.getView().getCenter()
			MyChannel.set_lbl_coord(JSON.stringify(center_coord, function(key, val) {
				return val.toFixed ? Number(val.toFixed(6)) : val;
			}));
			};
        map.on('moveend', set_lbl_coord);
        set_lbl_coord();
    });
});

