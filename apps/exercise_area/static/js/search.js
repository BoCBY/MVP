function toggleSearchInput() {
    $('#searchInput').toggle();
    if ($('#searchInput').is(":visible")) {
        $('#searchInput').focus(); // Focus on the input field when it becomes visible
    }
  
    $(document).on('click', function(event) {
      if (!$(event.target).closest('#searchContainer').length && !$(event.target).is('#searchContainer')) {
          $('#searchInput').hide();
      }
    });
  }

function filter() {
    // Get the search input value
    let searchText = $('#searchInput').val().toLowerCase();
  
    // Loop through each file link
    $('#displayFileContainer a').each(function() {
        // Get the text content of the file link and convert it to lowercase
        let text = $(this).text().toLowerCase();
  
        // Show or hide the file link based on whether the search text is found in the link text
        if (text.includes(searchText)) {
            $(this).parent().parent().show();
        } else {
            $(this).parent().parent().hide();
        }
    });
  }
  
  function search(){
    $('#searchIcon').click(toggleSearchInput)
    $('#searchInput').on('input', filter);
  }