
//  THIS FILE IS JUST ABOUT SCROLLING BEHAVIOUR OF HOME AND PROJECT PAGE
// THE EVENTS AFFECT WEBPAGE TO SCROLL TO PERTICULAR DIV, NOT IN BETWEEN
// CONSTIT OF EVENTS FOR SCROLL, CLICK, SIDE MENU



// Establish div to scroll to
function getTargetDiv(currDiv, value = 1){
    scrollTime = 800
    targetDiv = currDiv + value

    // check if div exist
    toString(targetDiv)
    var div = document.getElementById(targetDiv);
    if (div==null){
        targetDiv = 1;
        scrollTime = 2000;
    };
}


// scroll to div (it takes global targetDiv variable)
function scrollTo(){
    //turn of reaction to scroling
    $(window).off("scroll",scrollUpOrDown);

    // prepare targetDiv depending if it already consist of '#' or not
    // if user clicked on side div menu target div is taken form link atribute instead be generated bt getTargetDiv function
    // so currentDiv must be updated here
    if (targetDiv[0] == '#'){
        divToGoTo = targetDiv
        targetDiv = Number(targetDiv.substr(1));
    }else{
        divToGoTo = '#' + targetDiv
    }

    //animate scroling to target div
    $('html').animate({
        scrollTop: $(divToGoTo).offset().top
    }, scrollTime,);
    // wait until activating scroll function and update global variables
    waitTime = scrollTime + 50
    setTimeout(scrollOn, waitTime)
    currentDiv = targetDiv
    
}


function scrollOn(){
    $(window).on("scroll", scrollUpOrDown);
    position = $(window).scrollTop();
}


// fuction for scrollin on mouse scroll event
function scrollUpOrDown(){
            var scroll = $(window).scrollTop();
        if(scroll > position) {  
            getTargetDiv(currentDiv);
            scrollTo();
            //console.log('mouse: scroll down');            
        } else {
            valueDiv = -1
            getTargetDiv(currentDiv, valueDiv);
            scrollTo();
            //console.log('mouse: scroll up');
        }   
}


// -------------------------------------------------------- global variables
var currentDiv = 1
var targetDiv = null
var scrollTime = 800
var position = $(window).scrollTop();

// -------------------------------------------------------- Main
$(document).ready(function(){

    // scroll on scroll up or down
    $(window).on("scroll", scrollUpOrDown);
    
    // scroll on click on side div
    $('.side-nav-link').click(function(){
        targetDiv = $(this).attr('href')    
        scrollTo()
    });
});

