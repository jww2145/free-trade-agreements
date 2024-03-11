<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import * as topojson from 'topojson-client';
  
    let mapContainer;
    let width = 1000;
    let height = 500;
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
      projection = d3.geoMercator().translate([width, height/.95]).scale(200);
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
        .attr("d", path)
        .attr("fill", "#cccccc")
        .attr("stroke", "#000000")
        .attr("stroke-width", 0.4);
    });
  </script>
  <div class = 'parent'>  
    <div bind:this={mapContainer} class="chart"></div>
    <div class = 'intro'>
        <b>Do Free Trade Agreements Really Promote Trade?</b>

        <p>“FTAs are treaties between two or more countries designed to reduce or eliminate certain barriers to trade and investment, 
            and to facilitate stronger trade and commercial ties between participating countries.” </p>
        <p>- Australian Department of Foreign Affairs and Trade</p>
        <p> However, this is not always true. In some cases, FTAs can limit trade between countries even more than before, 
            especially if the comparative benefits are not the same. To the left are the member countries of the North American Free Trade Agreement,
        or NAFTA. </p>

        <p> Including to the International Trade Administration: </p>
        
        <p>"Reduction or elimination of tariffs on qualified. For example, a country that normally 
            charges a tariff of 12% of the value of the incoming product will eliminate that tariff for products that originate (as defined in the FTA)
             in the United States.”
        </p>

        <p> But, the ITA does not mention about other barriers that prevent trade between countries. We call these <b>non-tarrif barriers</b> to trade, or NTBs for short</p>

    </div>
</div>

<style>
    .parent{
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-left:-10%;
    }

    .chart{
        margin-left: -10%;
    }

    .intro{
        width:40%;
        margin-left:-10%;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
        font-size: 12pt;
    }

</style>
