

var data =[{labels: ['danceability','acousticness','loudness','energy','duration','speechiness','valence','tempo','liveness','instrumentalness','key','mode','time-signature'],
            values: ['.104','.099','.095','.094','.093','.093','.092','.089','.087','.084','.05','.01'],
            type: "pie"
}];

var layout = {height: 400,
                width: 500,


};

Plotly.newPlot('features',data,layout);