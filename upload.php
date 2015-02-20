<?php
$db_host="127.0.0.1";
$db_username="root";
$db_pass="";
$db_name="campusflats";

@mysql_connect("$db_host","$db_username","$db_pass") or die ("oopppsss...cannot connect to MySQL database");
@mysql_select_db("$db_name") or die ("database not found");


if(isset($_POST['submit']) && isset($_FILES['image']))
{
	if (getimagesize($_FILES['image']['tmp_name'])==FALSE) {
		echo "please select an image";
	}
	else
	{
		$image=addslashes($_FILES['image']['tmp_name']);
		$name=addslashes($_FILES['image']['name']);
		$image=file_get_contents($image);
		$image=base64_encode($image);
		save($name,$image);
	
	}
	
}
elseif (isset($_POST['submit']) && !isset($_FILES['image'])) {
	echo "file was notsent to database!";
}
	


function save($name,$image)
{
	$query="INSERT INTO `campusflats`.`images` (`ID`, `Image`, `name`) VALUES (NULL, '$image', '$name');";
	$result=mysql_query($query);
	if ($result) {
		echo "<br/>image uploaded successfully!";
	}
	else
	{
		echo "<br/>image not uploaded successfully!";
	}
	}



?>