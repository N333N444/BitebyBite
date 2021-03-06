<html>
<head>
    <link rel="stylesheet" href="../Css/Log_in.css">
    <link rel="stylesheet" href="../Css/Navigation_menu.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>Log in</title>
    <meta content="width=device-width, initial-scale=1" name="viewport" />
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
</head>
<body>
    <div class="index">
        <ul id="Navigation_desktop">
            <div class="Navbar_left">
                <li><a href="../index.html"><img src="../Pictures/index/leeg_logo.png" class="Logo"></a></li>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../HTML/Recipes.html">Products</a></li>
                <li><a href="../HTML/Dishes.html">Dishes</a></li>
                <li><a href="../HTML/About_us.html">About us</a></li>
            </div>
            <div class="Navbar_right">
                <li style="float:right;"><a class="Navigation_desktop_active" href="Log_in.php">Log in</a></li>
                <!-- <li style="float:right;"><a href=""><img src="../Pictures/index/Basic_profilepicture.png" class="Avatar"></a></li>                                         Moet worden aangepast als je bent ingelogd bent-->
                <li style="float: right;"><a href="" class="Shopping_cart"><i class='fa fa-shopping-cart' style='color:#939393; font-size: 30px; margin-top: 4px;'></i></a></li>
                <li style="float: right;">
                    <form action="action.php" class="Search" >
                        <input type="text" placeholder="Search" class="Search_bar">
                        <button type="submit"><i class="fa fa-search" aria-hidden="true"></i>
                        </button>
                    </form>
                </li>
            </div>
        </ul>
        <div id="Navigation_mobile">
            <a href="javascript:void(0);" class="icon hamburgericon" onclick="showTHINGIEYESPLEASAE()">
                <i class="fa fa-bars"></i></a>
                <a class="On_hover_off">Home</a>
                <div class="Shopping_cart_mobile">   
                    <a href="" class="Shopping_cart_mobile"><i class='fa fa-shopping-cart' style='color:#939393;'></i></a>
                </div>
                <div class="Avater_mobile">
                    <a href="" class="Avatar_mobile"><img src="Pictures/index/Basic_profilepicture.png" alt="Profiel foto"></a>
                </div>

            <script>
                function showTHINGIEYESPLEASAE(){
                var menu = document.getElementById('linkies')
                if (menu.style.display === 'block'){
                    menu.style.display = 'none';
                } else {
                    menu.style.display = 'block'
                    }
                }
            </script>
        
        </div>
        <div id="linkies">
            <li><a href="../HTML/Recipes.html">Recipes</a></li>
            <li><a href="../HTML/Dishes.html">Dishes</a></li>
            <li><a href="../HTML/About_us.html">About us</a></li>
        </div>
    </div>
    <div class="Login_menu">
        <div class="Log_in_form">
            <div class="Switch_button_box">
                <div id="Switch_button"></div>
                <button type="button" class="Switch" onclick="Login()">Log in</button>
                <button type="button" class="Switch" onclick="Register()">Register</button>
            </div>
            <div id="Second_box">
                <div id="Second_switch_button"></div>
                <button type="button" class="Switch" onclick="Personal()">Personal</button>
                <button type="button" class="Switch" onclick="Company()">Company</button>
            </div>
            <form id="Log_in_id" class="Log_in">
                <input type="text" class="Text_field" placeholder="Email" required>
                <input type="text" class="Text_field" placeholder="Password" required>
                <button type="submit" class="Submit_log_in">Log in</button>
            </form>
            <form id="Register_id" class="Log_in">
                <input type="text" class="Text_field" placeholder="Full name" required>
                <input type="email" class="Text_field" placeholder="Email" required>
                <input type="text" class="Text_field" placeholder="Password" required>
                <input type="text" class="Text_field" placeholder="Repeat password" required>
                <button type="submit" class="Submit_log_in">Register</button>
            </form>
            <form id="Register_id_company" class="Log_in">
                <input type="text" class="Text_field" placeholder="Company name" required>
                <input type="email" class="Text_field" placeholder="Company Email" required>
                <input type="text" class="Text_field" placeholder="Password" required>
                <input type="text" class="Text_field" placeholder="Repeat password" required>
                <button type="submit" class="Submit_log_in">Register</button>
            </form>
        </div>
    </div>

    <script>
        var x = document.getElementById("Log_in_id");
        var y = document.getElementById("Register_id");
        var z = document.getElementById("Switch_button");
        var d = document.getElementById("Second_box");
        var b = document.getElementById("Register_id_company");
        var c = document.getElementById("Second_switch_button");

        function Register(){
            x.style.left = "-450px";
            y.style.left = "50px";
            z.style.left = "110px";
            d.style.left = "0px";
        }

        function Login(){
            x.style.left = "50px";
            y.style.left = "500px";
            z.style.left = "0";
            d.style.left = "500px";
            b.style.left = "500px";
            c.style.left = "0px"
        }
    
        function Personal(){
            y.style.left = "50px";
            b.style.left = "500px";
            c.style.left = "0px";
        }

        function Company(){
            y.style.left = "500px";
            b.style.left = "50px";
            c.style.left = "110px";
        }
    </script>
</body>
</html>