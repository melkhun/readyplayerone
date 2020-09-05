<template>
  <div class="Home">
    <v-card
      color="blue"
      dark
      flat
      tile
    >
      <v-window v-model="onboarding">
        <v-window-item
          v-for="n in length"
          :key="`card-${n}`"
        >
          <v-card
            color="transparent"
            height="400"
          >
            <v-row
              class="fill-height"
              align="center"
              justify="center"
              tag="v-card-text"
            >
              {{newsdata}}
              Transparent themed, for background-imaged slides. Background color black added for demonstration purposes.
            </v-row>
          </v-card>
        </v-window-item>
      </v-window>

      <v-card-actions class="justify-space-between">
        <v-btn
          text
          @click="prev"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
        <v-item-group
          v-model="onboarding"
          class="text-center"
          mandatory
        >
          <v-item
            v-for="n in length"
            :key="`btn-${n}`"
            v-slot:default="{ active, toggle }"
          >
            <v-btn
              :input-value="active"
              icon
              @click="toggle"
            >
              <v-icon>mdi-record</v-icon>
            </v-btn>
          </v-item>
        </v-item-group>
        <v-btn
          text
          @click="next"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>

  </div>
</template>


<script>
// import A from '@/components/A'
// import B from '@/components/B'
// import C from '@/components/C'

// import * as apis from '@/api'

  export default {
    data: () => ({
      length: 4,
      onboarding: 0,
      newsdata: null,
    }),

    mounted (){
      // this.getNews()
    },

    methods: {
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
      // async getNews() {
      //   try {
      //     var resp = await apis.getNews()
      //     console.log(resp)
      //   } catch(e) {
      //     console.error(e)
      //   }
      // },
    },
  }
</script>
