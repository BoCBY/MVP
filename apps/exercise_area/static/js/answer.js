function regularAnswer(){
    $('#displayFileContainer').on('click', '.answer-file', function(){
      let fileName = $(this).text();
  
      $.ajax({
        url:'/exercise/',
        type:'post',
        data:{
          'purpose': 'regularAnswer',
          'subject': SUBJECT,
          'date': DATE,
          'number': NUMBER,
          'period': PERIOD,
          'fileName': fileName,
        },
        success: function(res){
          if (res.status){
            console.log('JJJJ')
            window.location.href = '/download_answer_panel/?path=' + encodeURIComponent(res.file_path);
          }else{
            alert(res.error)
          }
        }
      });
    });
  }
          
  function answerArea(){
    $('#questions-container').on('click', '.regular-answer', function(){
      DATE = $(this).attr('date');
      PERIOD = $(this).closest('[period]').attr('period');
      let prevModalTitle = $('#exerciseModalTitle').text()
      $('#answerModalLabel').text(prevModalTitle +' - '+ DATE);
      $('#answerModal').modal('show');
      $('#exerciseModal').modal('hide');
    })
  }
  
  function ansQuestionNum(){
    $('#questionNumTable').on('click', '.question-number', function(){
      NUMBER = $(this).text()
      let prevModalTitle = $('#answerModalLabel').text()
      $('#ansQuestionNumModalLabel').text(prevModalTitle + ' - ' + NUMBER)
      $('#answerModal').modal('hide');
  
      $.ajax({
        url:'/exercise/',
        type:'post',
        data:{
          'purpose':'openQuestionNumModal',
          'number': NUMBER,
          'date': DATE,
          'period': PERIOD,
          'subject': SUBJECT,
        },
        dataType:'JSON',
        success: function(res){
          if(res.status){
            /* 創建該題號資料夾裡的DOM標籤 */
  
            // 先把原本已有的刪除
            $('#displayFileContainer').empty();
  
            // 開始建DOM標籤
            $.each(res.file_dict, function(fileName, likeDislikeData){
              let divRow = $('<div>').attr('class', 'row');
              let divGrid = $('<div>').attr('class', 'col-sm-12 d-flex align-items-center');
              let notePanelIcon = $('<i>').attr('class', 'fa-solid fa-pen-to-square');
              let likeIcon = $('<i>').attr('class', 'fa-regular fa-thumbs-up like-btn');
              let dislikeIcon = $('<i>').attr('class', 'fa-regular fa-thumbs-down dislike-btn');
              // a與span標籤中喜歡數與不喜歡數是儲存在資料本身的, 要到後台獲取然後填上去
              let spanLike = $('<span>').attr('class', 'like-count').text(likeDislikeData.like); // 對應a的data-like
              let spanDislike = $('<span>').attr('class', 'dislike-count').text(likeDislikeData.dislike); // 對應a的data-dislike
              let a = $('<a>').attr({'href': '#', 'class': 'answer-file mr-auto', 'data-like': likeDislikeData.like, 'data-dislike': likeDislikeData.dislike,}).text(fileName);
              divGrid.append(notePanelIcon);
              divGrid.append(a);
              divGrid.append(likeIcon);
              divGrid.append(spanLike);
              divGrid.append(dislikeIcon);
              divGrid.append(spanDislike);
              divRow.append(divGrid);
              $('#displayFileContainer').append(divRow);
            })
            likeDislikeCount();
            $('#questionNumModal').modal('show');
          }else{
            alert(res.error)
          }
        }
      })
    })
  }