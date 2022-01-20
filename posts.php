<?php

    include "connect.php";

    $post_get = "SELECT * FROM post";
    $select = mysqli_query($conn,$post_get);
    $num_rows = mysqli_num_rows($select);
    if ($num_rows > 0) {

        while ($rows = mysqli_fetch_array($select, MYSQLI_ASSOC)) {
            echo "<div>";
            echo "<h3>" . $rows['Post_title'] . "</h3>";
            echo "<p>" . $rows['Post_Description'] . "</p>";
            ?>

            <p>
            <img src="<?php echo $rows['Post_image']; ?>">
            </p>

            <p>-------------------------------------------</p>
            <?php
            echo "</div>";
        }

    }elseif($num_rows == 0){
        echo "<p>No Posts Yet</p>";
    }
?>