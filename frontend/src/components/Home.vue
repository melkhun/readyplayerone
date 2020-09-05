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

  export default {
    data: () => ({
      length: 4,
      onboarding: 0,
    }),

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
    },
  }
</script>
