function prevPage(){
    $('#queNumTopContainer').on('click', '#question-number-previous', function(){
      $('#questionNumModal').modal('hide');
      $('#answerModal').modal('show');
    });
  
    $('#ansTopContainer').on('click', '#answer-previous', function(){
      $('#answerModal').modal('hide');
      $('#exerciseModal').modal('show');
    });
  }