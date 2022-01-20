<?php 

session_start(); 

include "connect.php";

if (isset($_POST['uname']) && isset($_POST['password'])) {

    function validate($data){

       $data = trim($data);

       $data = stripslashes($data);

       $data = htmlspecialchars($data);

       return $data;

    }

    $uname = validate($_POST['uname']);

    $pass = validate($_POST['password']);

    if (empty($uname)) {

        header("Location: login.php?error=User Name is required");

        exit();

    }else if(empty($pass)){

        header("Location: login.php?error=Password is required");

        exit();

    }else{

        $sql = "SELECT * FROM accounts WHERE username='$uname' AND password='$pass'";

        $result = mysqli_query($conn, $sql);

        if (mysqli_num_rows($result) === 1) {

            $row = mysqli_fetch_assoc($result);

            if ($row['username'] === $uname && $row['password'] === $pass) {

                $_SESSION['username'] = $row['username'];

                $_SESSION['name'] = $row['name'];

                $_SESSION['id'] = $row['id'];

                setcookie('username',$row['username'],time() + (86400 * 15), "/");
                setcookie('password',$row['password'],time() + (86400 * 15), "/");

                if(isset($_POST['remember']) && $_POST['remember'] == 'Yes'){
                    $hash_id = password_hash($row['id'],PASSWORD_DEFAULT, array('cost' => 9));
                    setcookie('remember_me',$hash_id,time() + (86400 * 5), "/");
                }

                if($_SESSION['username'] === 'admin' && $_SESSION['name'] === 'Johnny' && $_SESSION['id'] = '1'){

                    header("Location: admin_home.php");

                    exit();

                }else{

                header("Location: index.php");

                exit();
                }

            }else{

                header("Location: login.php?error=Incorrect Username or password");

                exit();

            }

        }else{

            header("Location: login.php?error=Incorrect Username or password");

            exit();

        }

    }

}else{

    header("Location: login.php");

    exit();

}