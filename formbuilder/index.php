<?php
if (count($_POST)>0){
  $csv = implode(', ', $_POST);
  $handle = fopen('list.txt', 'a');
  fwrite($handle, $csv.PHP_EOL);
  fclose($handle);
}
if (!empty($_GET['clear'])) {
  $handle = fopen('list.txt', 'w');
  fwrite($handle, "");
  fclose($handle);

}
?>
<h1> Form Builder</h1>
<form action="index.php" method="POST">
  Type: <input type="text" name = "type"> <br>
  Name: <input type="text" name = "name"> <br>
  Label: <input type="text" name ="label"> <br>
  <br><input type="submit" value="submit">

</form>

<form>
  <form action="index.php" method="GET">
    <input type="hidden" name="clear_form" value="true">
    <input type="submit" value="Clear form">
</form>

<form action="form.php">
  <input type="submit" value="View Form">
</form>
