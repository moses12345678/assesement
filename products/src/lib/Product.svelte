<script>
  import { onMount } from "svelte";
  import svelteLogo from "./assets/svelte.svg";
  export let title;
  export let description;
  let products = [];

  onMount(async () => {
    const res = await fetch(`https://dummyjson.com/products`);
    products = await res.json();
  });
</script>

<div class="products">
  {#each products as product}
    <div class="product">
      <div class="title">{product.title}</div>
      <div class="description">{product.description}</div>
    </div>
  {:else}
    <!-- this block renders products.length === 0 -->
    <p>Fecthing data...</p>
  {/each}
</div>

<h1 class="warning">Cannot fetch products</h1>
