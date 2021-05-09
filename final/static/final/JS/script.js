var link1 = (window.location.href == "http://127.0.0.1:8000/checkout/")
var link2 = (window.location.href == "http://127.0.0.1:8000/cart/")
var link3 = (window.location.href == "http://127.0.0.1:8000/register/")
var link4 = (window.location.href == "http://127.0.0.1:8000/delete/")
var link6 = (window.location.href == "http://127.0.0.1:8000/")
var link8 = (window.location.href == "http://127.0.0.1:8000/meals/")


if( link2 || link3)
{   
    var val = document.body.offsetHeight;
    var offsetHeight = document.getElementById('2').offsetHeight;

    document.getElementById('bottom').style.marginTop = offsetHeight + "px";

}
if(link1)
{
  
  var offsetHeight1 = document.getElementById('1').offsetHeight;
  var offsetHeight2 = document.getElementById('2').offsetHeight;

  document.getElementById('bottom').style.marginTop = offsetHeight1 + offsetHeight2 + "px";
	
}

if( link4)
{   
    var val = document.body.offsetHeight-800;

    document.getElementById('bottom').style.marginTop = val + "px";

}

// Display search in navbar for meals site
if(link8)
{   
    if(window.innerWidth <= 866 ){
        //don't display search option on mobile
      }else{
        document.getElementById('my-filter').style.display = "";
      }
}

//for meal
if(window.location.href.includes("meal/")){

  var offsetHeight = document.getElementById('2').offsetHeight;

  document.getElementById('bottom').style.marginTop = offsetHeight/5 + "px";

}
