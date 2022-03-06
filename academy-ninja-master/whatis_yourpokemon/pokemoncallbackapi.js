$(document).ready(function(){
        
    for (let i=1; i<=151; i++){
        $('.main').append('<img id='+ i +' src="https://unpkg.com/pokeapi-sprites@2.0.2/sprites/pokemon/other/dream-world/'+ i +'.svg">');
    }

        $('.main img').click(function() {
        let identifier= $(this).attr("id");
        callback_api(identifier);
    });

    function callback_api(identifier){
        $.get("https://pokeapi.co/api/v2/pokemon/"+identifier+"/", function(res) {
                let html_str = "";
                html_str += "<b>"+ res.name +"</b>";
                html_str += "</h2><p>";
                html_str += "<img src='https://unpkg.com/pokeapi-sprites@2.0.2/sprites/pokemon/other/dream-world/"+identifier+".svg'>";
                html_str += "</p><b>Types</b></p><ul>";
                
                for(let i = 0; i < res.types.length; i++) {
                    html_str += "<li>" + res.types[i].type.name + "</li>";
                }
                html_str += "</ul><b>Height</b><p>";
                html_str += res.height;
                html_str += "</p><b>Weight</b><p>";
                html_str += res.weight;             
                $(".details").html(html_str);
            }, "json");
    }
});