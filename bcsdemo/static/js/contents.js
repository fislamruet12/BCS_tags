


function contents(urls,pageurl)
{

window.history.pushState('object or string', 'Title',""+pageurl);
var displayResources = $("#conntent");

    displayResources.text("Loading data from JSON source...");

    $.ajax({
      type: "GET",
      url: urls, // Using our resources.json file to serve results
      success: function(result) {
        console.log(result);
        var output ="";

        for(var i in result){
          var d = new Date();

            output+="<div class='w3-col l10 m12' style='margin:10px;'><h1><span class='color_h1';>"+result[i].contentlist+" </span></h1>"+
            "<p>last update "+d.getMonth()+" months ago</span></p>"+
               "<div id ='single'>"+
                "<a id='qm'></a>";
               // "<a  onclick='questions(val=12653)' href='#'  data-toggle='modal' data-target='#mod'>Practice Question&raquo;</a>";
            output+="<div class='w3-clear nextprev'>"+
              //  "<a class='w3-left w3-btn' href='#' onclick='contents(val="+xl+")'>&#10094; Previous</a>"+
                //"<a class='w3-right w3-btn' href='/info/home/catalog/4/25/'>Next &#10095;</a>"+
            "</div><hr>";
          var cn=result[i].contents;


             for(var j in cn){

            var cont=cn[j].content.split('.');
            var im=cn[j].images;
            var mod=im.length,l;
             if(mod!=0){
               l=cont.length/mod;
            }

  output+= "<div class='bd'><h2>"+cn[j].title+"</h2>"+
                "<p>The button in front "+cn[0].title+" or behind it as a help text.</p>"+
                "<p>The <code>.input-group-addon</code> class attaches an icon or help text next to the input field.</p><br>"
                +"<div class='w3-example'>"+
                    "<div class='w3-code notranslate htmlHigh clearfix'>"+
                       "<ul>";

                              var imc=0;
                              var imgs=cn[j].images;

                              // output+="<img class='img1' src='"+imgs[0].content_pic+"' width='170' height='170'>";

                              for(var r in cont)
                            {

                              if(r%l==0)
                              {
                                for(var r in imgs)
                              {
                                  output+="<img class='img1' src='"+imgs[imc].content_pic+"' width='170' height='170'>";
                                  imc++;
                                  break;

                              }

                              }
                              output+="<li style='font-size:16px;font-weight:200;'>"+cont[r]+"</li>";
                            }

                        output+="</ul>"+
                    "</div>"+

                 "</div><br>";

              var tabletitle=cn[j].contenttable;
              var a=['cl1','cl2'];

              for(var k in tabletitle){
              var tableinfos=tabletitle[k].tableinfo
     output+="<br><p><code class='w3-codespan' >"+tabletitle[k].title+"</code></p>"+

               "<div class='w3-example' style='padding: 0.01em 5px;margin: 5px 0;'>"+

                    "<div class='w3-code notranslate htmlHigh clearfix'>"+
                        "<table id='customers'>"+
                    "<tr>"+
                        "<th>"+tabletitle[k].cl1+"</th>"+
                        "<th>"+tabletitle[k].cl2+"</th>"+
                        "<th>"+tabletitle[k].cl3+"</th>"+
                   "</t br>";
                   for(var tf in tableinfos )
                   if(tf%2==0){
                   output+="<tr>"+
                        "<td>"+tableinfos[tf].tl1+"</td>"+
                        "<td>"+tableinfos[tf].tl2+"</td>"+
                        "<td>"+tableinfos[tf].tl2+"</td>"+
                    "</tr>";
                    }else{
                    output+="<tr class='alt'>"+
                        "<td>"+tableinfos[tf].tl1+"</td>"+
                        "<td>"+tableinfos[tf].tl2+"</td>"+
                        "<td>"+tableinfos[tf].tl3+"</td>"+
                    "</tr>";
                    }
                output+="</table>"+
               "</div>"+
              "</div>";
               }



              output+="<br><div class='w3-example'>"+

                        "<a onclick='questions(val="+cn[j].id+")' href='#' class='w3-btn w3-margin-bottom'  data-toggle='modal' data-target='#mod'>Practice Question&raquo;</a>"+


                     "</div><br>";

           output+="</div>";


}




               output+="</div></div><div class='w3-col l2 m12' id='right''>"+

            "<div class='sidesection w3-light-grey' style='margin-left:auto;margin-right:auto;max-width:230px'>"+

                "<div class='w3-container w3-dark-grey'>"+

                    "<h4><a  class='w3-hover-text-white'>tropics</a></h4>"+
                "</div>"+
                "<div class='w3-container w3-left-align w3-padding-16'>";
                // alert(one+urls+pageurl +"hello");

                for(k in cn)
            {
                    output+="<a href='#' onclick='singleE(b="+result[i].id+",d="+cn[k].id+")'>"+cn[k].title+"</a><br>";
             }
                  output+="</div>"+
                 "</div>"+
            "</div>";
            }

        output += "";

        displayResources.html(output);

      }
    });
}



function questions(quesid)
{

var nameObject = {
    first: 'Joe',
    last: 'Schmoe'
};

  var x="/info/home/qu/api/"+quesid+"/";
  var displayResources = $("#qm");
$.ajax({
  type:"GET",
  url:x,
    success:function(result)
    {
    var subdisplay= $("#qut")
     out="";
      var cnt=1;
      for(var tp in result){
       var qus=result[tp].allquestion;

        for(var q in qus){
        out+="<div class='scontainer clearfix bd'>"+
        "<div class='tooltipz'>"+
               "<span class='tooltiptextz'>"+result[tp].title+"</span>"+
                       "</div>"+

        "<div class='lcontainer bd'>"+

         "<div><span style='font-size:150%;color:black;margin-left: -18px;'>"+(cnt++)+".</span><span style='font-size:120%;color:black'>"+qus[q].title+"</span> <a href='#'><span style='float:right;color:red;'>Bookmarks<span></a></div>"+

                      "<ul>"+
                           "<img src='https://images.pexels.com/photos/372297/pexels-photo-372297.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940' width='90%' height='150'>"+
                          "<li><strong class='d'> "+qus[q].que_pic+"</strong>"+
                            "</li>"
                            +"<li><strong class='d'> "+qus[q].op1+"</strong>"+
                            "</li>"+
                            "<li><strong class='d'>"+qus[q].op2+"</strong>"+
                            "</li>"+
                            "<li><strong class='d'>"+qus[q].op3+"</strong>"+
                            "</li>"+
                            "<li><strong class='d'>"+qus[q].op4+"</strong>"+
                            "</li>"+


                        "</ul>"+

        "<div class='radio img1'>"+
        "<label>"+
            "<input type='radio' name='ab"+tp+q+"' onclick='click_position(this,"+tp+","+q+")' id='ab' value='Ans : "+qus[q].ans+"'/>উত্তর</label>"+
         "</div>"+

        "<div class='radio img1'>"+
        "<label>"+
            "<input type='radio'  id='ab1' name='ab"+tp+q+"' onclick='click_position(this,"+tp+","+q+")' value='explain : "+qus[q].explain+"' class='regular-radio'' />ব্যাখ্যা</label>"+
         "</div>";
           out+="</div>"+

           "<div class='rcontainer'>";
        out+="<p id='ans"+tp+q+"'>press to get ans</p>";
           out+="</div></div><br>";
}

         "</div>";
         }
   // alert(result[0].title);
    subdisplay.html(out);
    }
});

var output="";
 output+="<div class='modal fade' id='mod' role='dialog'>"+
    "<div class='modal-dialog'>"+


      "<div class='modal-content'>"+
        "<div class='modal-header'>"+
        "<h1>QUESTION</h1>"+
          "<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>"+
        "</div>"+

        "<div id='qut' class='modal-body mcontainer clearfix '>"+
        "</div>"+
        "<div class='modal-footer'>"+
          "<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>"+
        "</div>"+
      "</div>"+

    "</div>"+
  "</div>";
  displayResources.html(output);

}

function greeting (obj) {
    alert('Hello ' + obj.first + ' ' + obj.last);
}


function singleE(a,b)
{
var displayResources = $("#single");
var url="/info/home/single/api/"+a+"/"+b+"/";
    displayResources.text("Loading data from JSON source...");

 $.ajax({
      type: "GET",
      url: url, // Using our resources.json file to serve results
      success: function(result) {
        console.log(result);
        var output ="";

            output+="<a id='qm'></a>";
            output+="<div class='w3-clear nextprev'>"+
            "</div><hr>";

            var cont=result.content.split('.');
            var im=result.images;
            var mod=im.length,l;
             if(mod!=0){
               l=cont.length/mod;
            }

  output+= "<div class='bd'><h2>"+result.title+"</h2>"+
                "<p>The button in front "+result.title+" or behind it as a help text.</p>"+
                "<p>The <code>.input-group-addon</code> class attaches an icon or help text next to the input field.</p><br>"
                +"<div class='w3-example'>"+
                    "<div class='w3-code notranslate htmlHigh clearfix'>"+
                       "<ul>";

                              var imc=0;
                              var imgs=result.images;

                              // output+="<img class='img1' src='"+imgs[0].content_pic+"' width='170' height='170'>";

                              for(var r in cont)
                            {

                              if(r%l==0)
                              {
                                for(var r in imgs)
                              {
                                  output+="<img class='img1' src='"+imgs[imc].content_pic+"' width='170' height='170'>";
                                  imc++;
                                  break;

                              }

                              }
                              output+="<li style='font-size:16px;font-weight:200;'>"+cont[r]+"</li>";
                            }

                        output+="</ul>"+
                    "</div>"+

                 "</div><br>";

              var tabletitle=result.contenttable;


              for(var k in tabletitle){
              var tableinfos=tabletitle[k].tableinfo
     output+="<br><p><code class='w3-codespan' >"+tabletitle[k].title+"</code></p>"+

               "<div class='w3-example' style='padding: 0.01em 5px;margin: 5px 0;'>"+

                    "<div class='w3-code notranslate htmlHigh clearfix'>"+
                        "<table id='customers'>"+
                    "<tr>"+
                        "<th>"+tabletitle[k].cl1+"</th>"+
                        "<th>"+tabletitle[k].cl2+"</th>"+
                        "<th>"+tabletitle[k].cl3+"</th>"+
                   "</t br>";
                   for(var tf in tableinfos )
                   if(tf%2==0){
                   output+="<tr>"+
                        "<td>"+tableinfos[tf].tl1+"</td>"+
                        "<td>"+tableinfos[tf].tl2+"</td>"+
                        "<td>"+tableinfos[tf].tl2+"</td>"+
                    "</tr>";
                    }else{
                    output+="<tr class='alt'>"+
                        "<td>"+tableinfos[tf].tl1+"</td>"+
                        "<td>"+tableinfos[tf].tl2+"</td>"+
                        "<td>"+tableinfos[tf].tl3+"</td>"+
                    "</tr>";
                    }
                output+="</table>"+
               "</div>"+
              "</div>";
               }



              output+="<br><div class='w3-example'>"+

                        "<a onclick='questions(val="+result.id+")' href='#' class='w3-btn w3-margin-bottom'  data-toggle='modal' data-target='#mod'>Practice Question&raquo;</a>"+


                     "</div><br>";



        output += "";

        displayResources.html(output);

      }
    });


}