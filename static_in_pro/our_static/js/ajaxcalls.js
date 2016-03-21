

$(document).ready(function() {
$("#test").submit(function(event){
    $.ajax({
    url: '127.0.0.1:8000/first',
    type: 'get', // This is the default though, you don't actually need to always mention it
    success: function(data) {
        alert(data);
    },
    failure: function(data) {
        alert('Got an error dude');
    }
        });
    });
});