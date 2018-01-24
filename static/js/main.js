$( document ).ready(function() {

	$( ".mydropdown" ).on("tap", function(){
	 	$( ".dropdownlinks" ).slideToggle('fast');
	});

	if($('#isntmobile').is(':visible')) {
		$( ".mydropdown" ).mouseenter(function(){
		 	$( ".dropdownlinks" ).slideToggle('fast');
		});
		$( ".mydropdown" ).mouseleave(function(){
		 	$( ".dropdownlinks" ).slideToggle('fast');
		});					
	}
	else {
		$( ".mydropdown" ).click(function(){
		 	$( ".dropdownlinks" ).slideToggle('fast');
		});	
	}



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

// function myFunction() {
//     var x, text;

//     // Get the value of the input field with id="numb"
//     x = document.getElementById("id_first_name").value;

//     // If x is Not a Number or less than one or greater than 10
//     if (isNaN(x) || x < 1 || x > 10) {
//         text = "Input not valid";
//     } else {
//         text = "Input OK";
// 		$( "#userdetails" ).slideToggle('slow');
		
//     }
//     document.getElementById("anotherone").innerHTML = text;
// }	

function validateForm() {
    var first_name = document.forms["shippingForm"]["first_name"].value;
    var last_name = document.forms["shippingForm"]["last_name"].value;
    var email = document.forms["shippingForm"]["email"].value;
    if (first_name == "" || null || last_name == "" || null || email == "" || null ) {
        text = "Please fill in all fields"
        document.getElementById("anotherone").innerHTML = text;
        return false;
    }
    else {
        // $( "#userdetails" ).slideToggle('slow');
        $( "#shippingdetails" ).slideToggle('slow');
    }
}	 	