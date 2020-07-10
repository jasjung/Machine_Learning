# Google Maps API 

- https://developers.google.com/maps/documentation/javascript/tutorial
- https://developers.google.com/maps/documentation/javascript/places#find_place_from_query


## hiding api key 

- https://medium.com/better-programming/how-to-hide-your-api-keys-c2b952bc07e6


## Save results from api 

https://stackoverflow.com/questions/46621928/how-to-format-output-result-of-google-maps-api-autocomplete


## Move search box out side of mapview 

https://stackoverflow.com/questions/20921378/google-maps-search-box-outside-map/20923791

comment this out: 

```js 
map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
```

## Search Box Only 

```html
new google.maps.places.Autocomplete(
  (document.getElementById('autocomplete')), {
    types: ['geocode']
  });

#autocomplete {
  width: 300px;
}

<input id="autocomplete" placeholder="Enter your address" type="text"></input>

<script src="https://maps.googleapis.com/maps/api/js?libraries=places"></script>
```

## Center map 

