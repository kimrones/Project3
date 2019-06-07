
Plotly.d3.csv('resources/obesity.csv', function(err, rows){
  function unpack(rows, key) {
      return rows.map(function(row) { return row[key]; });
  }

var mydata = [{
          type: 'choropleth',
          locationmode: 'USA-states',
          locations: unpack(rows, 'code'),
          z: unpack(rows, 'Poverty'),
          text: unpack(rows, 'state'),
          zmin: 0,
          zmax: 1,
          colorscale: [
            [0, 'rgb(242,240,247)'], [0.05, 'rgb(218,218,235)'],
            [0.10, 'rgb(188,189,220)'], [0.15, 'rgb(158,154,200)'],
            [0.20, 'rgb(117,107,177)'], [0.35, 'rgb(255,0,0)']
        ],
        colorbar: {
          title: 'poverty percentage',
          thickness: 0.2
        },
        marker: {
          line:{
            color: 'rgb(255,255,255)',
            width: 2
          }
        }
      }];

console.log(mydata[0].locations);
var layout = {
      title: 'poverty percentage by state',
      geo:{
        scope: 'usa',
        showlakes: true,
        lakecolor: 'rgb(89,255,255)'
      }
  };
  Plotly.plot(myDiv, mydata, layout, {showLink: false});
});