// from data.js
var tableData = data;

// select tbody 
tbody = d3.select("tbody")

// using Object.entries to get key, value data inside of the table
// and loop through them to add to the table in html
function displayData(data){ 
    tbody.text("")
    data.forEach(function(artist){
    new_tr = tbody.append("tr")
    Object.entries(artist).forEach(function([key, value]){
        new_td = new_tr.append("td").text(value)	
    })
})}

displayData(tableData)


//select the web user's input and the filter button
var InputText = d3.select("#artistname")
var button = d3.select("search-btn")

// filter data with date that the user inputs
function clickSelect(){
    //don't refresh the page!
    d3.event.preventDefault();
    //print the value that was input
    console.log(InputText.property("value"));
    //create a new table showing only the filterd data
    var new_table = tableData.filter(Artist => Artist.artist===InputText.property("value"))
    //display the new table
    displayData(new_table);
}

/*
//select the web user's input for song
var SongInput = d3.select("#songname")
var button_2 = d3.select("search-bttn")

//filter data with song input
function clickSelect(){
    d3.event.preventDefault();
    console.log(SongInput.property("value"));
    var new_table_2 = tableData.filter(Song => Song.song===SongInput.property("value"))
    displayData(new_table_2);
}
*/
// event listener to handle change and click
InputText.on("change", clickSelect)
