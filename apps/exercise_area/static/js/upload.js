function upLoad(){
    // 點擊圖標就能上傳檔案的功能
    $('#uploadIcon').on('click', function() {
      $('#fileInput').click();
    });
    
    $('#fileInput').on('change', function() {
      const file = this.files[0];
      if (file.type === 'text/plain') {
        uploadFile(file);
      } else {
        alert('Please select a .txt file');
      }
    });
  }
  
  function uploadFile(file) {
    const formData = new FormData(); // a built-in class in js which is key-value pair inside for coveniently using when uploading file
    formData.append('file', file);
    formData.append('subject', SUBJECT);
    formData.append('number', NUMBER);
    formData.append('date', DATE);
    formData.append('period', PERIOD);
  
    $.ajax({
      url: '/upload_file/', 
      type: 'POST',
      data: formData,
      processData: false,
      contentType: false,
      success: function(res) {
        if(res.status){
          alert(res.message);
          let divRow = $('<div>').attr('class', 'row');
          let divGrid = $('<div>').attr('class', 'col-sm-12 d-flex align-items-center');
          let notePanelIcon = $('<i>').attr('class', 'fa-solid fa-pen-to-square');
          let likeIcon = $('<i>').attr('class', 'fa-regular fa-thumbs-up like-btn');
          let dislikeIcon = $('<i>').attr('class', 'fa-regular fa-thumbs-down dislike-btn');
          let spanLike = $('<span>').attr('class', 'like-count').text(0);
          let spanDislike = $('<span>').attr('class', 'dislike-count').text(0);
          let a = $('<a>').attr({'href': '#', 'class': 'answer-file mr-auto', 'data-like': '0', 'data-dislike': '0',}).text(res.file_name);
          divGrid.append(notePanelIcon);
          divGrid.append(a);
          divGrid.append(likeIcon);
          divGrid.append(spanLike);
          divGrid.append(dislikeIcon);
          divGrid.append(spanDislike);
          divRow.append(divGrid);
          $('#displayFileContainer').append(divRow);
      }else{
        alert(res.error);
      }
    }
    });
  }