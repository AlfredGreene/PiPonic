<?php
	function Connection(){
		$server="localhost";
		$user="root";
		$pass="tortuga";
		$db="data";
		
		$connection = mysql_connect($server, $user, $pass);

		if(!$connection){
		die('MySQL ERROR: '. mysql_error());
		}

		mysql_select_db($db) or die( 'MySQL ERROR: '. mysql_error() );

		return $connection;
	}
?>
