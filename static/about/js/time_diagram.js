$(document).ready(function(){

    //Adjust height of the timegraph bars
    var rowHeight = $('#time-graph-dates').height()
    var liCount = $('#time-graph-bars').children().length;

    liHeight = rowHeight/liCount
    liMarginTop = (liHeight/2).toString() + "px"
    $('#time-graph-bars').children().height(liHeight);
    $('.time-bar').css("margin-top",liMarginTop)
})