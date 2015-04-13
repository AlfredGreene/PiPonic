<?php
	include("connection.php");

	$link = Connection();

	$result = mysql_query("SELECT * FROM 'data' ORDER BY 'date' DESC", $link);

	phpinfo();

?>

<?php phpinfo(); ?>
