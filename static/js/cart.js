let updateBtns = document.querySelectorAll(".update-cart");

updateBtns.forEach(function (btn) {
  btn.addEventListener("click", function () {
    let productId = this.dataset.product
    let action = this.dataset.action
    console.log('productId:', productId, "Action:", action)
    console.log("User", user)
    if (user === "AnonymousUser") {
      addCookieItem(productId, action);
    } else {
      updateUserOrder(productId, action);
    }
  });
});


function addCookieItem(productId, action) {
  console.log('User is not authenticated');  

  if (action == "add") {
    if (cart[productId] == undefined) {
      cart[productId] = {"quantity": 1};
    } else {
      cart[productId]["quantity"] += 1;
    }
  }

  if (action == "remove") {
    cart[productId]["quantity"] -= 1;

    if (cart[productId]["quantity"] <= 0) {
      console.log("Item should be deletde");
      delete cart[productId];
    }
  }

  console.log("Cart:", cart);
  document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
  location.reload();
}

function updateUserOrder(productId, action) {
  console.log("User is authenticated, sending data ...");
  
  let url = '/update_item/'
  
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({'productId': productId, 'action': action}),
  }).then((reponse) => {
    return reponse.json();
  }).then((data) => {
    location.reload();  
    console.log('data:', data);
  });
}

// Trying to make the user update the product quantity using the input number
// let productQuantityInput = document.getElementById("product-quantity");

// productQuantityInput.addEventListener("blur", function (e) {
//   if (productQuantityInput.value < 0) {
//     productQuantityInput.value *= -1;
//   } else {
//     productQuantityInput.value = productQuantityInput.value;
//   }
//   let productId = e.target.dataset.product;
//   if (user === "AnonymousUser") {
//     console.log("User is not authenticated");
//   } else {
//     updateUserOrder(productId);
//   }
// });product-quantity