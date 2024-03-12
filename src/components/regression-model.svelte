<script>
	// import Component
	import Katex from "./Katex.svelte"
	import RegressionResults from "./regression-results.svelte";
	// math equations

	const model = "\\Delta\\text{MFN Tariff}= \\beta_0 + \\beta_1 \\text{initial MFN} + \\beta_2dxr + \\beta_3 imf + \\beta_4 fsharec + \\beta_5 wlrcac + \\beta_6 polity + \\varepsilon ";
    
	$: math = model;
	
</script>
<div>
    <h2>Linear Regression Model</h2>
    <Katex {math} displayMode/> 

    <p>
       The above model establishes a relationship between changes in tariff rates and several non-tariff barriers that might influence said changes, such as 
       various measure of economic conditions, financial indicators and democratic stability. Our reasoning behind the chosen independent variables is as follows: 
    </p>

    <p class = list>
        1. A country's economic health may affect how willing that country is to trade with others,
        with increasing/decreasing tariff rates as a result 
        <br>
        2. Political stability, along with democratic policies, could affect a country's receptiveness to trade with others 
        <br>
        3. Financial indicators within a country, similarly, could influence a country's decision to trade
    </p>
</div>
<RegressionResults/>
<style>
    .list{
        padding:1.5%;
        width:45%;
        text-align: center;
    }
    p{
        width:60%;
        font-size: 12pt;
        margin:auto;
        line-height:150%;
    }
    div{
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    }
    h2{
        text-align: center;
    }

</style>