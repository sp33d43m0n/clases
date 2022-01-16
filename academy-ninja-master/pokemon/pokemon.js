$(document).ready(function() {
        $('h1').click(function() {
            for (let i=1; i<=80; i++) {
            $('.container').append('<img src="https://unpkg.com/pokeapi-sprites@2.0.2/sprites/pokemon/other/dream-world/'+ i +'.svg">');
            }
        });
});


