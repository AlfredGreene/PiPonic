<?php
	include("connection.php");

	if(!$link=Connection()){
		print("Connect Failed");
	}

	$result=mysql_query("SELECT * FROM  `data` ORDER BY `date` DESC", $link);
	
	include("header.html");

?>

	<h1> All PiPonic Readings </h1>
		<table border="1" cellspacing="1" cellpadding="1">
		<tr>
		<td>&nbsp;Date&nbsp;</td>
		<td>&nbsp;Moisture&nbsp;</td>
		<td>&nbsp;Temperature&nbsp;</td>
		<td>&nbsp;Light&nbsp;</td>
		</tr>

				<?php
					if($result!==FALSE){
						while($row = mysql_fetch_array($result)) {
							printf("<tr><td> &nbsp; %s </td><td> &nbsp; %s &nbsp;</td><td> &nbsp; %s &nbsp;</td><td> &nbsp; %s &nbsp; </td></tr>", $row["date"], $row["moisture"], $row["temperature"], $row["light"]);
						}
					mysql_free_result($result);
					mysql_close();
					} else print("Result failed");
				?>

		</table>

<?php
	include("footer.html");
?>


