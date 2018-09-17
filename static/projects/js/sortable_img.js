$(document).ready(function(){

    $( "#sortable" ).sortable(
        {
            update: function(){
                var count=1
                 $( "#sortable" ).children().each(function(){
                    $(this).find('.currOrder').html(count) ;
                    var myinput = $(this).find('input').val(count);
                    count++;
                 });        

            }
        });
    $( "#sortable" ).disableSelection();

})