<script>
    import { onMount } from 'svelte';
    import Plot from 'svelte-plotly.js';

    let plotData;

    onMount(async () => {
        const response = await fetch('https://raw.githubusercontent.com/jww2145/free-trade-agreements/main/data-exploration/plot_data.json');
        plotData = await response.json();
    });
</script>

{#if plotData}
    <Plot data={plotData} />
{:else}
    <p>Loading...</p>
{/if}