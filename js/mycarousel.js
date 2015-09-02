$(document).ready(function () {
    var quotes = [];
    var initial = "<p class=\"inital-text\">Inspiration can come from the most unlikely places,"+ 
    "to learn design, we must continually seek out new inspiration"+
    "so let this be a way to find some.</p>"+
"<span class=\"inital-text\">Perform action to find some</span>";
    quotes.push(initial);
    var counter = quotes.length;
    //$("body").css({"background-color": "black"}); #for testing with carousel.html, provides contrast.
    $("#right").on({ 
    mouseenter: function () {
        $(this).addClass("netflix-shadow");
    },
    mouseleave: function () {
        $(this).removeClass("netflix-shadow");
    },
    click: function () {
        if (counter === quotes.length){        
            $.ajax( {
      		url: 'https://jsonp.afeld.me/?url=http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1',
        	success: function ( data ) {
        		var post = data.shift();
        		quotes.push(post.content);
        		counter++;  
        		$("#text-area").html(quotes[counter-1]);
        		//$("#text-area").append(counter-1);  

      },
      cache: false
    } );}
        else {
            counter++;
            $("#text-area").html(quotes[counter-1]);
            //$("#text-area").append(counter-1);
        }
    }    
      
});
    $("#left").on({
    mouseenter: function () {
        $(this).addClass("netflix-shadow");
    },
    mouseleave: function () {
        $(this).removeClass("netflix-shadow");
    },
     click: function () {
        if (counter > 1){
            counter--;
            $("#text-area").html(quotes[counter-1]);
            //$("#text-area").append(counter-1);
            
        }
     },
        
        
        
});

});

