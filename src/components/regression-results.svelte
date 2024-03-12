<h3>Regression Results</h3>
<table id = 'regression-table'>
    <thead>
        <td></td>
        <td>coef</td>
        <td>std err</td>
        <td>z</td>
        <td>P > |z|</td>
        <td>[0.025</td>
        <td>.975]</td>
    </thead>
    <tr>
        <td>constant</td>
        <td>1.1532</td>
        <td>0.318</td>
        <td>3.622</td>
        <td>0.000</td>
        <td>0.529</td>
        <td>1.777</td>
    </tr>
    <tr>
        <td>l_lnsmfn</td>
        <td>-0.4776</td>
        <td>0.114</td>
        <td>-4.208</td>
        <td>0.000</td>
        <td>-0.700</td>
        <td>-0.255</td>
    </tr>
    <tr>
        <td>dxr</td>
        <td>-0.2784</td>
        <td>0.299</td>
        <td>-0.931</td>
        <td>0.352</td>
        <td>-0.307</td>
        <td>-0.864</td>
    </tr>
    <tr>
        <td>imf</td>
        <td>-0.0604</td>
        <td>0.020</td>
        <td>-3.001</td>
        <td>0.003</td>
        <td>0.021</td>
        <td>-0.100</td>
    </tr>
    <tr>
        <td>fsharec</td>
        <td>-0.0005</td>
        <td>0.003</td>
        <td>-0.164</td>
        <td>0.870</td>
        <td>-0.006</td>
        <td>0.005</td>
    </tr>
    <tr>
        <td>wlrcac</td>
        <td>-0.1584</td>
        <td>0.144</td>
        <td>1.096</td>
        <td>0.273</td>
        <td>-0.125</td>
        <td>0.441</td>
    </tr>
    <tr>
        <td>polity</td>
        <td>-0.0345</td>
        <td>0.012</td>
        <td>-2.824</td>
        <td>0.005</td>
        <td>-0.058</td>
        <td>-0.011</td>
    </tr>
</table>

<script>
    import { onMount } from "svelte";
    const alphaValue = 0.05;

    onMount(async () =>{
        const pValueCells = await document.querySelectorAll('table tr td:nth-child(5)');

    pValueCells.forEach(cell => {
        const pValue = parseFloat(cell.textContent);
        if (pValue < alphaValue) {
            cell.style.backgroundColor = "#ffcdd2";
        }
});
    })
</script>


<style>
    h3{
        text-align: center;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    }
    
    table {
        background-color: #fff;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
        border-collapse: collapse;
        width: 60%;
        margin:auto;
        padding:2%;
    }

    thead {
        background-color: #f2f2f2;
    }

    td {
        padding: 12px 15px;
        text-align: left;
    }


    tr td:first-child{
        background-color: #f2f2f2;
        border:none;
        text-align: center;
    }

    tr td:first-child{
        font-weight: bold;
        background-color: #f2f2f2;
        border:none;
        text-align: center;
    }

    tr:nth-child(even) {
        background-color: #f5f5f5;
    }

</style>