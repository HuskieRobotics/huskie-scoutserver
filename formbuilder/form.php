
<h1> Form </h1>

<form action="list.txt" method="POST">
  <?php
  $readin = file('list.txt');
  foreach ($readin as $fname){
    $entryArray = explode(',', $fname);
    echo $entryArray[2].': <input type ="'.$entryArray[0].'" name = "'.$entryArray[1].'" > <br>';
    //echo 'Label: <input type="text" name ="label"> ';

  }

  ?>

</form>
<form action="index.php">
  <input type="submit" value="Return to Formbuilder">
</form>
