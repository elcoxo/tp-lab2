function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

let btns = document.querySelectorAll(".productContainer button")
let btn_delete = document.querySelectorAll(".item button")

btns.forEach(btn=>{
    btn.addEventListener("click", addToCart)
})
btn_delete.forEach(btn=>{
    btn.addEventListener("click", deleteItem)
})

function addToCart(e){
    let product_id = e.target.value
    let url = "/add_to_cart"

    let data = {id:product_id}

    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        document.getElementById("num_of_items").innerHTML = data
        console.log(data)
    })
    .catch(error=>{
        console.log(error)
    })
}
function deleteItem(e){
    let product_id = e.target.value
    let url = "/delete_item/${product_id}"

    let data = {id:product_id}

    console.log(csrftoken)

    fetch(url, {
        method: "DELETE",  // Используем метод DELETE
        headers: {"Content-Type": "application/json", 'X-CSRFToken': csrftoken},
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("num_of_items").innerHTML = data
        console.log(data)
    })
    .catch(error => {
        console.log(error)
    })
}