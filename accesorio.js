let cart = [];
let total = 0;

function addToCart(productName, price) {
    cart.push({ productName, price });
    total += price;
    updateCart();
    showFloatingCart();
}

function removeFromCart(index) {
    total -= cart[index].price;
    cart.splice(index, 1);
    updateCart();
}

function updateCart() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');

    cartItems.innerHTML = '';
    let totalPrice = 0; // Variable para calcular el total sin decimales
    cart.forEach((item, index) => {
        const li = document.createElement('li');
        li.textContent = `${item.productName}: $${item.price.toLocaleString()}`; // Formatear el precio con separadores de miles
        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'Eliminar';
        removeBtn.onclick = () => removeFromCart(index);
        li.appendChild(removeBtn);
        cartItems.appendChild(li);
        totalPrice += item.price; // Sumar el precio de cada producto al total
    });

    total = totalPrice; // Actualizar el total
    cartTotal.textContent = Math.round(total).toLocaleString(); // Formatear el total con separadores de miles
}


function pay() {
    alert(`Total a pagar: $${Math.round(total)}`); // Redondear el total sin decimales
}

// Función para mostrar el carrito flotante
function showFloatingCart() {
    const floatingCart = document.getElementById('floating-cart');
    floatingCart.style.display = 'block';
}

// Función para ocultar el carrito flotante
function hideFloatingCart() {
    const floatingCart = document.getElementById('floating-cart');
    floatingCart.style.display = 'none';
}

// Agregar evento de clic al icono del carrito para mostrar el carrito flotante
const cartIcon = document.getElementById('cart-icon');
cartIcon.addEventListener('click', showFloatingCart);

// Llamar a la función para mostrar el carrito flotante al agregar un producto
// Esta línea fue movida de la función addToCart() original
