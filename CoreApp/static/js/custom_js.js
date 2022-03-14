function SignUp() {
  try {
     if (!$("#file-upload-form")[0].checkValidity()) {
            $("#file-upload-form").find("#submit-hidden").click();
            return;
        } 
        else {
            swal("Please wait...", "", "success");
            $.ajax({
                type: 'POST',
                url: "/RegisterUser/",
                dataType: 'json',
                async: true,
                data:
                {
                    username: $('#username_id').val(),
                    email: $('#email_id').val(),
                    password: $('#password_id').val(),
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
                },
                success: function (json) {
                    if(json.flag == true) {
                        $('#AuthenticationId').show()
                        $('#SignupId').hide()
                        $('#UpdatePasswordId').hide()
                        $('#email_id_AuthenticationProcess').val(json.email)
                        $('#AuthType_id').val(json.AuthType)           
                     }
                    else {
                        swal(json.Msg, "", "warning");
                    }
                }

            });
        }
        }
        catch (e) {
            swal(e, "", "warning");
        }
        
    }
    
function AuthenticationProcess() {
  try {
    if (!$("#form-action")[0].checkValidity()) {
           $("#form-action").find("#submit-hidden2").click();
           return;
       } 
       else {
           $.ajax({
               type: 'POST',
               url: "/AuthenticationProcess/",
               dataType: 'json',
               async: true,
               data:
               {
                   code: $('#code_id').val(),
                   email: $('#email_id_AuthenticationProcess').val(),
                   AuthType: $('#AuthType_id').val(),
                   'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
               },
               success: function (json) {
               console.log(json);
                if(json.flag == true &&  json.AuthType=='Forgot') {
                    $('#UpdatePasswordId').show()
                     $('#AuthenticationId').hide()
                     $('#SignupId').hide()
                     

                }
                else if(json.flag == true &&  json.AuthType=='Register') {
                 swal({
                    title: "Success",
                    text: json.Msg,
                    icon: "success",
                    buttons: true,
                    dangerMode: true,
                })
                    .then((willDelete) => {
                        if (willDelete) {
                            window.location.href = "/login/";
                        } 
                        else{
                           window.location.href = "/login/";

                        }
                    });
                }

                   else {
                       swal(json.Msg, "", "warning");
                   }
               }

           });
       }
       }
       catch (e) {
           swal(e, "", "warning");
       }
       
   }
  
function Forgot_Password() {

  try {
    if (!$("#forgot-form")[0].checkValidity()) {
           $("#forgot-form").find("#submit-hidden").click();
           return;
       } 
       else {
           swal("Please wait...", "", "success");
           $.ajax({
               type: 'POST',
               url: "/forgot_password/",
               dataType: 'json',
               async: true,
               data:
               {
                   forgot_email: $('#forgot_email_id').val(),
                   'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
               },
               success: function (json) {
               console.log(json);
                if(json.flag == true ) {
                    $('#myModal').modal('hide');
                    $('#myModal2').modal('show');
                    $('#email_forgot_id').val(json.email);
                }
                   else {
                       swal(json.Msg, "", "warning");
                   }
               }

           });
       }
       }
       catch (e) {
           swal(e, "", "warning");
       }
       
   } 
function UpdatePassword() {
    try {
        if (!$("#file-update-form")[0].checkValidity()) {
               $("#file-update-form").find("#submit-hidden3").click();
               return;
           } 
        else {
          $.ajax({
              type: 'POST',
              url: "/UpdatePassword/",
              dataType: 'json',
              async: true,
              data:
              {
                  email: $('#update_email_id').val(),
                  password: $('#update_password_id').val(),
                  'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
              },
              success: function (json) {
                  if(json.flag == true) {
                      $('#AuthenticationId').show()
                      $('#SignupId').hide()
                      $('#UpdatePasswordId').hide()
                      $('#update_email_id').val(json.email)

                  }
                  else {
                      swal(json.Msg, "", "warning");
                  }
              }

          });
      }
      }
      catch (e) {
          swal(e, "", "warning");
      }
      
  }
function Login() {
  try {
   if (!$("#form-action")[0].checkValidity()) {
            $("#form-action").find("#submit-hidden").click();
            return;
        } 
        else {
            $.ajax({
                type: 'POST',
                url: "login_authentication/",
                dataType: 'json',
                async: true,
                data:
                {
                    email: $('#emailId').val(),
                    password: $('#passwordId').val(),
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
                },
                success: function (json) {
                    if(json.Flag == true) {
                        window.location.href = "/index/";
                    }

                    else {
                        swal(json.Msg, "", "warning");
                    }
                }

            });
        }
        }
        catch (e) {
            swal(e, "", "warning");
        }
        
    }
    
function LogOut() {
  try {
   
            $.ajax({
                type: 'POST',
                url: "/logout/",
                dataType: 'json',
                async: true,
                data:
                {
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
                },
                success: function (json) {
                        window.location.href = "/login/";
                }

            });
        }
        catch (e) {
            swal(e, "", "warning");
        }
        }
        