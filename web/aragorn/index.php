<?php
	session_start();
	
	include 'lib/Mysql.php';
    $mysql = new Mysql;
    $mysql->connect();

	if(isset($_GET)) {
		$user_id = $_GET['user_id'];
		$record = $_GET['record'];
		$sql_str = 'INSERT INTO `records` (`user_id`, `record`) VALUES ('."'".$user_id."'".', '."'".$record."'".')';
        $mysql->query($sql_str);
	} else {
		echo 'nothing get';
	}
?>
