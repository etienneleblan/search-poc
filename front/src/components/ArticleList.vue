<template>
  <div>
    <div v-if="loading">
      Loading...
      <b-progress
        size="is-large"
        style="max-width:500px; margin:auto;"
      ></b-progress>
    </div>
    <div class="article-list">
      <div v-for="article in articles" :key="article.id">
        <ArticleListCard :article="article" />
      </div>
    </div>
  </div>
</template>

<script>
import ArticleListCard from '@/components/ArticleListCard.vue'

import axios from 'axios'

export default {
  name: 'ArticleList',
  props: {
    msg: String
  },
  components: {
    ArticleListCard
  },
  data: function() {
    return {
      articles: [],
      loading: false,
      query: this.msg,
      baseURL: process.env.VUE_APP_BACKEND_BASE_URL,
      searchEndpoint: process.env.VUE_APP_SEARCH_ENDPOINT
    }
  },
  watch: {
    msg: function(newVal, oldVal) {
      console.log('Prop changed: ', newVal, ' | was: ', oldVal)
      this.query = newVal
      this.runSearch()
      this.loading = true
    }
  },
  mounted() {
    this.runSearch()
  },
  methods: {
    runSearch() {
      if (this.query && this.query !== '') {
        this.loading = true
        console.log(this.searchEndpoint)
        axios
          .get(this.baseURL + this.searchEndpoint, {
            params: {
              q: this.msg,
              locale: 'en_US'
            }
          })
          .then((res) => {
            this.articles = res.data.data
          })
          .finally(() => (this.loading = false))
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.list-page {
  text-align: center;
  margin: auto;
}

.article-list {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}
h5 {
  color: grey !important;
}

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: rgb(3, 169, 244);
}
</style>
