# Ajax CSRF 

https://stackoverflow.com/questions/49541397/django-ajax-csrf-token-missing

key: `headers:{"X-CSRFToken": '{{ csrf_token }}'},` 

```js 
$('.your_class').click(function () {
    $.ajax({
        type: "POST",
        dataType:'json',
        headers:{"X-CSRFToken": '{{ csrf_token }}'},
        url: decodeURI("{% url 'your_url' %}"),
        data: {"ajax_item":"{{data_you_want_to_send}}"},
        success: function(data){
        	// add your logic here
            alert(data);
        }
    });
});
```