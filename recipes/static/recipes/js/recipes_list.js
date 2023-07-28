$(document).ready(function () {
  // Initialize the select2 dropdown
  $("#id_Ingredients").select2({
    placeholder: "Choose ingredients",
    allowClear: true,
    multiple: true,
    width: "200px",
  });

  // Attach the click event handler to the clearButton
  $("#clearButton").click(function () {
    // Check if any of the search fields have a value
    var isSearchMade =
      $("#id_Recipe_Name").val().trim() !== "" ||
      $("#id_Ingredients").val().length !== 0 ||
      $("#id_chart_type").val().trim() !== "";

    if (isSearchMade) {
      // If a search has been made, reload the page without search parameters
      window.location.href = recipesListUrl; // Use the variable from the template
    } else {
      // If no search has been made, just clear the fields
      $("#id_Recipe_Name").val("");
      $("#id_Ingredients").val(null).trigger("change"); // Clear select2 field
      $("#id_chart_type").val("");
    }
  });
});
