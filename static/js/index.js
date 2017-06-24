/**
 * Created by Administrator on 2016/12/1.
 */
$.fn.extend({
    animateCss: function (animationName) {
        var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
        this.addClass('animated ' + animationName).one(animationEnd, function() {
            $(this).removeClass('animated ' + animationName);
        });
    }
});

$(document).ready(function(){
    $(".header-img img").animateCss("bounceInDown")
});

function loadArticle() {

    $.ajax({
            url:"/使用Python爬取妹子图片",
            method:"post",
            success:function(text) {
                $(".right-col").empty();
                $(".right-col").append(text);
            }
        });
}