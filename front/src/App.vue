<template>
  <div id="app">
    <div id="nav">
      <router-link to="/" v-on:click.native="reloadPage()">Home</router-link>
      |
      <router-link to="/news">News</router-link>
      |
      <router-link to="/about">About</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    reloadPage() {
      window.location.reload()
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  text-align: center;
}

#nav a {
  font-weight: bold;

  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: rgb(3, 169, 244);

  font-size: 20px;
}
</style>
