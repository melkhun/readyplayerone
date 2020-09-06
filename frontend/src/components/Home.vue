<template>
  <div class="Home">

  <kinesis-container class="container">
      <kinesis-element>
        <!-- LogRocket logo -->
      </kinesis-element>

      <!-- background-circles-props -->
      <kinesis-element axis="y">
        <div class="circle circle-purple"></div>
      </kinesis-element>
      <kinesis-element axis="y">
        <div class="circle circle-purple1"></div>
      </kinesis-element>
      <kinesis-element axis="y">
        <div class="circle circle-purple2"></div>
      </kinesis-element>
      <kinesis-element axis="y">
        <div class="circle circle-purple3"></div>
      </kinesis-element>
    </kinesis-container>
    <v-card color="blue" dark flat tile>
      <v-window v-model="onboarding" dark>
        <v-window-item v-for="article of articles" :key="article.url">
          <v-card color="transparent" height="400">
            <v-row class="fill-height" align="center" justify="center">
              <v-img
                gradient="to top right, rgba(0,0,0,.3), rgba(0,0,0,.3)"
                :src="`${article.urlToImage}`"
              >
                <v-card-title>
                  <a :href="`${article.url}`">{{ article.description }}</a>
                </v-card-title>
              </v-img>
            </v-row>
          </v-card>
        </v-window-item>
      </v-window>

      <v-card-actions class="justify-space-between">
        <v-btn text @click="prev">
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
        <v-item-group v-model="onboarding" class="text-center" mandatory>
          <v-item
            v-for="n in length"
            :key="`btn-${n}`"
            v-slot:default="{ active, toggle }"
          >
            <v-btn :input-value="active" icon @click="toggle">
              <v-icon>mdi-record</v-icon>
            </v-btn>
          </v-item>
        </v-item-group>
        <v-btn text @click="next">
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { getNews } from "../api";

<<<<<<< HEAD
export default {
  data: () => ({
    length: 4,
    onboarding: 0,
    articles: [],
  }),
  mounted() {
    this.getNews();
  },
  methods: {
    async getNews() {
      try {
        var resp = await getNews();
        this.articles = resp.articles;
        console.log(this.articles);
      } catch (e) {
        console.error(e);
      }
    },
    next() {
      this.onboarding =
        this.onboarding + 1 === this.length ? 0 : this.onboarding + 1;
=======
  export default {
    data: () => ({
      length: 4,
      onboarding: 0,
      articles: []
    }),
    mounted() {
      // this.getNews()
    },
    methods: {
      async getNews() {
        try {
          var resp = await getNews()
          this.articles = resp.articles
          // console.log(this.articles)
        } catch(e) {
          console.error(e)
        }
      },
      next () {
        this.onboarding = this.onboarding + 1 === this.length
          ? 0
          : this.onboarding + 1
      },
      prev () {
        this.onboarding = this.onboarding - 1 < 0
          ? this.length - 1
          : this.onboarding - 1
      },
>>>>>>> b6b7d4fa8042ac9041eb097c53079481252ca32d
    },
    prev() {
      this.onboarding =
        this.onboarding - 1 < 0 ? this.length - 1 : this.onboarding - 1;
    },
  },
};
</script>

<style scoped>
.v-image {
  max-height: 400px;
}

.v-window >>> .v-window-item >>> .v-card >>> .v-row >>> .v-img >>> .v-card-title >>> a {
  padding: 20 20 20 20;
  text-align: center;
  font-size: 1.2rem;
  color: white;
}
</style>
