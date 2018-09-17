function disableScrolling(isDisabled){

    if(isDisabled){
        $('body').attr('scroll', 'yes');
        $('body').attr('style', 'overflow:visible;');
        scrollDisable = false

    }else{
        $('body').attr('scroll', 'no');
        $('body').attr('style', 'overflow:hidden;');
        scrollDisable = true
    }
}


function menuToggle(){$('.my-nav').css('height','100%');};

function fadeInToggle(isDisabled){
    if(isDisabled){
        setTimeout(function(){ menuItemsLi[0].animate({ opacity:1, width: "100%", },800) },200);
        setTimeout(function(){ menuItemsLi[1].animate({ opacity:1, width: "100%", },800) },400);
        setTimeout(function(){ menuItemsLi[2].animate({ opacity:1, width: "100%", },800) },600);
    }else{
        console.log('close')
        setTimeout(function(){ menuItemsLi[0].animate({ opacity:0, width: "60%", },800) },200);
        setTimeout(function(){ menuItemsLi[1].animate({ opacity:0, width: "60%", },800) },400);
        setTimeout(function(){ menuItemsLi[2].animate({ opacity:0, width: "60%", },800) },600);
    }
}
//global variables
var scrollDisable = false
var count = 0
var menuItemsLi= []

//MAIN
$(document).ready(function(){
    
    var menuUl = ''
    var allLinks = $('.nav-menu-ul').children('li').each(function(){
        var item = $(this).html();
        item = '<li class="opacity">' + item + '</li>'
        menuUl = menuUl + item
        //console.log(item);
    });

    menuUl = '<div class="menu-collapse"><ul class="mobile-menu-ul-close">'+ menuUl +'</ul></div>';
    $('.my-nav').after(menuUl);

	$('.menu-button').click(function(){

        disableScrolling(scrollDisable);

        $(this).toggleClass('open');
        $('.my-nav').toggleClass('openMenu');
        $('.mobile-menu-ul-close').toggleClass('mobile-menu-ul-open');
        $('.menu-collapse').toggleClass('menu-collapse-open');


        $('.mobile-menu-ul-open').children('li').each(function(index){
            x = $(this)
            menuItemsLi.push(x)
        });
        fadeInToggle(scrollDisable);

    });
});