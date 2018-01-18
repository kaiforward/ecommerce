$( document ).ready(function() {
	$( ".mydropdownbutton" ).on("tap", function(){
	 	$( ".dropdownlinks" ).slideToggle('fast');
	})	
	if($('#isntmobile').is(':visible')) {
		$( ".mydropdown" ).hover(function(){
		 	$( ".dropdownlinks" ).slideToggle('fast');
		})		
	}
	else {	
		$( ".mydropdownbutton" ).click(function(){
		 	$( ".dropdownlinks" ).slideToggle('fast');
		})
	};

	// Add swipe functionality to images
	$(".mycarousel").on("touchstart", function(event){
	        var xClick = event.originalEvent.touches[0].pageX;
	    $(this).one("touchmove", function(event){
	        var xMove = event.originalEvent.touches[0].pageX;
	        if( Math.floor(xClick - xMove) > 5 ){
	            $(this).carousel('next');
	        }
	        else if( Math.floor(xClick - xMove) < -5 ){
	            $(this).carousel('prev');
	        }
	    });
	    $(this).on("touchend", function(){
	            $(this).off("touchmove");
	    });
	});
});

