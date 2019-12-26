<?php
require_once 'conf.php';
function readdata($file){
  $load = file_get_contents($file);
  $line = explode("\n", $load);
  #var_dump($line);
  return $line;
}
function save_phone($date){
  // code...

  $match = '/(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).\d{1,}.{1,}клиенту (\d{11,12}) отправлено: \{.{1,}failure":(\d{1,}).{1,}\[(.{0,}\{"error":"\w{1,}"\}.{0,})\]/';

    // code...
    preg_match_all($match, $date, $list);
    if(!empty($list[0])){
     $arr_err = serialase_ids($list[4][0]);
    $date = strtotime($list[1][0]);
    find_error($arr_err, $list[2][0], $date);
  }
  return true;
}
function find_error($arr_err, $phone, $date){
  // code...
  $count = 1;
  foreach ($arr_err as $value) {
    // code...

    $match = '/("error":"NotRegistered|"error":"MismatchSenderId")/';
    preg_match_all($match, $value, $list);
    if(!empty($list[0])){
      $ids_source = select_db($phone, $count, $date);
      $count++;
      $status = 1;
      insert_log($phone, $ids_source, $date, $status);
    }
    else {
      $ids_source = select_db($phone, $count, $date);
      $count++;
      $status = 0;
      insert_log($phone, $ids_source, $date, $status);
    }
  }
}
function save_ids($list){
  // code...
  $date = strtotime($list[1][0]);
  $secund = $date;
   $id = insert_ids($list[2][0], $date);
#   echo $id;
   $arr_ids = serialase_ids($list[3][0]);
   $count = 1;
   foreach ($arr_ids as $ids) {
     // code...
    update_ids($id, $ids, $count, $date);
     $count ++;
   }
}
function read_ids($file){
  // code...
  $open_file = readdata($file);
  $match = '/(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{1,3}).{1,}для клиента (\d{11,12}).{1,}\[(.{1,})\]/';
  foreach ($open_file as $value) {
    // code...
    preg_match_all($match, $value, $list);
   if(!empty($list[0])){
      save_ids($list);
    }
   else {
     // code...
     save_phone($value);

   }
  }
}
function serialase_ids($ids){
  // code...
  $date=explode(',', $ids);
  return $date;
}
function load_file(){
	// code...
  $arr_file_name = scandir('file/');
  foreach ($arr_file_name as $file_name){
  	// code...
  	#echo $file_name;
  	$file='file/'.$file_name;
  	#echo $file;
  	if (($file != 'file/.') && ($file != 'file/..')){
  		// code...
      var_dump($file);
    read_ids($file);
    }}
}
function parser_file($file){
  // code...
  read_ids($file);
  #save_error($file);
}
