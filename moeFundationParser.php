<?php
    $fileName = "fundation.csv";
    $file = fopen($fileName,"r");
    print_r(fgetcsv($file));
    fclose($file);
?>