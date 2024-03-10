function calculus(){ 
    $('#calculusBtn').click(function(){
      SUBJECT = $(this).attr('SUBJECT');

      $.ajax({
        url: '/exercise/',
        type: 'post',
        data: {
          'purpose': 'makeTags',
          'SUBJECT': SUBJECT},
        dataType: 'JSON',
        success : function(res){
          if (res.status){
            // 先刪除已存的, 不然重複開啟按鈕會不斷生成標籤
            $('div[period="present"] .row').remove();
            $('div[period="past"] .row').remove();

            // 創建當期試題(present)的標籤
            let divRow = $('<div>').attr('class', 'row');
            let divQueCol = $('<div>').attr('class', 'col-sm-5');
            let divAnsCol = $('<div>').attr('class', 'col-sm-5');
            let pdfIcon = $('<i>').attr('class', 'fa-regular fa-file-pdf');
            let folderIcon = $('<i>').attr('class', 'fa-regular fa-folder');
            let aQuestion = $('<a>').attr({'href':'#', 'class':'regular-question', 'date': res.present}).text(res.present+'.pdf');
            let aAnswer = $('<a>').attr({'href':'#', 'class':'regular-answer', 'date': res.present}).text('答案區');
            divQueCol.append(pdfIcon);
            divQueCol.append(aQuestion);
            divAnsCol.append(folderIcon);
            divAnsCol.append(aAnswer);
            divRow.append(divQueCol);
            divRow.append(divAnsCol);
            $('div[period="present"] h6').after(divRow);

            // 創建歷期試題(past)的標籤
            $.each(res.past, function(index, date){
              let divRow = $('<div>').attr('class', 'row');
                let divQueCol = $('<div>').attr('class', 'col-sm-5');
                let divAnsCol = $('<div>').attr('class', 'col-sm-5');
                let pdfIcon = $('<i>').attr('class', 'fa-regular fa-file-pdf');
                let folderIcon = $('<i>').attr('class', 'fa-regular fa-folder');
                let aQuestion = $('<a>').attr({'href':'#', 'class':'regular-question', 'date': date}).text(date+'.pdf');
                let aAnswer = $('<a>').attr({'href':'#', 'class':'regular-answer', 'date': date}).text('答案區');
                divQueCol.append(pdfIcon);
                divQueCol.append(aQuestion);
                divAnsCol.append(folderIcon);
                divAnsCol.append(aAnswer);
                divRow.append(divQueCol);
                divRow.append(divAnsCol);
                $('div[period="past"] h6').after(divRow);
            });
            
            $('#exerciseModalTitle').text($('#calculusBtn').text());
            $('#exerciseModal').modal('show');
          }else{
            alert(res.error);
          }
        }
      });
    });
  }

  function linearAlgebra(){ 
    $('#linAlgeBtn').click(function(){
      SUBJECT = $(this).attr('SUBJECT');
      
      $.ajax({
        url: '/exercise/',
        type: 'post',
        data: {
          'purpose': 'makeTags',
          'SUBJECT': SUBJECT},
        dataType: 'JSON',
        success : function(res){
          if (res.status){
            // 先刪除已存的, 不然重複開啟按鈕會不斷生成標籤
            $('div[period="present"] .row').remove();
            $('div[period="past"] .row').remove();

            // 創建當期試題(present)的標籤
            let divRow = $('<div>').attr('class', 'row');
            let divQueCol = $('<div>').attr('class', 'col-sm-5');
            let divAnsCol = $('<div>').attr('class', 'col-sm-5');
            let pdfIcon = $('<i>').attr('class', 'fa-regular fa-file-pdf');
            let folderIcon = $('<i>').attr('class', 'fa-regular fa-folder');
            let aQuestion = $('<a>').attr({'href':'#', 'class':'regular-question', 'date': res.present}).text(res.present+'.pdf');
            let aAnswer = $('<a>').attr({'href':'#', 'class':'regular-answer', 'date': res.present}).text('答案區');
            divQueCol.append(pdfIcon);
            divQueCol.append(aQuestion);
            divAnsCol.append(folderIcon);
            divAnsCol.append(aAnswer);
            divRow.append(divQueCol);
            divRow.append(divAnsCol);
            $('div[period="present"] h6').after(divRow);

            // 創建歷期試題(past)的標籤
            $.each(res.past, function(index, date){
              let divRow = $('<div>').attr('class', 'row');
                let divQueCol = $('<div>').attr('class', 'col-sm-5');
                let divAnsCol = $('<div>').attr('class', 'col-sm-5');
                let pdfIcon = $('<i>').attr('class', 'fa-regular fa-file-pdf');
                let folderIcon = $('<i>').attr('class', 'fa-regular fa-folder');
                let aQuestion = $('<a>').attr({'href':'#', 'class':'regular-question', 'date': date}).text(date+'.pdf');
                let aAnswer = $('<a>').attr({'href':'#', 'class':'regular-answer', 'date': date}).text('答案區');
                divQueCol.append(pdfIcon);
                divQueCol.append(aQuestion);
                divAnsCol.append(folderIcon);
                divAnsCol.append(aAnswer);
                divRow.append(divQueCol);
                divRow.append(divAnsCol);
                $('div[period="past"] h6').after(divRow);
            });
            
            $('#exerciseModalTitle').text($('#linAlgeBtn').text());
            $('#exerciseModal').modal('show');
          }else{
            alert(res.error);
          }
        }
      });
    });
  }

  function generalPhysics(){ 
    $('#GenPhyBtn').click(function(){
      SUBJECT = $(this).attr('SUBJECT');
      
      $.ajax({
        url: '/exercise/',
        type: 'post',
        data: {
          'purpose': 'makeTags',
          'SUBJECT': SUBJECT},
        dataType: 'JSON',
        success : function(res){
          if (res.status){
            // 先刪除已存的, 不然重複開啟按鈕會不斷生成標籤
            $('div[period="present"] .row').remove();
            $('div[period="past"] .row').remove();

            // 創建當期試題(present)的標籤
            let divRow = $('<div>').attr('class', 'row');
            let divQueCol = $('<div>').attr('class', 'col-sm-5');
            let divAnsCol = $('<div>').attr('class', 'col-sm-5');
            let pdfIcon = $('<i>').attr('class', 'fa-regular fa-file-pdf');
            let folderIcon = $('<i>').attr('class', 'fa-regular fa-folder');
            let aQuestion = $('<a>').attr({'href':'#', 'class':'regular-question', 'date': res.present}).text(res.present+'.pdf');
            let aAnswer = $('<a>').attr({'href':'#', 'class':'regular-answer', 'date': res.present}).text('答案區');
            divQueCol.append(pdfIcon);
            divQueCol.append(aQuestion);
            divAnsCol.append(folderIcon);
            divAnsCol.append(aAnswer);
            divRow.append(divQueCol);
            divRow.append(divAnsCol);
            $('div[period="present"] h6').after(divRow);

            // 創建歷期試題(past)的標籤
            $.each(res.past, function(index, date){
              let divRow = $('<div>').attr('class', 'row');
                let divQueCol = $('<div>').attr('class', 'col-sm-5');
                let divAnsCol = $('<div>').attr('class', 'col-sm-5');
                let pdfIcon = $('<i>').attr('class', 'fa-regular fa-file-pdf');
                let folderIcon = $('<i>').attr('class', 'fa-regular fa-folder');
                let aQuestion = $('<a>').attr({'href':'#', 'class':'regular-question', 'date': date}).text(date+'.pdf');
                let aAnswer = $('<a>').attr({'href':'#', 'class':'regular-answer', 'date': date}).text('答案區');
                divQueCol.append(pdfIcon);
                divQueCol.append(aQuestion);
                divAnsCol.append(folderIcon);
                divAnsCol.append(aAnswer);
                divRow.append(divQueCol);
                divRow.append(divAnsCol);
                $('div[period="past"] h6').after(divRow);
            });
            
            $('#exerciseModalTitle').text($('#GenPhyBtn').text());
            $('#exerciseModal').modal('show');
          }else{
            alert(res.error);
          }
        }
      });
    });
  }