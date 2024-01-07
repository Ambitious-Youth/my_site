msg = """
        body {
  background-color: #cccccc;
  background-image: linear-gradient(red, yellow, green);
}

h1 {
  color: blue;
}
p {
    
    font-style: italic;
    color: black;
}



.head {
    background-color:silver;
    text-align: center;
    padding: 10px 16px;
    font-size: 100%;    
    }
    
    h3 {
        text-align: center;
}

#myTopnav {
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
}
        

/* Add a black background color to the top navigation */
.topnav {
  background-color: #333;
  overflow: hidden;
}

/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  display: block;
  color: #f3f3f3;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #fff;
  color: gray;
}

/* Add an active class to highlight the current page */
.topnav a.active {
  background-color: #04AA6D;
  color: white;
}

/* Hide the link that should open and close the topnav on small screens */
.topnav .icon {
  display: none;
}

/* When the screen is less than 600 pixels wide, hide all links, except for the first one ("Home"). Show the link that contains should open and close the topnav (.icon) */
@media screen and (max-width: 600px) {
  .topnav a:not(:first-child) {display: none;
  }
  .topnav a.icon {
    float: right;
    display: block;
  }
}

/* The "responsive" class is added to the topnav with JavaScript when the user clicks on the icon. This class makes the topnav look good on small screens (display the links vertically instead of horizontally) */
@media screen and (max-width: 600px) {
  .topnav.responsive {position: relative;
  }
  .topnav.responsive a.icon {
    position: absolute;
    right: 0;
    top: 0;
  }
  .topnav.responsive a {
    float: none;
    display: block;
    text-align: center;
    
  }
}


img{  
    position: fixed;
    height: 75%;
    width: 20%;
    margin-left: 1px;
    margin-bottom: 10%;

}

article{
    margin-left: 22%;
    padding: 16px;
}

.sticky {
  position: fixed;
  top: 0;
  width: 100%;
}

.sticky + article {
  padding-top: 102px;
}

.footer{
    background-color: blue;
    text-align: center;
    padding: 8px;
    width: 100% 
    bottom: 0;
    position: fixed;
    }

"""

with open('styles.css', 'w') as web:
    msg2 = web.write(msg)
print(msg2)
