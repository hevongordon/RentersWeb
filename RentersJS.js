function load()

{	$("#bottom").load("information.html");
	$("#areas").mousedown(function(){
	$("#rightside").load("filter.html");
	$("#content").load("areas.html");
});	
}

$("#filterbutton").mousedown(function(){
	alert("this is a test");
});

/*$("#home").mousedown(function(){
	$("#content").load("");
});
*/





