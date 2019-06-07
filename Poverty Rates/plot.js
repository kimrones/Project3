function init() {
    var data = [{
      values: [19, 26, 55, 88],
      labels: ["Poverty","Above Poverty"],
      type: "pie"
    }];
  
    var layout = {
      height: 600,
      width: 800
    };
  
    Plotly.plot("pie", data, layout);

    var selector = d3.select("#selDataset");
    d3.json("api/all").then((data)=>{
        data.county.forEach(county => {
            selector
            .append('option')
            .text(county)
            .property('value', county)
        
        });

    });
  }
  
  function updatePlotly(newdata) {
    var PIE = document.getElementById("pie");
    Plotly.newPlot(PIE, "values", [newdata]);
    d3.json('api/all').then((result)=>{
        result

    });
  }
  
  function getData(dataset) {
    var data = [];
    switch (dataset) {
    case "dataset1":
      data = [53.5,46.7];
      break;
    case "dataset2":
      data = [48.7,51.3];
      break;
    case "dataset3":
      data = [48,52];
      break;
    case "dataset4":
      data = [46.4,53.6];
      break;
    case "dataset5":
      data = [45.6,54.4];
      break;
    case "dataset6":
      data = [45.3,54.7];
      break;
    case "dataset7":
      data = [43.4,56.6];
      break;
    case "dataset8":
      data = [43,57];
      break;
    case "dataset9":
      data = [42.7,57.3];
      break;
    default:
      data = [42.2,57.8];
    }
    updatePlotly(data);
  }
  
  init();
  