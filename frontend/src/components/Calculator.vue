<template>
  <div class="Calculator">
    <v-container flex colour="transparent">
      <v-row class="justify-center">
        <v-col cols="12" sm="4">
          <v-btn
            class="pa-5"
            min-height="150px"
            rounded
            @click="budgetCalculator"
          >
            <span class="text-blue">Budget Calculator</span>

            <v-img
              src="../assets/money.svg"
              contain
              height="80px"
              width="80px"
            ></v-img>
          </v-btn>
        </v-col>
        <v-col cols="12" sm="4">
          <v-btn
            class="pa-5"
            min-height="150px"
            rounded
            @click="assetCalculator"
          >
            <span class="text-blue">Asset Calculator</span>

            <v-img
              src="../assets/assets.svg"
              contain
              height="80px"
              width="80px"
            ></v-img>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  methods: {
    budgetCalculator() {
        console.log(this.recommendation)
        this.showResult = true
      },
  }
};
</script>
