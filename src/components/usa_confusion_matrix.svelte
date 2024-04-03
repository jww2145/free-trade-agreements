<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
  
    let data = [];
    let width = 500;
    let height = 500;
    let margin = { top: 100, right: 120, bottom: 50, left: 120 };
  
    // Define the nicknames and their corresponding original names
    const nicknames = {
      'Value in Billions USD_Export': 'Exports',
      'Value in Billions USD_Import': 'Imports',
      'Quantity in Million Metric Tons_Export': 'Exp. Qty',
      'Quantity in Million Metric Tons_Import': 'Imp. Qty',
      'Tariff_Rates': 'Tariffs',
      'Mortgage_Rates': 'Mortgage',
      'Interest_Rates': 'Interest',
      'Median_Household_Income': 'Income',
      'Inflation_Rate': 'Inflation',
      'GDP': 'GDP',
      'S&P 500 Returns by Year': 'S&P 500',
      'Employment Rate': 'Employment',
      'Percent of Democrats in Congress': 'Democrats',
      'Revenue of Strip Clubs in the US (billions)': 'Strip Clubs'
    };

    const columnOrder = [
    'Exports', 'Imports', 'Exp. Qty', 'Imp. Qty', 'Tariffs', 'Mortgage',
    'Interest', 'Income', 'Inflation', 'GDP', 'S&P 500', 'Employment',
    'Democrats', 'Strip Clubs'
  ];

  
    onMount(async () => {
        
      // Load the CSV data
      data = await d3.csv(`https://raw.githubusercontent.com/jww2145/free-trade-agreements/main/data-exploration/correlation_usa.csv`);

  
      // Remove the first column (empty column)
      data.forEach(d => delete d['']);
  
      // Get the column names
      const columns = Object.keys(data[0]);


    // Replace the original column names with their nicknames
    data.forEach(d => {
      columns.forEach(column => {
        const nickname = nicknames[column];
        if (nickname) {
          d[nickname] = d[column];
          if (column !== nickname) {
            delete d[column];
          }
        }
      });
    });

        // Get the updated column names in the desired order
        const nicknameColumns = columnOrder.filter(column => data[0].hasOwnProperty(column));
    console.log('Nickname columns:', nicknameColumns);


  

  
      // Create a color scale
      const colorScale = d3.scaleSequential()
        .domain([1, -1])
        .interpolator(d3.interpolateRdBu);
  
      // Create the SVG element
      const svg = d3.select('#heatmap')
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);
  
      // Create the rows
      const row = svg.selectAll('.row')
        .data(data)
        .enter().append('g')
        .attr('class', 'row')
        .attr('transform', (d, i) => `translate(0,${i * height / data.length})`);
  
      // Create the cells
      const cell = row.selectAll('.cell')
        .data(d => nicknameColumns.map(column => ({ column, value: d[column] })))
        .enter().append('rect')
        .attr('class', 'cell')
        .attr('x', (d, i) => i * width / nicknameColumns.length)
        .attr('width', width / nicknameColumns.length)
        .attr('height', height / data.length)
        .attr('fill', d => colorScale(d.value));
  
      // Create the column labels
      const columnLabels = svg.append('g')
  .selectAll('.column-label')
  .data(nicknameColumns)
  .enter().append('text')
  .attr('class', 'column-label')
  .attr('x', (d, i) => i * width / nicknameColumns.length + width / nicknameColumns.length / 2)
  .attr('y', -70)
  .attr('text-anchor', 'middle')
  .attr('transform', (d, i) => `rotate(-45, ${i * width / nicknameColumns.length + width / nicknameColumns.length / 2}, -70)`)
  .text(d => {
    return d;
  });
  
      // Create the row labels
      const rowLabels = svg.append('g')
        .selectAll('.row-label')
        .data(data)
        .enter().append('text')
        .attr('class', 'row-label')
        .attr('x', -5)
        .attr('y', (d, i) => i * height / data.length + height / data.length / 2)
        .attr('text-anchor', 'end')
        .attr('dominant-baseline', 'middle')
        .text((d, i) => nicknameColumns[i]);
  
      // Create the legend
      const legend = svg.append('g')
        .attr('class', 'legend')
        .attr('transform', `translate(${width + 20}, 0)`);
  
      const legendScale = d3.scaleLinear()
        .domain(colorScale.domain())
        .range([height, 0]);
  
      const legendAxis = d3.axisRight(legendScale)
        .tickSize(10)
        .tickFormat(d3.format('.2f'));
  
      legend.append('g')
        .attr('class', 'legend-axis')
        .call(legendAxis);
  
      legend.selectAll('.legend-rect')
        .data(d3.range(height))
        .enter().append('rect')
        .attr('class', 'legend-rect')
        .attr('x', 0)
        .attr('y', d => d)
        .attr('width', 20)
        .attr('height', 1)
        .attr('fill', d => colorScale(legendScale.invert(d)));
  
      // Create the key
      const key = svg.append('g')
        .attr('class', 'key')
        .attr('transform', `translate(0, ${height + 20})`);
  
      key.append('text')
        .attr('class', 'key-title')
        .attr('x', 0)
        .attr('y', 0)
        .text('Key:');
  
      const keyItems = key.selectAll('.key-item')
        .data(Object.entries(nicknames))
        .enter().append('g')
        .attr('class', 'key-item')
        .attr('transform', (d, i) => `translate(0, ${(i + 1) * 20})`);
  
      keyItems.append('text')
        .attr('class', 'key-label')
        .attr('x', 0)
        .attr('y', 0)
        .text(d => `${d[1]}: ${d[0]}`);
    });
  </script>
  
  <style>
    #heatmap {
      display: flex;
      justify-content: center;
      align-items: center;
    }
  
    .cell:hover {
      stroke: black;
      stroke-width: 2px;
    }
  
    .column-label {
      font-size: 10px;
      text-anchor: end;
      dominant-baseline: middle;
    }
  
    .key {
      font-size: 12px;
    }
  
    .key-title {
      font-weight: bold;
    }
  </style>
  
  <div id="heatmap"></div>