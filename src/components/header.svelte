<!-- Header.svelte -->
<script>
    export let title = `What's "Free" About the North American Free Trade Agreement?`
  </script>
  
  <header>
    <h1>{title}</h1>
  </header>
  
  <style>
    header {
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: none;
      padding: 5%;
    }
  
    h1 {
      font-size: 24px;
      color: #333;
      margin: 0;
    }
  </style>