<?php 

session_start();

if (isset($_SESSION['reset_token'])) {

?>

<html>

    <head>
        <title>Create Account</title>
        <link rel="stylesheet" href="style.css">
        <?php
            echo '<link rel="shortcut icon" href="gg.png" type="image/x-icon" />';
        ?>
    </head>
    
    <body>
        <div class="">
            <div class="">
                <h2>Reset Password</h2>

                    <form action="reset_password_process.php" method="post">

                        <?php if (isset($_GET['error'])) { ?>

                            <p class="error"><?php echo $_GET['error']; 
                                if($_GET['error']=="Password Reset Successful"){
                                unset($_SESSION['reset_token']);
                                }
                            ?></p>

                        <?php } ?>

                        <p>
                            <input type="text" id="username" name="password" placeholder="Password" required>
                        </p>
                        <p>
                            <input type="password" id="password" name="confirm" placeholder="Confirm Password" required>
                        </p>
                        <p>
                            <input type="submit" id="login" value="Reset Password">
                        </p>
                    </form>
                <div id='#'>
                    <p><a href="login.php">Login</a><p>
                    <p><a href="index.php">Back to home page</a><p>
                </div><!--create-account-wrap-->
            </div><!--login-form-wrap-->
        </div>
    </body>

</html>

<?php 

}else{

     header("Location: forget_password.php");

     exit();

}

?>