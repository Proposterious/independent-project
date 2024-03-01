<script>
	import Header from './Header.svelte';
	import '../app.css';
</script>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

</div>

<style>
	* {
		overflow: hidden;
	}
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
		background-color: lightgray;
	}
</style>
