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
            <div class="content">
                <p>
                  When two countries agree to a bilateral trade agreement, is the resulting increase in trade volume because of the FTA?
                  As an example, let us look towards the 1994 North American Free Trade Agreement (NAFTA) and the difference between
                  United States's imports of goods and services (IMPGS) following the agreement versus before.
                  From 1989 to 1994, the US had 12,928.263 billions of dollars worth of goods.
                  However, after NAFTA was established, the US had an import volume of 19,405.701.
                  Indeed, the current biggest trading partners for the United States in the current day are Canada and Mexico, with both countries pushing beyond China.
                  Now, the question is was the increase in import volume because of NAFTA or a reduction in some non-tariff barriers?
                </p>
                <p>
                  The question is pertinent because NAFTA is not the ideal bilateral agreement.
                  In May 2024, Canada has raised some concerns over unfair tariffs on softwood lumber,
                  showcasing the existence of tariffs within a bilateral trade agreement.
                  Earlier in March 2024, senators Sherrod Brown and Tom Cotton introduced the "Stop Mexico's Steel Surge Act,"
                  that would reinstate 232 tariffs on the Mexican steel industry. In the eyes of NAFTA, both actions would decrease
                  the amount of imports the US would receive, yet from Q2 2023 to Q1 2024, United States's IMPGS has been on an upward trend.
                </p>
              </div>

        </div>
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

    .content {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }

  p {
    margin-bottom: 20px;
    line-height: 1.6;
    text-align: justify;
  }

</style>
