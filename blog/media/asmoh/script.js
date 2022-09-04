(function($){
    $('#ios-form').on('submit',function(e){          
        e.preventDefault()
       $('#sub-btn').html('')
       $('#sub-btn').addClass('io-spiner')
        var action = function(d){
          if(d=='Created'){
          let item=`<div class="navsm-success" data-aos="zoom-in" id="msg2">Thanks Form has been submited</div>`
          document.getElementById('server-msg').innerHTML= item;
          $('#sub-btn').removeClass('io-spiner')
          $('#sub-btn').html('Contact')
          $("#ios-form")[0].reset();

        }
        else{
            let item=`<div class="navsm-warning" data-aos="zoom-in" id="msg2">OOPS An error occured</div>`
            document.getElementById('server-msg').innerHTML= item; 
            $('#sub-btn').removeClass('io-spiner')
            $('#sub-btn').html('Try again')  
        }
        };
        $.ajax({
            type: "POST",
            url: "contact/",
            data: {
                name:$('#name').val(),
                email:$('#email').val(),
                text:$('#text_area').val(),
                topic:$('#topic').find(":selected").text(),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
            },
            success: action,
            error:action
        });
    });
    }(jQuery))
    $('#email_sub').on('submit',function(e){          
        e.preventDefault()
        $('#sub-btn-email').html('')
        $('#sub-btn-email').addClass('io-spiner')
         var action = function(d){
           console.log(d)
           if(d=='Created'){
           let item=`<div class="alert alert-success" data-aos="zoom-in" id="msg">ThankYou for our email subscription.</div>`
           document.getElementById('server-msg-sub').innerHTML= item;
           $('#sub-btn-email').removeClass('io-spiner')
           $('#sub-btn-email').html('<i class="fa fa-rocket text-iosprimary" aria-hidden="true"></i>')
           $("#email_sub")[0].reset();
 
         }
         else{
             if(d=='all'){
                 let item=`<div class="alert alert-danger" data-aos="zoom-in" id="msg">You are alread subscribed to email service.</div>`
                 document.getElementById('server-msg-sub').innerHTML= item; 
                 $('#sub-btn-email').removeClass('io-spiner')
                 $('#sub-btn-email').html('<i class="fa fa-rocket text-iosprimary" aria-hidden="true"></i>') 
             }
             else{
                 let item=`<div class="alert alert-danger" data-aos="zoom-in" id="msg">OOPS An error occured</div>`
                 document.getElementById('server-msg-sub').innerHTML= item; 
                 $('#sub-btn-email').removeClass('io-spiner')
                 $('#sub-btn-email').html('<i class="fa fa-rocket text-iosprimary" aria-hidden="true"></i>') 
             }
             
         }
         };
         $.ajax({
             type: "POST",
             url: "subscribe/",
             data: {
                 email:$('#email-sub').val(),
                 csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
             },
             success: action,
             error:action
         });
     });
    



     
     $('#delete_blog').on('submit',function(e){          
        e.preventDefault()
        $('#sub-btn-email').html('')
        $('#delete .all').addClass('io-spiner-only')
         var action = function(d){
           console.log(d)
           if(d=='Created'){
           let item=`<div class="navsm-success" data-aos="zoom-in" id="msg2">ThankYou for our email subscription.</div>`
           document.getElementById('server-msg-sub').innerHTML= item;
           $('#sub-btn-email').removeClass('io-spiner')
           $('#sub-btn-email').html('<i class="fa fa-rocket text-iosprimary" aria-hidden="true"></i>')
           $("#email_sub")[0].reset();
 
         }
         else{
             if(d=='all'){
                 let item=`<div class="navsm-warning" data-aos="zoom-in" id="msg2">You are alread subscribed to email service.</div>`
                 document.getElementById('server-msg-sub').innerHTML= item; 
                 $('#sub-btn-email').removeClass('io-spiner')
                 $('#sub-btn-email').html('<i class="fa fa-rocket text-iosprimary" aria-hidden="true"></i>') 
             }
             else{
                 let item=`<div class="navsm-warning" data-aos="zoom-in" id="msg2">OOPS An error occured</div>`
                 document.getElementById('server-msg-sub').innerHTML= item; 
                 $('#sub-btn-email').removeClass('io-spiner')
                 $('#sub-btn-email').html('<i class="fa fa-rocket text-iosprimary" aria-hidden="true"></i>') 
             }
             
         }
         };
         $.ajax({
             type: "POST",
             url: "/blog/delete/",
             data: {
                 slug:$('#slug').val(),
                 csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
             },
             success: action,
             error:action
         });
     });