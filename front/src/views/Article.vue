<template>
  <div>
    <div v-if="loading">
      <p style="text-align: center;">
        Loading...
      </p>
      <b-progress
        size="is-large"
        style="max-width:500px; margin:auto;"
      ></b-progress>
    </div>
    <div class="columns">
      <VueScrollProgressBar height="0.5rem" />
      <div class="column is-one-fifth">
        <div class="box info">
          <div class="">
            <p>
              <strong>Reading time:</strong> <br />{{ article.reading_time }}
              min
            </p>
            <p>
              <strong>Published: </strong><br />{{
                dateCalc(article.modified_at)
              }}
            </p>
          </div>
          <div class="">
            <p>
              <strong>Publication: </strong><br />{{ article.publication.name }}
            </p>
            <p><strong>Issue: </strong><br />{{ article.issue.issue_name }}</p>
          </div>
          <div class="" style="text-align:center;">
            <br />
            <img
              :src="article.issue.issue_cover_image"
              alt="cover"
              style="max-height:130px;"
            />
          </div>
        </div>
      </div>

      <div
        v-if="articleContent && articleContent.content && articleCssStyle"
        v-html="articleContent.content"
        class=" article-content column is-three-fifths"
        style="z-index:-99;"
      ></div>
      <div class="column is-one-fifth"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import TimeAgo from 'javascript-time-ago'
import en from 'javascript-time-ago/locale/en'
import { VueScrollProgressBar } from '@guillaumebriday/vue-scroll-progress-bar'

TimeAgo.addLocale(en)
const timeAgo = new TimeAgo('en-US')

export default {
  name: 'Article',
  components: {
    VueScrollProgressBar
  },
  data() {
    return {
      article: this.$route.params.article,
      loading: false,
      articleContent: null,
      articleCssStyle: null,
      articleCssFonts: null,
      baseURL: process.env.VUE_APP_BACKEND_BASE_URL,
      contentEndpoint: process.env.VUE_APP_CONTENT_ENDPOINT
    }
  },
  watch: {
    articleCssStyle: function(item) {
      this.appendFile(item)
      this.loading = false
    },
    articleCssFonts: function(item) {
      this.appendFile(item)
    }
  },
  mounted() {
    const fullPath =
      this.contentEndpoint +
      this.$route.params.issueId +
      '/stories/' +
      this.$route.params.articleId
    this.loading = true
    axios
      .get(this.baseURL + fullPath, {
        params: {
          css_content: true
        }
      })
      .then((res) => {
        this.articleContent = res.data.data
        this.articleCssStyle = res.data.data.template.css[1]
        this.articleCssFonts = res.data.data.template.css[0]
      })
  },
  // Required so that new styles get fetched for every story
  beforeDestroy() {
    this.destroyFile(this.articleCssStyle)
    this.destroyFile(this.articleCssFonts)
  },
  methods: {
    dateCalc(date) {
      let myDate = new Date(date)
      let result = myDate.getTime()
      return timeAgo.format(result)
    },
    /* Used to append template files in head */
    appendFile(item) {
      let file = document.createElement('link')
      file.rel = 'stylesheet'
      file.href = item
      file.setAttribute('id', item)
      document.head.appendChild(file)
      return item
    },
    /* removing template when leaving the story. not great.
    should instead cache the file and only load if new */

    destroyFile(item) {
      const file = document.getElementById(item)
      file.parentElement.removeChild(file)
    }
  }
}
</script>

<style scoped>
.info {
  display: flex;
  flex-direction: column;
  max-height: 500px;
  max-width: 200px;
  position: fixed;
  margin-left: 2em;
}

.article-content {
  margin: auto;
  max-width: 800px;
  margin-top: -2em !important;
}
</style>
