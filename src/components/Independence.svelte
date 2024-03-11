<script>
    import * as d3 from 'd3';
    import { onMount } from 'svelte';

    let data = [];
    let columns = [];

    onMount(async () => {
        const csvUrl = 'https://raw.githubusercontent.com/jww2145/free-trade-agreements/main/data-exploration/correlation_matrix.csv'

        // Use the d3.csv() function to fetch the CSV data
        const rawData = await d3.csv(csvUrl);

        console.log(rawData)
        // Extract column names from the first row
        columns = Object.keys(rawData[0]);

        // Parse the data into an array of objects with column names as keys
        data = rawData.map(row => {
            const obj = {};
            columns.forEach(col => {
                obj[col] = isNaN(parseFloat(row[col])) ? row[col] : formatNumber(Number(row[col])); // Convert string to number
            });
            return obj;
        });

    });

    function formatNumber(value) {
            return value ? value.toFixed(4) : ''; // Truncate to 4 decimal places
        }
</script>
  
{#if columns.length > 0 && data.length > 0}
  <table>
    <thead>
      <tr>
        {#each columns as column}
          <th>{column}</th>
        {/each}
      </tr>
    </thead>
    <tbody>
      {#each data as row}
        <tr>
          {#each columns as column}
            <td>{row[column]}</td>
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
{/if}

<style>
    table{
        background-color: #fffdfd;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    }
    tbody{
        text-align: center;
    }

    tr td:first-child{
        font-weight: bold;
    }
</style>