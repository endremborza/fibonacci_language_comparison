<?php
function fib($n) {
    if($n < 2){
        return(1);
    }else{
        return(fib($n-1) + fib($n-2));
    }
}


for ($x = 0; $x < 41; $x++) {
    echo fib($x);
    echo "\n";
} 

?>
