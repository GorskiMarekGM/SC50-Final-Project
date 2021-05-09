function get_posts(mealId){

//document.querySelector('.meal').innerHTML = '';

fetch('/all_meals/'+ mealId)
    .then(response => response.json())
    .then(data => {
    console.log(data)
        document.querySelector('.name').innerHTML = `
            <h2>${data.name}</h2>`;

        document.querySelector('.totalPrice').innerHTML = `
            ${data.price} zł`;

        if(data.size!=null)
        {
            if(data.meal_type=='Pizza')
            {
                document.querySelector('.size').style.visibility="visible";
            }

        }

        if((data.description != null)&&(data.description!="None") )
        {   
            try {
                document.querySelector('.info').innerHTML = `
                <h3>${data.description}</h3><hr>`;
            } catch (error) {
                
            }
        }
    });
}

function get_ingredients(mealId){
    var obj;
    var i=0;

    fetch('/ingredients/'+ mealId)
    .then(response => response.json())
    .then(data => obj = data)
    .then(() => console.log(obj))
    .then(() => obj.forEach(() => {
        document.querySelector('.ingredients').innerHTML += `<li>${obj[i].name}</li>`;
        i++;
    }))
    .then(() => {document.querySelector('.ingredients').innerHTML += `<hr>`;})

}

function load_meal_details(meal_id){
    get_posts(meal_id);
    get_ingredients(meal_id);

}

function get_option(){
    document.addEventListener('DOMContentLoaded', function() {
        var e = document.getElementById('sizeSelect');
        var value=e.value;// get selected option value.
        console.log('value '+value);
    });
}
function option_change(mealId){
    
    document.getElementById('sizeSelect').onchange = function() {
        var newId
        console.log("value changed")
        //get size from option
        var value = document.getElementById('sizeSelect').value;
        console.log("Val"+ value);
        //get new pizza from API
        
        fetch('/pizza_api/'+mealId+'/'+value)
        .then(response => response.json())
        .then(data => {

            get_posts(data.id);
            newId = data.id
            // console.log('newID '+newId)
            document.getElementById('add').dataset.product = newId;
            // console.log('Dataset ' + document.getElementById('add').dataset.product)

            return newId
        });

    };
    
}
function get_by_size(id, val)
{
    fetch('/pizza_api/'+ id + val)
    .then(response => response.json())
    .then(data => {
    console.log("New Pizza ID:"+data.id)
    });
    
}
