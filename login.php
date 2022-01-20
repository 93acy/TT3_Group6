<!DOCTYPE html>
<html lang="en" >
<head>

  <meta charset="UTF-8">
  <title>Login</title>
  <link rel="stylesheet" href="style.css">
    <?php
            echo '<link rel="shortcut icon" href="gg.png" type="image/x-icon" />';
    ?>

</head>

<body>
    <div class="">
        <div class="">
            <h2>Login</h2>

                <form action="checkprocess.php" method="post">

                    <?php if (isset($_GET['error'])) { ?>

                        <p class="error"><?php echo $_GET['error']; ?></p>

                    <?php } ?>

                    <p>
                        <input type="text" id="username" name="uname" value="<?php if(isset($_COOKIE['username'])){echo $_COOKIE['username'];}?>" placeholder="Username" required>
                    </p>
                    <p>
                        <input type="password" id="password" name="password" value="<?php if(isset($_COOKIE['username'])){echo $_COOKIE['username'];}?>" placeholder="Password" required>
                    </p>
                    <p><input type="checkbox" name="remember" value="Yes" /> Remember Me</p>
                    <p>
                        <input type="submit" id="login" value="Login">
                    </p>
                </form>
            <div id='#'>
                <p>Forget your password? Reset <a href="forget_password.php">HERE</a><p>
                <p>Not a member? <a href="create_account.php">Create Account</a><p>
                <p>Go back to home page <a href="index.php">Back</a><p>
            </div><!--create-account-wrap-->
        </div><!--login-form-wrap-->
    </div>
<!-- partial -->
</body>

</html>