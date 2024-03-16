// Define a search module
const searchModule = (function() {
  // Private functions
  function toggleSearchInput(searchInputId) {
      $(`#${searchInputId}`).toggle();
      if ($(`#${searchInputId}`).is(":visible")) {
          $(`#${searchInputId}`).focus(); // Focus on the input field when it becomes visible
      }
  
      $(document).on('click', function(event) {
          if (!$(event.target).closest('.search-container').length && !$(event.target).is('.search-container')) {
              $(`#${searchInputId}`).hide();
          }
      });
  }
  
  function filter(searchInputId, searchArea) {
      let searchText = $(`#${searchInputId}`).val().toLowerCase();
  
      if(searchArea === '#displayFileContainer a'){
      // for ansSearchInput
        $(searchArea).each(function() {
            let text = $(this).text().toLowerCase();
    
            if (text.includes(searchText)) {
                $(this).parent().parent().show();
            } else {
                $(this).parent().parent().hide();
            }
        });
      }else if(searchArea === '#allSubjectContainer h5'){
          // for subjectSearchInput
          $(searchArea).each(function() {
              let text = $(this).text();
              if (text.includes(searchText)) {
                  $(this).closest(".subject-container").show();
              } else {
                  $(this).closest(".subject-container").hide();
              }
          });
      }else{
          // for each subject searchInput ex: mathSearchInput, physicsSearchInput 
          $(searchArea).each(function() {
              let text = $(this).text();
      
              if (text.includes(searchText)) {
                  $(this).show();
              } else {
                  $(this).hide();
              }
      });
  }
  }

  // Public function
  function init(searchIconId, searchInputId, searchArea) {
      $(`#${searchIconId}`).click(function(event) {
          event.preventDefault();
          toggleSearchInput(searchInputId);
      });
      $(`#${searchInputId}`).on('input', function() {
          filter(searchInputId, searchArea);
      });
  }

  // Expose public functions
  return {
      init: init
  };
})();