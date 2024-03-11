<script>
    import * as d3 from 'd3';
    import { onMount } from 'svelte';

    let data = [];
    let columns = [];

    function getCellColor(value) {
        if (!isNaN(parseFloat(value))) {
            const absValue = Math.abs(value);
            if (value >= 0) {
                // Positive value, use shades of green
                if (absValue < 0.2) {
                    return 'very-low-positive';
                } else if (absValue < 0.4) {
                    return 'low-positive';
                } else if (absValue < 0.6) {
                    return 'medium-positive';
                } else if (absValue < 0.8) {
                    return 'high-positive';
                } else {
                    return 'very-high-positive';
                }
            } else {
                // Negative value, use shades of red
                if (absValue < 0.2) {
                    return 'very-low-negative';
                } else if (absValue < 0.4) {
                    return 'low-negative';
                } else if (absValue < 0.6) {
                    return 'medium-negative';
                } else if (absValue < 0.8) {
                    return 'high-negative';
                } else {
                    return 'very-high-negative';
                }
            }
        } else {
            return value;
        }
    }

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
          <td class={getCellColor(row[column])}>{row[column]}</td>
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
{/if}

<style>
    table {
        background-color: #fff;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
        border-collapse: collapse;
        width: 100%;
    }

    thead {
        background-color: #f2f2f2;
    }

    th, td {
        padding: 12px 15px;
        text-align: left;
    }

    th {
        font-weight: bold;
    }

    tr td:first-child{
        font-weight: bold;
        background-color: #f2f2f2;
        border:none;
        text-align: center;
    }

    tbody tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    tbody tr:hover {
        background-color: #e6e6e6;
    }

    .very-low-positive {
        background-color: #e8f5e9;
    }

    .low-positive {
        background-color: #c8e6c9;
    }

    .medium-positive {
        background-color: #a5d6a7;
    }

    .high-positive {
        background-color: #81c784;
    }

    .very-high-positive {
        background-color: #66bb6a;
    }

    .very-low-negative {
    background-color: #ffcdd2;
    }

    .low-negative {
        background-color: #ef9a9a;
    }

    .medium-negative {
        background-color: #e57373;
    }

    .high-negative {
        background-color: #e53935;
    }

    .very-high-negative {
        background-color: #c62828;
    }
</style>