<script>
    import Independence from "./Independence.svelte";
</script>

<div class = 'parent'>
    <div class = 'left'>
        <h2>Correlation Heat Map</h2>
        <Independence/>
    </div>
    
    <div class = 'right'>
        <h2>Independent Variables</h2>
        <ol>
            <li><b>l_lnsmfn:</b>  (MFN tariff measure) is not a non-tariff barrier, but a baseline, adjusted variable representing the initial tariff level.</li>
            <li><b>dxr:</b> The percentage change in real exchange rate between tariff observations, which can impact trade flows and potentially 
                influence tariff rates.</li>
            <li><b>imf:</b> The number of years a country received loans from the International Monetary Fund (IMF), 
                which may be associated with certain trade policy conditions or reforms.</li>
            <li><b>fsharec:</b> The mean center of Intra-FTA (Free Trade Agreement) trade as a percentage of total trade 
                from 1990 to 1995, representing the level of trade integration within an FTA bloc.</li>
            <li><b>wlrcac:</b>  The mean center of an output-weighted measure of a country's comparative advantage based 
                on the Revealed Comparative Advantage (RCA) index.</li>
            <li><b>polity:</b> A measure of a country's level of democracy, which may influence trade policies and tariff rates.</li>
        </ol>
    </div>
</div>


<style>
    .parent{
        padding: 5%;
        display:flex;
        justify-content: space-around;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;

    }

    .left{
        text-align: center;
        width:40%;
    }
    .right{
        text-align: center;
        width: 40%;
    }

    ol{
        text-align: center;
        line-height: 150%;
    }


</style>
