$(document).ready(function(){

    $("#submitquery").on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")
        var q = $('#querybox').val();
        makeQuery(q);

    });
    $("#questionsubmit")

    function makeQuery(q){
        console.log("We makin those queries!");
        $.ajax({
            url: '/search/',
            dataType: 'json',
            type: 'GET',
            data: {
                         q: q
            },
            success: function(data)
            {
               var show = data.cities;
               $('#showqueryhere').html(show)
            }
        });

    }
});