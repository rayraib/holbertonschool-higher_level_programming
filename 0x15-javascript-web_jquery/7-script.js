let url = "https://swapi.co/api/people/5/?format=json";
$.get(url, function(data, textStatus){
    let name = data['name'];
    console.log(name)
    $('#character').text(name);
});