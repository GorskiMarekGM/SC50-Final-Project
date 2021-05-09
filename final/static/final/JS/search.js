function searchFunction() {
    var input, filter, cards, cardContainer, h5, title, i;
    
    Element.prototype.remove = function() {
        this.parentElement.removeChild(this);
    }
    NodeList.prototype.remove = HTMLCollection.prototype.remove = function() {
        for(var i = this.length - 1; i >= 0; i--) {
            if(this[i] && this[i].parentElement) {
                this[i].parentElement.removeChild(this[i]);
            }
        }
    }

    if(window.innerWidth <= 866 ){
        input = document.getElementById("my-filter-mobile");
        select = document.querySelector('.search');
        document.querySelector('.meals-nav').removeChild(select);

      }else{
        input = document.getElementById("my-filter");
      }


    filter = input.value.toUpperCase();
    cards = document.getElementsByClassName("card");
    
    document.querySelector('.posts-container').style.paddingTop = "5em";


    // cards names none
    let myNames = document.querySelectorAll(".meal-name");

    for (let i = 0; i < myNames.length; i++) {
        myNames[i].style.display = "none";
    }

    var results = 0;
    console.log("length" + cards.length)
    for (i = 0; i < cards.length; i++) {
        title = cards[i].querySelector(".card-body h4.card-title");
        if (title.innerText.toUpperCase().indexOf(filter) > -1) {
            cards[i].style.display = "";
            results = results+1;
            console.log("results"+results)
        } else {
            cards[i].style.display = "none";
        }
    }

    if(results==0)
    {
        message = document.querySelector('.message').innerHTML = `<div id="mess">0 results</div>`

        document.querySelector('#mess').style.width="100%";
        document.querySelector('#mess').style.height="18em";
        document.querySelector('#mess').style.textAlign="center";
        document.querySelector('#mess').style.fontSize="45px";
        document.querySelector('#mess').style.margin="45%";
    }else
    {   
        document.querySelector('.message').innerHTML = ""
    }
}

function mobileSearch() {
    
    var input, filter, cards, title, i;
    input = document.getElementById("my-filter-mobile");
    filter = input.value.toUpperCase();
    console.log("input"+input.value)
    cards = document.getElementsByClassName("card");
    // nav = document.querySelector('.meals-nav').style.display="none";
    document.querySelector('.posts-container').style.paddingTop = "5em";
    document.querySelector('.mobile-search').style.display="none";
    // document.querySelector('.all').style.paddingTop="25em";


    // cards names none
    let myNames = document.querySelectorAll(".meal-name");

    for (let i = 0; i < myNames.length; i++) {
        myNames[i].style.display = "none";
    }

    var results = 0;
    console.log("length" + cards.length)
    for (i = 0; i < cards.length; i++) {
        title = cards[i].querySelector(".card-body h4.card-title");
        // console.log(title)
        if (title.innerText.toUpperCase().indexOf(filter) > -1) {
            cards[i].style.display = "";
            results = results+1;
            // console.log("results"+results)
        } else {
            cards[i].style.display = "none";
        }
    }

    if(results==0)
    {
        message = document.querySelector('.message').innerHTML = `<div id="mess">0 results</div>`

        document.querySelector('#mess').style.width="100%";
        document.querySelector('#mess').style.height="18em";
        document.querySelector('#mess').style.textAlign="center";
        document.querySelector('#mess').style.fontSize="45px";
        document.querySelector('#mess').style.margin="45%";
    }else
    {   
        document.querySelector('.message').innerHTML = ""
    }
}