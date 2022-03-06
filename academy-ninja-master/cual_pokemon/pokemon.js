$(document).ready(function() {
        $.get("https://pokeapi.co/api/v2/pokemon/1/", function(res) {
            console.log(res);
            return res;
            }, "json");
        $('h1').click(function() {
            for (let i=1; i<=80; i++) {
            $('.main').append('<img id='+ i +' src="https://unpkg.com/pokeapi-sprites@2.0.2/sprites/pokemon/other/dream-world/'+ i +'.svg">');
            }
        });
        $('.main img').click(function() {
            const identifier = $(this).attr("id");
            alert(identifier);
            });
});


