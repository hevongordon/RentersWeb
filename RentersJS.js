function load()

{	$("#left-side-content").load("simple-fade-slideshow.source.html");
	$("#areas").mousedown(function(){
	$("#rightside").load("filter.html");
		$("#right-side-content").load("test.html");
	$("#content").load("areas.html");
	$("#left-side-content").load("areas.html");
});	
}

$("#filterbutton").mousedown(function(){
	alert("this is a test");
});

/*$("#home").mousedown(function(){
	$("#content").load("");
});
*/
$("#firstheading").mousedown(function()
{
$("#content").load("full-width-slider.source.html");
$("#rightside").empty();
alert("hey this was done!");
});




