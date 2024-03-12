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

        <div>
            <div class=paragraph>
                The countries on the left represent participating countries under NAFTA, which includes the United States of America. According to 
                the US International Trade Administration: 

                <div class = quoteblock>
                    <p>
                    “FTAs can help your company to enter and compete more easily in the global marketplace through zero or reduced tariffs and 
                    other provisions...This makes it easier and cheaper for U.S. companies to export their products and services 
                    to trading partner markets.”
                    </p>
                </div>

                However, this is not always the case. There are usually many factors that determine trading volume between countries, including
                non-tariff barriers, which we call NTBs. The purpose of our study is to determine how effective can NTBs be used to predict 
                trade between countries. 
            </div>

        </div>
    </div>
</div>

<style>

    .quoteblock{
        width:70%;
        margin: auto;
        border-left:solid 5px #dad9d9;
        background-color: #f5f5f5c7;
        margin-top:3%;
    }
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

    .paragraph{
        line-height: 150%;

        padding-top:1%;
    }

    p{
        padding:3%;
        text-align: center;
    }

    h2{
        text-align: center;
    }

</style>
