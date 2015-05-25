
function setActiveLink(selector){
    $('#menu').find('a').removeClass('active');
    if (selector){
        $(selector).addClass('active');
    }
}