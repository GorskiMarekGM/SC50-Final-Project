   
//Script to handle onclick events on each card in order to display proper website

document.addEventListener('DOMContentLoaded', () => {
    click()
});

function click(){

    const list = document.querySelectorAll('.card');
    var meal = document.querySelectorAll("div.card");


    for (let i = 0; i < list.length; i++) {
        const article = list[i];

        list[i].addEventListener('click', event => {

            if(event.target.classList.contains('btn-outline-secondary'))
            {}
            else{
                var meal_id = meal[i].dataset.id
                location.href = "{% url 'meal' 123 %}".replace('123', meal_id);
            }
        });

    }
}
    