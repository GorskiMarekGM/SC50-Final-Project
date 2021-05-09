var upadteBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < upadteBtns.length; i++){
    upadteBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productID:', productId, 'action:',action)

        console.log('USER:',user)
        if(user === 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log('Not logged it..')
    console.log(cart[productId])

    // ADDing elements to cart
    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }else{
            cart[productId]['quantity'] += 1
        }
    }
    //Removing elements from cart
    if(action == 'remove'){
        cart[productId]['quantity'] -= 1

        if(cart[productId]['quantity']<=0){
            console.log('Remove Item')
            delete cart[productId]
        }
    }
    //Delete all items of that type
    if(action == 'delete'){
        delete cart[productId]
    }
    
    //Override cookie
    console.log('Cart:',cart)
    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    
    if(action == 'add'){
        orderedPopUp(productId)
    }else{
        location.reload()
    }
}

function updateUserOrder(productId, action){
    
    console.log('User is logged sending data')

    var url = '/update_item/'

    //sending data to view
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        // data send to backend in body
        body:JSON.stringify({'productId': productId, 'action':action})
    })
    //return promise
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)

        //TODO: Dynamic way, without reloading page
        // location.reload()
        if(action == 'add'){
            orderedPopUp(productId)
        }else{
            location.reload()
        }
    });

}   