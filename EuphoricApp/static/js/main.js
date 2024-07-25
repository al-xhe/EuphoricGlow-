

//For the card button
document.addEventListener('DOMContentLoaded', function () {
    const cart = [];
    const cartButton = document.getElementById('cartButton');
    const cartCount = document.getElementById('cartCount');
    const cartDropdownMenu = document.getElementById('cartDropdownMenu');
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            const name = this.getAttribute('data-name');
            const price = this.getAttribute('data-price');
            const img = this.getAttribute('data-img');

            const product = { name, price, img };
            cart.push(product);
            updateCart();
        });
    });

    function updateCart() {
        cartCount.textContent = cart.length;

        let dropdownContent = '';
        if (cart.length > 0) {
            cart.forEach(item => {
                dropdownContent += `
                    <li class="dropdown-item">
                        <img src="${item.img}" alt="${item.name}">
                        <div>
                            <strong>${item.name}</strong>
                            <p>${item.price}</p>
                        </div>
                    </li>
                `;
            });
        } else {
            dropdownContent = '<li><a class="dropdown-item" href="#">Your cart is empty</a></li>';
        }
        cartDropdownMenu.innerHTML = dropdownContent;
    }
});

/*document.addEventListener('DOMContentLoaded', function () {
    const cart = [];
    const cartButton = document.getElementById('cartButton');
    const cartCount = document.getElementById('cartCount');
    const cartDropdownMenu = document.getElementById('cartDropdownMenu');
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            const name = this.getAttribute('data-name');
            const price = this.getAttribute('data-price');
            const img = this.getAttribute('data-img');

            const product = { name, price, img };
            cart.push(product);
            updateCart();
        });
    });

    function updateCart() {
        cartCount.textContent = cart.length;

        let dropdownContent = '';
        if (cart.length > 0) {
            cart.forEach(item => {
                dropdownContent += `
                    <li class="dropdown-item">
                        <img src="${item.img}" alt="${item.name}">
                        <div>
                            <strong>${item.name}</strong>
                            <p>${item.price}</p>
                        </div>
                    </li>
                `;
            });
        } else {
            dropdownContent = '<li><a class="dropdown-item" href="#">Your cart is empty</a></li>';
        }
        cartDropdownMenu.innerHTML = dropdownContent;
    }
}); */

/* Order form submission handling
//document.getElementById('orderForm').addEventListener('submit', function(event) {
   // event.preventDefault(); // Prevent the default form submission

    // Collect form data
  //  const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const product = document.getElementById('product').value;
    const quantity = document.getElementById('quantity').value;

    // You can handle the form data here (e.g., send it to a server)
    console.log('Order Details:', {
        name,
        email,
        phone,
        product,
        quantity
    });

    // Show the confirmation message
    document.getElementById('orderForm').classList.add('hidden');
    document.getElementById('orderConfirmation').classList.remove('hidden');
});*/