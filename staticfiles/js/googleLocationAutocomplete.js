function init() {
	var input = document.getElementById('location-input')
    var autocomplete = new google.maps.places.Autocomplete(input)
}
google.maps.event.addDomListener(window, 'load', init)