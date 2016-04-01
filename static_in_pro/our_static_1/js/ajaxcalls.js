function showQuestion(value) {
        //document.getElementById("show-question").innerHTML = showthis;
        $.ajax({
            url: '/getquestion/',
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

    $("#submitquery-1,#submitquery-2,#submitquery-3").on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")
        var id_str = $(this).attr('id');
        var id_split_arr = id_str.split("-");
        i = id_split_arr[1];
        var q = $(this).find('.querybox').val();
        makeQuery(q,i);
        var q = $(this).find('.querybox').val();
        var width = $('#table-striped-'+i).width()

    });


    function makeQuery(q,i){
        console.log("We makin those queries!");
        $.ajax({
            url: '/search/',
            dataType: 'json',
            type: 'GET',
            data: {
                         q: q,
                         i: i
            },
            success: function(data)
            {
               var show = data.cities;
               var render_div = '#showqueryhere' + i
               $(render_div).html(show)
            }
        });

    }
});