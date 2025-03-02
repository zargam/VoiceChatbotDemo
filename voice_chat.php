<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fixed Speech Icon Bottom-Right</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
        }

        /* Speech Icon Fixed at Bottom-Right */
        .speech-icon {
            position: fixed;
            /*bottom: 20px; 
            right: 20px; 
            */
            font-size: 60px;
            cursor: pointer;
            color: #333;
            transition: transform 0.3s ease-in-out, color 0.3s;
        }

        /* Default hover effect */
        .speech-icon:hover {
            color: red;
        }

        /* Pulse Effect (Wave Animation) */
        .active {
            animation: pulse 1s infinite;
            color: red;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }

    </style>
</head>
<body>
    
    <i id="clickOnMikeButton"  isPlay = "0" class="fa-solid fa-microphone speech-icon"></i>
    
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    
    <script>
        $(document).ready(function(){
            $('#clickOnMikeButton').click(function(){
                this.classList.toggle("active");
                if($(this).attr('isPlay') == "0"){
                    $(this).attr('isPlay',"1");
                }else{
                    $(this).attr('isPlay',"0");
                }
               if($(this).attr('isPlay') == "1"){
                $.ajax({
                    url: 'http://127.0.0.1:5000/voice-command', // Flask server ka URL
                    type: 'GET',
                    success: function(response){
                        $("#clickOnMikeButton").removeClass("active")
                        $("#clickOnMikeButton").attr('isPlay',"0")
                        console.log('Server Response:', response.msg);
                    },
                    error: function(xhr, status, error){
                        $("#clickOnMikeButton").removeClass("active")
                        $("#clickOnMikeButton").attr('isPlay',"0")
                       console.error('Error in API Call');
                   }
               });
            }
          
        });
    });
    </script>

</body>
</html>
