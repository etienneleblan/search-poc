<template>
  <div v-if="article.image[0]" class="article box ">
    <router-link
      :to="{
        name: 'Article',
        params: {
          article: article,
          articleId: article.id,
          issueId: article.issue.issue_zenith_id
        }
      }"
    >
      <article class="media columns is-mobile">
        <div class="img media-left column is-one-third">
          <img
            :src="
              'https://' +
                article.site_url +
                (article.image[0] && article.image[0].image_url)
            "
          />
        </div>
        <div class="media-content column">
          <div class="details content">
            <h3 class="story-title title is-5 is-marginless">
              {{ article.name }}
            </h3>
            <h5 class="pub-name" style="margin: 0.5em 0">
              {{ article.publication.name }}
            </h5>
            <p class="excerpt">{{ article.excerpt }}</p>
            <div class="meta is-flex">
              <div class="reading-time">
                <span
                  class="icon is-small has-text-grey"
                  style="margin-right: 0.5em;"
                >
                  <i class="fas fa-clock"></i>
                </span>
                <span> &nbsp; {{ article.reading_time }}' read</span>
              </div>
              <span class="article-date">{{
                dateCalc(article.modified_at)
              }}</span>
            </div>
          </div>
        </div>
      </article>
    </router-link>
  </div>
</template>

<script>
import TimeAgo from 'javascript-time-ago'
import en from 'javascript-time-ago/locale/en'

TimeAgo.addLocale(en)
const timeAgo = new TimeAgo('en-US')

export default {
  props: {
    article: Object
  },
  methods: {
    dateCalc(date) {
      let myDate = new Date(date)
      let result = myDate.getTime()
      return timeAgo.format(result)
    }
  }
}
</script>

<style scoped lang="scss">
.article {
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.15);
  transition: box-shadow 0.3s !important;
  &:hover {
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
  }
}
a {
  color: black;
}

.meta {
  .reading-time {
    background-color: #f5f5f5;
    padding: 0 0.5em;
    border-radius: 3px;
    display: flex;
    align-items: center;
  }
  .article-date {
    margin: auto;
    color: grey;
  }
}
.story-title {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* number of lines to show */
  -webkit-box-orient: vertical;
}

.excerpt {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4; /* number of lines to show */
  -webkit-box-orient: vertical;
}

h5 {
  color: grey !important;
}
.box {
  padding: 1em;
  margin: 1em;
  max-width: 500px;
}
img {
  max-height: 200px;
}
</style>
