function sortDate(){
    const fileItems = $('.answer-file');
  
    // Convert jQuery object to Array for easier sorting
    const fileArray = $.makeArray(fileItems);
  
    // Sort the array based on the number in the text of the <a> tag
    fileArray.sort((a, b) => {
      const numA = parseInt($(a).text().split('-')[1].replace('.txt', '')); // .txt要改成筆記檔的副檔名
      const numB = parseInt($(b).text().split('-')[1].replace('.txt', '')); // .txt要改成筆記檔的副檔名
      return numB - numA; // Descending order
    });
  
    // Remove existing items
    $('#displayFileContainer').empty();
  
    // Re-append sorted items
    fileArray.forEach((file) => {
      $('#displayFileContainer').append($(file).parent().parent());
    });
  }
  
  function sortLike(){
    const fileItems = $('.answer-file');
  
    // Convert jQuery object to Array for easier sorting
    const fileArray = $.makeArray(fileItems);
  
    // Sort the array based on the number like-dislike
    fileArray.sort(function(a, b) {
      const aLike = parseInt($(a).data('like'));
      const aDislike = parseInt($(a).data('dislike'));
      const aValue = aLike - aDislike;
  
      const bLike = parseInt($(b).data('like'));
      const bDislike = parseInt($(b).data('dislike'));
      const bValue = bLike - bDislike;
  
      return bValue - aValue; // Sort in descending order
    });
  
    // Remove existing items
    $('#displayFileContainer').empty();
  
    // Re-append sorted items
    fileArray.forEach((file) => {
      $('#displayFileContainer').append($(file).parent().parent());
    });
  }
  
  function sort(){
    // Toggle dropdown menu when sort icon is clicked
    $('#sortIcon').click(function() {
      $('#sortDropdown').toggle();
    });
  
    // Close the dropdown menu if the user clicks outside of it
    $(document).click(function(event) {
      if (!$(event.target).closest('#sortContainer').length) {
          $('#sortDropdown').hide();
      }
    });
  
    // Handle sorting logic when the user selects an option
    $('#sortDate').click(function() {
      sortDate();
      $('#sortDropdown').hide();
    });
  
    $('#sortLike').click(function() {
      sortLike();
      $('#sortDropdown').hide();
    });
}