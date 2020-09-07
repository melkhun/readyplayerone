<template>
  <div class="Home">
    <kinesis-container class="container">
      <kinesis-element>
        <img src="@/assets/team_logov2.png" />
      </kinesis-element>
      <br />
      <kinesis-element>
        <h1>We help you go from 0 to Hero.</h1>
        <h3>
          Learn more about your financials and where to start investing in.
        </h3>
      </kinesis-element>
      <!-- background-circles-props 
      <v-container flex colour="transparent" style="padding-bottom:30">
        <v-row flex class="justify-center">
          <v-col cols="12" md="4">
            <v-btn
              min-width="260px"
              min-height="40px"
              rounded
              dark
              medium
              color="#651FFF"
              @click="$router.push('calculator')"
              >Calculate Your Finances</v-btn
            >
          </v-col>
          <v-col cols="12" md="4">
            <v-btn
              min-width="260px"
              min-height="40px"
              rounded
              dark
              medium
              color="#651FFF"
              @click="$router.push('quickstart')"
              >Start Investing
            </v-btn>
          </v-col>
        </v-row>
      </v-container>-->

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

    <!--NEWS SECTION-->

    <v-card color="#651FFF" dark flat tile>
      <div class="market-news">Latest Market News</div>
      <v-window v-model="onboarding" dark>
        <v-window-item v-for="article of articles" :key="article.url">
          <v-card color="transparent" height="400">
            <v-row align="center" justify="center">
              <v-img
                gradient="to top right, rgba(0,0,0,.3), rgba(0,0,0,.3)"
                :src="`${article.urlToImage}`"
              >
                <a :href="`${article.url}`" class="link-style">{{
                  article.description
                }}</a>
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

export default {
  data: () => ({
    length: 10,
    onboarding: 1,
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
    },
    prev() {
      this.onboarding =
        this.onboarding - 1 < 0 ? this.length - 1 : this.onboarding - 1;
    },
  },
  prev() {
    this.onboarding =
      this.onboarding - 1 < 0 ? this.length - 1 : this.onboarding - 1;
  },
};
</script>

<style scoped>
.circle {
  position: absolute;
  border-radius: 100%;
}

.circle.circle-purple {
  border: 10px solid #f2eafa;
  opacity: 0.1;
  width: 4vw;
  height: 4vw;
  left: 10%;
  top: 25%;
}

.circle.circle-purple1 {
  border: 15px solid #f2eafa;
  opacity: 0.1;
  width: 8vw;
  height: 8vw;
  right: -2%;
  bottom: 17%;
}
.circle.circle-purple2 {
  background-color: #f2eafa;
  opacity: 0.1;
  width: 5vw;
  height: 5vw;
  left: 20%;
  bottom: 17%;
}

.circle.circle-purple3 {
  border: 15px solid #f2eafa;
  opacity: 0.3;
  width: 3vw;
  height: 3vw;
  top: 80%;
  left: 60%;
}

h1 {
  color: #58039e;
  font-size: 2.5rem;
  line-height: 2.5rem;
  margin-bottom: 20px;
  margin-left: 50px;
  margin-right: 50px;
}

h3 {
  color: #3e0d69;
  font-size: 1.4rem;
  font-weight: 100 !important;
  line-height: 1.3rem;
  margin-bottom: 30px;
}

img {
  width: 10rem;
}

.v-image {
  max-height: 400px;
}

.market-news {
  font-size: 2.5rem;
  font-weight: 700;
  line-height: 2.5rem;
  padding-top: 0.7em;
  padding-bottom: 0.5em;
}
.link-style {
  display: block;
  font-size: 1.8em;
  line-height: 1.2em;
  color: white;
  margin-top: 100px;
  margin-left: 100px;
  margin-right: 100px;
  text-decoration: none;
}
</style>
