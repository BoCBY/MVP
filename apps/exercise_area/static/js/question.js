// 一鍵生成
function oneBtn(){
    $('#oneBtn').click(function(){
      $.ajax({
        url:'/exercise/',
        type:'post',
        data:{ 
          'purpose': 'oneBtn',
          'SUBJECT': SUBJECT,
        },
        success: function(res){
          if(res.status){
            window.location.href = '/download_pdf/?path=' + encodeURIComponent(res.pdf_path);
          }else {
            alert(res.error)
          }
        }
      });
    });
  }

// 定期試題
function regularQuestion(){
    $('#questions-container').on('click', '.regular-question', function(){
      let date = $(this).attr('date');
      let fileName = $(this).text();
      let period = $(this).closest('[period]').attr('period');
      // console.log(period)

    $.ajax({
      url:'/exercise/',
      type:'post',
      data:{
        'purpose': 'regularQuestion',
        'subject': SUBJECT,
        'date': date,
        'fileName': fileName,
        'period': period,
      },
      success: function(res){
        if (res.status){
          window.location.href = '/download_pdf/?path=' + encodeURIComponent(res.file_path);
        }else{
          alert(res.error)
        }
      }
    })
  })
}