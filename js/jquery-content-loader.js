// About
$(function(){
    $("#about").load("content/about.html")
});

// Projects
$(function(){
    $("#projects").load("content/projects.html")
});


// GetJSON
$.getJSON("../data/engineering_quotes.json", function(json){
    console.log(json);
})