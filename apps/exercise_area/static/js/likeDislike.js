function likeDislike(){
    $('#displayFileContainer').on('click', '.like-btn', function() {
      let $this = $(this);
      const file = $this.parent().find('.answer-file');
      let fileName = file.text();
      let likeCount = parseInt(file.attr('data-like'));
      let dislikeCount = parseInt(file.attr('data-dislike'));
  
      if ($this.hasClass('fa-regular')) {
          // Like the file
          file.attr('data-like', ++likeCount);
          $this.removeClass('fa-regular').addClass('fa-solid');
          $this.next('.like-count').text(likeCount);
          // 執行到這裡, 後台關於這份檔案的讚數要去+1
          $.ajax({
            url: '/like_dislike/',
            type: 'post',
            data: {
              'action': 'like+1',
              'subject': SUBJECT,
              'date': DATE,
              'period': PERIOD,
              'number': NUMBER,
              'fileName': fileName,
            },
            dataType: 'JSON',
            success: function(res){
              if(res.status){
                // 接著判斷, 如果原本是按倒讚的情形
                if ($this.siblings('.dislike-btn').hasClass('fa-solid')){
                  file.attr('data-dislike', --dislikeCount);
                  $this.siblings('.dislike-btn').removeClass('fa-solid').addClass('fa-regular');
                  $this.siblings('.dislike-btn').next('.dislike-count').text(dislikeCount);
                  // 執行到這裡, 後台關於這份檔案的倒讚數要-1
                  $.ajax({
                    url: '/like_dislike/',
                    type: 'post',
                    data: {
                      'action': 'dislike-1',
                      'subject': SUBJECT,
                      'date': DATE,
                      'period': PERIOD,
                      'number': NUMBER,
                      'fileName': fileName,
                    },
                    dataType: 'JSON',
                    success: function(res){
                      if(res.status){
                        console.log(res.message)
                      }else{
                        console.log(res.error)
                      }
                }
              }); // inner ajax end
              }
            }else{
                console.log(res.error) 
              }
            }
          }); // outer ajax end
          
      } else {
          // Cancel like
          file.attr('data-like', --likeCount);
          $this.removeClass('fa-solid').addClass('fa-regular');
          $this.next('.like-count').text(likeCount);
          // 執行到這裡, 後台關於這份檔案的讚數要去-1
          $.ajax({
            url: '/like_dislike/',
            type: 'post',
            data: {
              'action': 'like-1',
              'subject': SUBJECT,
              'date': DATE,
              'period': PERIOD,
              'number': NUMBER,
              'fileName': fileName,
            },
            dataType: 'JSON',
            success: function(res){
              if(res.status){
                console.log(res.message)
              }else{
                console.log(res.error)
              }
        }
      }); // ajax end
      }
      });
  
    $('#displayFileContainer').on('click', '.dislike-btn', function() {
      let $this = $(this);
      const file = $this.parent().find('.answer-file');
      let fileName = file.text();
      let likeCount = parseInt(file.attr('data-like'));
      let dislikeCount = parseInt(file.attr('data-dislike'));
  
      if ($this.hasClass('fa-regular')) {
          // Dislike the file
          file.attr('data-dislike', ++dislikeCount);
          $this.removeClass('fa-regular').addClass('fa-solid');
          $this.next('.dislike-count').text(dislikeCount);
          // 執行到這裡, 後台關於這份檔案的倒讚數要+1
          $.ajax({
            url: '/like_dislike/',
            type: 'post',
            data: {
              'action': 'dislike+1',
              'subject': SUBJECT,
              'date': DATE,
              'period': PERIOD,
              'number': NUMBER,
              'fileName': fileName,
            },
            dataType: 'JSON',
            success: function(res){
              if(res.status){
                // 接著判斷, 如果原本是按讚的情形
                if ($this.siblings('.like-btn').hasClass('fa-solid')){
                  file.attr('data-like', --likeCount);
                  $this.siblings('.like-btn').removeClass('fa-solid').addClass('fa-regular');
                  $this.siblings('.like-btn').next('.like-count').text(likeCount);
                  // 執行到這裡, 後台關於這份檔案的讚數要-1
                  $.ajax({
                    url: '/like_dislike/',
                    type: 'post',
                    data: {
                      'action': 'like-1',
                      'subject': SUBJECT,
                      'date': DATE,
                      'period': PERIOD,
                      'number': NUMBER,
                      'fileName': fileName,
                    },
                    dataType: 'JSON',
                    success: function(res){
                      if(res.status){
                        console.log(res.message)
                      }else{
                        console.log(res.error)
                      }
                }
              }); // inner ajax end
              }
            }else{
                console.log(res.error) 
              }
            }
          }); // outer ajax end
          
      } else {
          // Cancel dislike
          file.attr('data-dislike', --dislikeCount);
          $this.removeClass('fa-solid').addClass('fa-regular');
          $this.next('.dislike-count').text(dislikeCount);
          // 執行到這裡, 後台關於這份檔案的倒讚數要-1
          $.ajax({
            url: '/like_dislike/',
            type: 'post',
            data: {
              'action': 'dislike-1',
              'subject': SUBJECT,
              'date': DATE,
              'period': PERIOD,
              'number': NUMBER,
              'fileName': fileName,
            },
            dataType: 'JSON',
            success: function(res){
              if(res.status){
                console.log(res.message)
              }else{
                console.log(res.error)
              }
        }
      }); // ajax end
      }
    });
  }
  
  function likeDislikeCount(){
    $('.row').each(function () {
      var $row = $(this);
      var $answerFile = $row.find('.answer-file');
      var $likeCount = $row.find('.like-count');
      var $dislikeCount = $row.find('.dislike-count');
  
      $likeCount.text($answerFile.data('like'));
      $dislikeCount.text($answerFile.data('dislike'));
    });
  }