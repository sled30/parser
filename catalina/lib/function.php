<?php
require_once 'conf.php';
function readdata($file){
  $load = file_get_contents($file);
  $line = explode("\n", $load);
  #var_dump($line);
  return $line;
}
function save_error($file){
  // code...
  $open_file = readdata($file);
  $match = '/(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).\d{1,}.{1,}клиенту (\d{11,12}) отправлено: \{.{1,}failure":(\d{1,}).{1,}\[(.{0,}\{"error":"\w{1,}"\}.{0,})\]/';

  foreach ($open_file as $value) {
    // code...
    preg_match_all($match, $value, $list);
    if(!empty($list[0])){
     #var_dump($list[4][0]);
     #insert_error($list[1][0], $list[2][0], $list[3][0]);
     $arr_err = serialase_ids($list[4][0]);
    # var_dump($arr_err);
    # echo "\n";
    #select_db($list[1][0]);
    $date = strtotime($list[1][0]);
    find_error($arr_err, $list[2][0], $date);
    }
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
      write_report($phone, $ids_source, $date);
      /*  if(!isset($id)){
        $id = $ids_source;
      }
      else{
        $id =$id.", ".$ids_source;
      }
      write_report($phone, $id);
  */  }
  else {
    $ids_source = select_db($phone, $count, $date);
    $count++;
    write_succes($phone, $ids_source, $date);
  }
    #var_dump($id);
  }
}
function write_succes($phone, $string, $date){
  // code...
  $fp = fopen('succes.csv', 'a+');
  fputs($fp, $date." ");
  fputs($fp, $phone." ");
  fputs($fp, $string."\n");
  fclose($fp);
}
function write_report($phone, $string, $date){
  // code...
  $fp = fopen('out.csv', 'a+');
  fputs($fp, $date." ");
  fputs($fp, $phone." ");
  fputs($fp, $string."\n");
  fclose($fp);
}

function read_ids($file){
  // code...
  #$list[1] телефон
  #$list[2] список ids
  $open_file = readdata($file);
  #var_dump($open_file);
  $match = '/(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{1,3}).{1,}для клиента (\d{11,12}).{1,}\[(.{1,})\]/';
  foreach ($open_file as $value) {
    // code...
    preg_match_all($match, $value, $list);
  #  var_dump($list);
   if(!empty($list[0])){
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
  }
}
function replace_date($date){
  // code...
  return substr_replace($date, null, 0, 3);
}
function secund($data){
  // code...
  $line = explode(":", $data);
  return $line[2];
}
function corect_data($data){
  // code...
  $line = explode(".", $data);
  #echo $line[0];
  return $line[0];
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
    parser_file($file);
    }}
}
function parser_file($file){
  // code...
  echo 1;
  read_ids($file);
  save_error($file);
}
