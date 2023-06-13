var anchofinal;
var actualiza;
         document.addEventListener('DOMContentLoaded',function(){
                    
                 anchofinal = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
                     
                 if(anchofinal <= 767){
                        actualiza = "<video autoplay muted loop  class='videomedia'><source src='images/mivideo2.mp4' type='video/mp4'> </video>"
                        }
                        else
                        {
                            actualiza = "<video autoplay muted loop   class='videomedia'><source src='images/mivideo.mp4' type='video/mp4'> </video>"
                        }
                        document.getElementById('video').innerHTML = actualiza;



                     window.addEventListener('resize',function(anchofinalinicial){
                            anchofinal=window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
                         
                           
                            if(anchofinal <= 767){
                                     actualiza = "<video autoplay muted loop  class='videomedia'><source src='images/mivideo2.mp4' type='video/mp4'> </video>"
                                }
                                else
                                {
                                    actualiza = "<video autoplay muted loop   class='videomedia'><source src='images/mivideo.mp4' type='video/mp4'> </video>"
                                }
                                document.getElementById('video').innerHTML = actualiza;
                             
                        });
                    
   
                }); 

         
               