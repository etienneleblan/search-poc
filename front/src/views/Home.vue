<template>
  <div class="home">
    <h1 class="title is-2">Search for some Zinio articles:</h1>

    <div class="control has-icons-left" style="max-width:300px; margin: auto;">
      <input
        class="input has-icons-left"
        type="text"
        v-model.lazy="query"
        placeholder="search something"
      />
      <span class="icon is-medium is-left">
        <i class="fas fa-search"></i>
      </span>
    </div>

    <br />
    <ArticleList :msg="query" :loading="false" />
    <br />
    <h2 class="title is-3">Or read about some trending topics:</h2>
    <div class="trending columns">
      <div class="column">
        <h3 class="title is-4">iPhone 12</h3>
        <ArticleList msg="iPhone 12" />
      </div>
      <div class="column">
        <h3 class="title is-4">Nvidia</h3>
        <ArticleList msg="Nvidia" />
      </div>
      <div class="column">
        <h3 class="title is-4">Borat</h3>
        <ArticleList msg="Borat" />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'Home',
  components: {
    ArticleList
  },
  data() {
    return {
      query: ''
    }
  }
}
</script>
<style scoped>
.home {
  text-align: center;
  margin: 0 1em;
}
h3 {
  text-decoration: underline rgb(3, 169, 244);
}
</style>
