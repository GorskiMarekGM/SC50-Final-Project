function samePage(){
    location.reload()
}

function orderedPopUp(mealId){
    var menu = "http://127.0.0.1:8000/meals/"
    var cart2 = "http://127.0.0.1:8000/cart/"
    
    // location.reload()
    // location.href = '#popup'
    var popup = document.querySelector('.popup')
    var overlay = document.querySelector('.overlay')
    console.log("overlay"+overlay)

    overlay.style.visibility = "visible";
    overlay.style.opacity = 1;

    fetch('/all_meals/'+ mealId)
    .then(response => response.json())
    .then(data => {
    console.log(data)
        popup.innerHTML = `
            <h3>Added to cart!</h3>
            <a class="close" onclick="samePage()">&times;</a>
            <div class="content">
                <div class="container cont-pop">
                    <div class="row row-pop">
                        <div class="col-sm-12 col-md-6">
                            <div id="photoURL">
                                <img class="img" src="${data.imageURL}" >
                            </div>
                        </div>
                        <div class="col-sm-12 col-md-6 nice-font" ><h3>${data.name}</h3> <br>
                        <h4>${data.price} zł </h4>
                        <div id="description"></div>
                        </div>
                    </div></div>
                    <div class="row row-pop">
                        <div class="col-sm-12 col-md-6"><a href="${menu}" class="btn-mobile-red nice-font full-width-btn">Menu</a></div>
                        <div class="col-sm-12 col-md-6"><a href="${cart2}" class="mmargin btn-mobile-red nice-font full-width-btn">Cart</a></div>
                    </div>
                </div>
            </div>`;
            if((data.description != null)&&(data.description!="None") )
            {
                document.getElementById('description').innerHTML += `
                <h5>${data.description}</h5><hr>`;
            }
            if(window.location.href.includes("/meal/"))
            {
                document.getElementById('photoURL').innerHTML = `
                    <img class="img" src="../${data.imageURL}" >
                `
            }
    });

}
