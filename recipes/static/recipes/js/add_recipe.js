document.addEventListener("DOMContentLoaded", function () {
  const formsetContainer = document.getElementById("formset-container");
  const addAnotherBtn = document.getElementById("add-another-btn");
  const totalFormsInput = document.querySelector(
    'input[name="form-TOTAL_FORMS"]'
  );

  addAnotherBtn.addEventListener("click", function () {
    const originalForm = document.querySelector(
      "#formset-container .form-item"
    );
    const clonedForm = originalForm.cloneNode(true);
    const newIngredientInput = clonedForm.querySelector('input[type="text"]');
    newIngredientInput.value = ""; // Reset the value to an empty string

    // Update the input names and IDs based on the new form count
    let totalForms = parseInt(totalFormsInput.value);
    clonedForm.innerHTML = clonedForm.innerHTML.replace(
      /form-\d+/g,
      `form-${totalForms}`
    );

    formsetContainer.appendChild(clonedForm);

    // Increment the TOTAL_FORMS value
    totalFormsInput.value = totalForms + 1;
  });

  // Code to auto-hide the message
  setTimeout(function () {
    let alerts = document.querySelectorAll(".alert");
    if (alerts) {
      alerts.forEach(function (alert) {
        alert.style.opacity = "0";
        setTimeout(function () {
          alert.style.display = "none";
        }, 300); // Waits for the opacity animation to complete before hiding the element
      });
    }
  }, 3000); // hides the message after 3 seconds
});
