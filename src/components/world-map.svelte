<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import * as topojson from 'topojson-client';
  
    let mapContainer;
    let width = 800;
    let height = 400;
    let projection;
    let path;
    let svg;
  
    onMount(async () => {
      // Load the TopoJSON data
      const response = await fetch('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json');
      const world = await response.json();
      const desired_countries = ['Canada', 'Mexico', 'United States of America']
      let countries = topojson.feature(world, world.objects.countries).features;
      let target_countries = countries.filter((country) => desired_countries.includes(country.properties.name))
  

      const bounds = d3.geoBounds({ type: 'FeatureCollection', features: target_countries });
      const scale = Math.max(width / (bounds[0][1] - bounds[0][0]), height / (bounds[1][1] - bounds[1][0])) * 0.9;
      projection = d3.geoMercator().translate([width, height/1.4]);
      path = d3.geoPath().projection(projection);
  
      svg = d3.select(mapContainer)
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g");
  
      svg.selectAll(".country")
        .data(target_countries)
        .enter().append("path")
        .attr("class", "country")
        .attr("d", path);
    });
  </script>
  
  <div bind:this={mapContainer} class="chart"></div>