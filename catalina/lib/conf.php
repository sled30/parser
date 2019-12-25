<?php
class MyDB extends SQLite3{
        function __construct()
        {
                $this->open('mysqlitedb.db');

        }

}
/* CREATE INDEX "phone" ON "ids" (
	"phone",
	"string_error"
);*/
function create_index(){
  // code...
  $db = new MyDB();
  $sql = "CREATE INDEX `phone` ON `ids` (`phone`, `string_error`)";
  $db->exec($sql);
	$db->close();
}
function create_db(){
	// code...
	$db = new MyDB();
	$sql = "CREATE TABLE IF NOT EXISTS `source` (
	  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
	  `phone` varchar(14) NOT NULL, `count_error` varchar(3) NOT NULL,
    `string_error` varchar(20) NOT NULL, `secund` varchar(2) NOT NULL,
    `1_error` varchar(100) NULL, `2_error` varchar(100) NULL,
    `3_error` varchar(100) NULL, `4_error` varchar(100) NULL,
    `5_error` varchar(100) NULL,  `6_error` varchar(100) NULL,
    `7_error` varchar(100) NULL, `8_error` varchar(100) NULL,
    `9_error` varchar(100) NULL, `10_error` varchar(100) NULL,
    `11_error` varchar(100) NULL,  `12_error` varchar(100) NULL,
    `13_error` varchar(100) NULL,  `14_error` varchar(100) NULL,
    `15_error` varchar(100) NULL, `16_error` varchar(100) NULL,
    `17_error` varchar(100) NULL, `18_error` varchar(100) NULL,
    `19_error` varchar(100) NULL, `20_error` varchar(100) NULL,
    `21_error` varchar(100) NULL, `22_error` varchar(100) NULL,
    `23_error` varchar(100) NULL,  `24_error` varchar(100) NULL,
    `25_error` varchar(100) NULL,  `26_error` varchar(100) NULL,
    `27_error` varchar(100) NULL, `28_error` varchar(100) NULL,
    `29_error` varchar(100) NULL, `30_error` varchar(100) NULL);
    CREATE TABLE IF NOT EXISTS `ids` (
  	  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
  	  `phone` varchar(14) NOT NULL, `string_error` varchar(100) NOT NULL,
      `secund` varchar(2) NULL, `status` varchar(2) NULL,
      `1_error` varchar(100) NULL, `2_error` varchar(100) NULL,
      `3_error` varchar(100) NULL, `4_error` varchar(100) NULL,
      `5_error` varchar(100) NULL,  `6_error` varchar(100) NULL,
      `7_error` varchar(100) NULL, `8_error` varchar(100) NULL,
      `9_error` varchar(100) NULL, `10_error` varchar(100) NULL,
      `11_error` varchar(100) NULL,  `12_error` varchar(100) NULL,
      `13_error` varchar(100) NULL,  `14_error` varchar(100) NULL,
      `15_error` varchar(100) NULL, `16_error` varchar(100) NULL,
      `17_error` varchar(100) NULL, `18_error` varchar(100) NULL,
      `19_error` varchar(100) NULL, `20_error` varchar(100) NULL,
      `21_error` varchar(100) NULL, `22_error` varchar(100) NULL,
      `23_error` varchar(100) NULL,  `24_error` varchar(100) NULL,
      `25_error` varchar(100) NULL,  `26_error` varchar(100) NULL,
      `27_error` varchar(100) NULL, `28_error` varchar(100) NULL,
      `29_error` varchar(100) NULL, `30_error` varchar(100) NULL)";
	$db->exec($sql);
	$db->close();

  }

function insert_error($phone, $count_error, $string_error){
	// code...
	$db = new MyDB();
	$sql= "INSERT INTO source (phone, count_error, string_error) VALUES ('$phone', '$count_error', '$string_error')";
	//echo $sql;
	//echo "\n";
	$db->exec($sql);
	$db->close();
}
function insert_ids($phone, $date){
	// code...
	$db = new MyDB();
	$sql= "INSERT INTO ids (phone, string_error) VALUES ('$phone', '$date')";
	#echo $date;
	//echo "\n";
	$db->exec($sql);
  $id = $db->lastInsertRowId();
	$db->close();
  return $id;
}

function update_ids($id, $ids, $count, $date){
  // code...
  $set = $count.'_error';
  $sql = "update ids set '$set' = '$ids' where id = '$id'";
  $db = new MyDB();
  $db->exec($sql);
	$db->close();
}
function select_db($phone, $count, $date){
  // code...
  $set = $count.'_error';
  $end_date = $date-6;
  $sql = "select `$set` from ids where phone='$phone' and string_error BETWEEN '$end_date' and '$date'";
  #echo $sql;
  $db = new MyDB();
	$db->exec($sql);
  $result = $db->query($sql);
  $status = $result->fetchArray();
  #var_dump($status[0]);
  #if($status === TRUE){
  #  var_dump($status);
  #}

  if(is_bool($status)){
    $end_date = $date-15;
    $sql = "select `$set` from ids where phone='$phone' and string_error BETWEEN '$end_date' and '$date'";
    $db->exec($sql);
    $result = $db->query($sql);
    $status = $result->fetchArray();
    if(is_bool($status)){
      var_dump($status);
      echo "\n";
      var_dump($sql);
    }
  }
  $db->close();
  return $status[0];
}
function select_rov($phone, $date){
  // code...
  $sql = "SELECT * from ids where phone = '$phone' and string_error BETWEEN '$date' and '$date +=6'";
  $db = new MyDB();
	$db->exec($sql);
  $result = $db->query($sql);
  $status = $result->fetchArray();
#  if($status === FALSE){
#    $status[0]='не найдено';
#    echo "алярма\n";
#  }
	$db->close();
  return $status;
}
