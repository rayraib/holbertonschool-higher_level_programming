let url = 'https://swapi.co/api/films/?format=json';
let results;
$.get(url, function(data, textStatus) {
    results = data['results'];
    console.log(results)
    for (let i = 0; i < results.length; i++) {
        let title = results[i]['title'];
        $('UL#list_movies').append(title + '<br/>')
    }
});