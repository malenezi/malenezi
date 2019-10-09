
(function( $ ) {
	"use strict";
	
	jQuery(window).resize(function() {
		refreshSidebar();
	});

	jQuery(window).ready(function() {

		jQuery('img').each( function(i){
			var bottom_of_object = jQuery(this).offset().top + jQuery(this).outerHeight();
			var bottom_of_window = jQuery(window).scrollTop() + jQuery(window).height() + 200;

			if( bottom_of_window <= bottom_of_object ){
				jQuery(this).css("opacity", "0");
			}
		});

		jQuery(window).scroll( function(){
			jQuery('img').each( function(i){
				var bottom_of_object = jQuery(this).offset().top + jQuery(this).outerHeight();
				var bottom_of_window = jQuery(window).scrollTop() + jQuery(window).height() + 200;

				if( bottom_of_window > bottom_of_object ){
					jQuery(this).animate( {'opacity':'1'}, 500 );
				}
			});
		});

		jQuery(".tab-a").each(function(){
			jQuery(this).find("h3").eq(0).addClass("active");
		});

		jQuery(".tab-d").each(function(){
			jQuery(this).children("div").eq(0).addClass("active");
		});

		jQuery(".tab-a h3").click(function(){
			var thisel = jQuery(this);
			var thisindex = thisel.index();
			thisel.addClass("active").siblings("h3.active").removeClass("active");
			thisel.parent().siblings(".tab-d").children("div").eq(thisindex).addClass("active").siblings("div.active").removeClass("active");
			refreshSidebar();
		});

		jQuery(".w-photos .photo-images").each(function(){
			jQuery(this).children("a").eq(0).addClass("active");
		});

		jQuery(".gallery-link-left").click(function(){
			slideGalleryWidget(jQuery(this).siblings(".photo-images").children("a.active").prev());
			return false;
		});

		jQuery(".gallery-link-right").click(function(){
			slideGalleryWidget(jQuery(this).siblings(".photo-images").children("a.active").next());
			return false;
		});

		jQuery(".carousel-right").click(function(){
			var thisel = jQuery(this);
			var maxcount = Math.ceil((thisel.siblings(".inner-carousel").children(".item").size())/3);
			if(thisel.parent().attr("rel")){
				if(thisel.parent().attr("rel") < maxcount-1){
					var nuum = parseInt(thisel.parent().attr("rel"))+1;
				}else{
					var nuum = parseInt(thisel.parent().attr("rel"));
				}
			}else{
				if(maxcount-1 >= 1){
					var nuum = 1;
				}else{
					var nuum = 0;
				}
			}
			thisel.parent().attr("rel", nuum);
			thisel.siblings(".inner-carousel").animate({
				"left" : "-"+(nuum*103.5)+"%"
			}, 200);
			return false;
		});

		jQuery(".carousel-left").click(function(){
			var thisel = jQuery(this);
			if(thisel.parent().attr("rel")){
				if(thisel.parent().attr("rel") > 0){
					var nuum = parseInt(thisel.parent().attr("rel"))-1;
				}else{
					var nuum = parseInt(thisel.parent().attr("rel"));
				}
			}else{
				var nuum = 0;
			}
			thisel.parent().attr("rel", nuum);
			thisel.siblings(".inner-carousel").animate({
				"left" : "-"+(nuum*103.5)+"%"
			}, 200);
			return false;
		});

		jQuery(".slider .slider-navigation li > a").click(function() {
			var thisel = jQuery(this);
			var thisindex = thisel.parent().index();
			thisel.parent().addClass("active").siblings("li.active").removeClass("active");
			thisel.parent().parent().siblings(".slider-image").children("a").eq(thisindex).addClass("active").siblings("a.active").each(function() {
				var curel = jQuery(this);
				setTimeout(function () {
					curel.removeClass("active");
				}, 100);
			});
			return false;
		});


		// Alert box close
		jQuery('a[href="#close-alert"]').click(function() {
			jQuery(this).parent().animate({
				opacity: 0,
				padding: "0px 13px",
				margin: "0px",
				height: "0px"
			}, 300, function() {
				refreshSidebar();
			});
			return false;
		});

		// Accordion blocks
		jQuery(".accordion > div > a").click(function() {
			var thisel = jQuery(this).parent();
			if(thisel.hasClass("active")){
				thisel.removeClass("active").children("div").animate({
					"height": "toggle",
					"opacity": "toggle",
					"padding-top": "toggle"
				}, 300);
				return false;
			}
			// thisel.siblings("div").removeClass("active");
			thisel.siblings("div").each(function() {
				var tz = jQuery(this);
				if(tz.hasClass("active")){
					tz.removeClass("active").children("div").animate({
						"height": "toggle",
						"opacity": "toggle",
						"padding-top": "toggle"
					}, 300, function() {
						refreshSidebar();
					});
				}
			});
			// thisel.addClass("active");
			thisel.addClass("active").children("div").animate({
				"height": "toggle",
				"opacity": "toggle",
				"padding-top": "toggle"
			}, 300, function() {
				refreshSidebar();
			});
			return false;
		});
	  

		// Tabbed blocks
		jQuery(".short-tabs").each(function() {
			var thisel = jQuery(this);
			thisel.children("div").eq(0).addClass("active");
			thisel.children("ul").children("li").eq(0).addClass("active");
		});

		jQuery(".short-tabs > ul > li a").click(function() {
			var thisel = jQuery(this).parent();
			thisel.siblings(".active").removeClass("active");
			thisel.addClass("active");
			thisel.parent().siblings("div.active").removeClass("active");
			thisel.parent().siblings("div").eq(thisel.index()).addClass("active");
			refreshSidebar();
			return false;
		});

		jQuery(".lightbox").click(function () {
			jQuery(".lightbox").css('overflow', 'hidden');
			jQuery("body").css('overflow', 'auto');
			jQuery(".lightbox .lightcontent").fadeOut('fast');
			jQuery(".lightbox").fadeOut('slow');
		}).children().click(function(e) {
			return false;
		});


		// Responsive menu
		jQuery(".main-menu > div").append('<a href="#" class="toggle-menu"><i class="fa fa-ban"></i> Toggle Menu</a>');
		jQuery(".header-topmenu > div").append('<a href="#" class="toggle-menu"><i class="fa fa-ban"></i> Toggle Menu</a>');
		
		jQuery(".toggle-menu").click(function() {
			var thisel = jQuery(this).siblings("ul");
			thisel.fadeToggle();
			return false;
		});


		// Refresh sidebars look
		refreshSidebar();

	});

})(jQuery);

function lightboxclose(){
	jQuery(".lightbox").css('overflow', 'hidden');
	jQuery(".lightbox .lightcontent").fadeOut('fast');
	jQuery(".lightbox").fadeOut('slow');
	jQuery("body").css('overflow', 'auto');
}


function refreshSidebar() {
	jQuery("#sidebar").each(function() {
		jQuery(this).css("height", "auto");
		var maxheight = jQuery(this).height();
		var secondheight = jQuery(".main-content").height();
		maxheight = (parseInt(secondheight) > parseInt(maxheight))?secondheight:maxheight;
		jQuery("#sidebar").css("height", maxheight);
	});
}

function slideGalleryWidget(theitem) {
	theitem.css("opacity", "0").css("display", "block").animate({
		"opacity" : "1"
	}, 200, function(){
		jQuery(this).addClass("active").siblings("a.active").removeClass("active").css("display", "none");
		refreshSidebar();
	});
}



