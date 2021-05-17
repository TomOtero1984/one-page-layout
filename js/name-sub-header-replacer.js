$.ajax({
    type: "GET",
    url: "data/positive-vibes.csv",
    dataType: "text",
    success: (res)=>{pos_vibes_data = $.csv.toArrays(res)}
  });

function sub_name_header_replace(){
    new_vibes = get_vibes();
    document.getElementById("name-sub-header").innerHTML = `${new_vibes[0]} | ${new_vibes[1]} | ${new_vibes[2]}`;
}

function get_vibes(){
    var MAX = pos_vibes_data[0].length - 1
    console.log((Math.round(MAX*Math.random())))
    var index = [Math.round(MAX*Math.random()),
                 Math.round(MAX*Math.random()),
                 Math.round(MAX*Math.random())]
    console.log(index)             
    var new_vibes = [capitalize(pos_vibes_data[0][index[0]]),
                     capitalize(pos_vibes_data[0][index[1]]),
                     capitalize(pos_vibes_data[0][index[2]])]
    return new_vibes;
}

function capitalize(word){
    return word.charAt(0).toUpperCase() + word.slice(1)
}