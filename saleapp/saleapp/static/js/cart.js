function addToCart(id, name, price) {
        fetch('/api/cart', {
        method: "post",
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => res.json()).then((data) => {
        console.info(data)
        let d = document.getElementsByClassName("cart-counter")
        for (let i = 0; i < d.length; i++)
            d[i].innerText = data.total_quantity
    })
}

function updateCart(product_id, obj){
    fetch(`/api/cart/${product_id}`, {
        method: "put",
        body: JSON.stringify({
            "quantity": obj.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => res.json()).then((data) => {
        console.info(data)
        let d = document.getElementsByClassName("cart-counter")
        for (let i = 0; i < d.length; i++)
            d[i].innerText = data.total_quantity

        let a = document.getElementsByClassName("cart-value")
        for (let i = 0; i < a.length; i++)
            a[i].innerText = data.total_value.toLocaleString("en-US")
    })
}

function deleteCart(product_id){
    fetch(`/api/cart/${product_id}`, {
        method: "delete",
    }).then(res => res.json()).then((data) => {
        console.info(data)
        let d = document.getElementsByClassName("cart-counter")
        for (let i = 0; i < d.length; i++)
            d[i].innerText = data.total_quantity

        let a = document.getElementsByClassName("cart-value")
        for (let i = 0; i < a.length; i++)
            a[i].innerText = data.total_value.toLocaleString("en-US")

        let c = document.getElementById(`cart${product_id}`)
        c.style.display = "none"
    })
}