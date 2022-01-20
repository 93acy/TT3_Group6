<?php
    include "connect.php";

    session_start();

    if ($_POST['password'] == $_POST['confirm']){
        $password = $_POST['password'];
        $user_id = $_SESSION['reset_token'];
        $update = "UPDATE accounts SET password ='$password' WHERE id='$user_id'";
        $result = mysqli_query($conn, $update) or die($conn->error);

        if (mysqli_query($conn, $update)) {
            header("Location: reset_password.php?error=Password Reset Successful");
            exit();
        }
    }else{
        header("Location: reset_password.php?error=Passwords are not the same");
        exit();
    }
?>