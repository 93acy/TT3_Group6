<?php
    include "connect.php";
    $list = "SELECT * FROM orders_1";
    $result = mysqli_query($conn, $list);
    $times = mysqli_num_rows($result);
    $sale_total = 0;
    $sale_in_15_days = 0;
    $order_no_in_15_days = 0;
    $order_no = 0;
    for ($i = 0; $i < $times; $i++) {
        if ($rows = mysqli_fetch_row($result)) {
            $sale_total += $rows[5];
            $date = date("Y-m-d");
            $order_no += 1;
            if ($date <= $rows[2]){
                $sale_in_15_days += $rows[5];
                $order_no_in_15_days += 1;
            }
        }
    }
?>
<div>
    <h2>Summary</h2>
</div>    
<div>
    <h3>Total</h3>
    <p>Sale total : $<?php echo $sale_total; ?></p>
    <p>Total Orders : <?php echo $order_no; ?></p>
</div>
<div>
    <h3>In 15 Days</h3>
    <p>Sale in 15 days : $<?php echo $sale_in_15_days; ?></p>
    <p>Orders in 15 days : <?php echo $order_no_in_15_days; ?></p>
</div>