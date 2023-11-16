// map.js

// Initialize the map
var mymap = L.map('map').setView([43.2301, 5.4323], 15); // Set latitude, longitude, and zoom level

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; OpenStreetMap contributors'
}).addTo(mymap);

// Add a marker to the map
var marker = L.marker([43.2301, 5.4323]).addTo(mymap);
marker.bindPopup("<b>Luminy Faculty - France</b>").openPopup();