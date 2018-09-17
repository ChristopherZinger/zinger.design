
function descContentToggle(x){
    if(x == true){
        $('.description-text').toggleClass('open')
        $('.description-title').toggleClass('open')
    }else{
        setTimeout(function(){
            $('.description-text').toggleClass('open')
            $("h3").animate({opacity: 1});
            $(".description-text").animate({opacity: 1});
            
        },500);
        setTimeout(function(){
            $('.description-title').toggleClass('open')
        },500);
    }
}

function isOpenToggle(x){
    if(x == true){
        isOpen = false
    }else{
        isOpen = true
    }
}

function descriptionCloseToggle(x){
    if(x == true){
        $('#x-description').html('description');
    }else{
        $('#x-description').html('');
    }
}

var isOpen = false
//MAIN
$(document).ready(function(){
	$('.x-icon').click(function(){

        $('#desc-icon3').toggleClass('open');
        $('.description-container').toggleClass('open');
        $('#x-description').toggleClass('open');

        descContentToggle(isOpen);
        descriptionCloseToggle(isOpen);
        isOpenToggle(isOpen);
    });
    
});