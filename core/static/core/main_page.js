function ajaxifyLinks(){
    // Capture all the links to push their url to the history stack and trigger the StateChange Event
    $('a').not('.external_link').click(function(evt) {
        History.pushState(null, $(this).text(), $(this).attr('href'));
        // do not execute the actual link behaviour
        evt.preventDefault();
    });
}
 
function setActiveLink(selector){
    $('#menu').find('a').removeClass('active');
    if (selector){
        $(selector).addClass('active');
    }
}