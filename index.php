<?php
    include_once "remember_me.php"
?>
<html>

    <head>
        <title>Home Page</title>
        <link rel="stylesheet" href="style.css">
        <?php
            echo '<link rel="shortcut icon" href="gg.png" type="image/x-icon" />';
        ?>
    </head>
    
    <body>
        <div class="">
            <div class="">
                <h1>Home Page</h1>

                <?php session_start();
                    if (!isset($_SESSION['id']) and !isset($_SESSION['username'])) { ?>
                    <h3>Please Login to browse Items available today.</h3>
                    <p>Not a member? <a href="create_account.php">Create Account</a><p>
                    <p>Already have an account? <a href="login.php">Login</a><p>
                        <?php }else{ ?>
                            <p><b>Logged in user <?php echo $_SESSION['name']; ?></b></p>
                            <p><a href="profile.php">Profile</a> | <a href="logout.php">Logout</a></p>
                            
                <?php 
                    include "posts.php";}
                ?>
            </div>
        </div>
    </body>

</html>