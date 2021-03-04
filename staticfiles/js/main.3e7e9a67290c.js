
$(document).ready(function(){
    $(".scr").on("click", function (event) {
        event.preventDefault();
        var id  = $(this).data("to"),
            top = $(id).offset().top;
        $('body,html').animate({scrollTop: top}, 50);
    });
    
//    $(".lang-ch").on("click",function(){
//        $($(this).data("lang")).css("display","none");
//        $($("act-langu").data("lang")).css("display","none");
//        $(this).addClass("act-langu");
//        $(this).data("lang")
//    });
});