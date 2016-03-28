function showQuestion(value) {
        //document.getElementById("show-question").innerHTML = showthis;
        $.ajax({
            url: '/postquestion/',
            dataType:'json',
            type:'GET',
            data:{
                quest: value
            },
            success: function(data){
                console.log(data);
                showQ = data.question;
                document.getElementById("show-question").innerHTML = showQ;
            }

        });

    }


$(document).ready(function(){

    $("#submitquery").on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")
        var q = $('#querybox').val();
        makeQuery(q);

    });
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