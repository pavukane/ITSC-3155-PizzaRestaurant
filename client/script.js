// Function to fetch crusts from the REST API and populate the form
function populateCrusts() {
  fetch('http://localhost:8000/crusts')
    .then(response => response.json())
    .then(crusts => {
      const crustsFieldset = document.getElementById('crustsFieldset');
      crusts.forEach(crust => {
        const crustLabel = document.createElement('label');
        crustLabel.innerHTML = `
          <input type="checkbox" name="crust" value="${crust.name}">
          ${crust.name}
        `;
        crustsFieldset.appendChild(crustLabel);
      });
    })
    .catch(error => {
      console.error('Error fetching crusts:', error);
    });
}

// Function to fetch toppings from the REST API and populate the form
function populateToppings() {
  fetch('http://localhost:8000/toppings')
  .then(response => response.json())
  .then(toppings => {
    const toppingsFieldset = document.getElementById('toppingsFieldset');
    toppings.forEach(topping => {
      const toppingLabel = document.createElement('label');
      toppingLabel.innerHTML = `
        <input type="checkbox" name="topping" value="${topping.name}">
        ${topping.name}
      `;
      toppingsFieldset.appendChild(toppingLabel);
    });
  })
  .catch(error => {
    console.error('Error fetching toppings:', error);
  });
}

// Event listener for form submission
document.getElementById('pizzaForm').addEventListener('submit', function(event) {
  event.preventDefault();
  const formData = new FormData(this);
  const selectedCrust = formData.get('crust');
  const selectedToppings = formData.getAll('topping');

  // You can process the selected options here, e.g., display them, send to server, etc.
  console.log('Selected Crust:', selectedCrust);
  console.log('Selected Toppings:', selectedToppings);
});
