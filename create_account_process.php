<?php 

session_start(); 

include "connect.php";

if (isset($_POST['name']) && isset($_POST['uname']) && isset($_POST['password'])) {

    function validate($data){

       $data = trim($data);

       $data = stripslashes($data);

       $data = htmlspecialchars($data);

       return $data;

    }

    $name = validate($_POST['name']);

    $uname = validate($_POST['uname']);

    $email = validate($_POST['email']);

    $pass = validate($_POST['password']);

    if (empty($uname)) {

        header("Location: create_account.php?error=Username is required");

        exit();

    }else if(empty($pass)){

        header("Location: create_account.php?error=Password is required");

        exit();

    }else if(empty($email)){

        header("Location: create_account.php?error=Email is required");

        exit();

    }else if(empty($name)){

        header("Location: create_account.php?error=Name is required");

        exit();

    }else{

        $sql = "SELECT * FROM accounts WHERE username='$uname'";
        $result = mysqli_query($conn, $sql);

        if (mysqli_num_rows($result) === 1) {
            header("Location: create_account.php?error=User already exists");
            exit();
        }else{
            $insert = "INSERT INTO accounts "."(name, username, email, password) "."VALUES ".
            "('$name','$uname', '$email','$pass')";
            if (mysqli_query($conn, $insert)) {
                header("Location: create_account.php?error=Account created successfully");
            }
        }
    }
}