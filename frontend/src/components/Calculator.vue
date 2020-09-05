<template>
  <div class="Calculator">
    <v-container flex colour="transparent">
      <v-row flex class="justify-center">
        <v-col cols="12" sm="4">
          <v-btn
            class="pa-5"
            min-height="100px"
            rounded
            @click="budgetFormHidden = !budgetFormHidden"
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
            min-height="100px"
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

    <!---Show Form-->

    <div v-show="budgetFormHidden">
      <v-flex xs12 sm6 offset-sm3>
        <v-card class="calculator-form" color="white">
          <v-form>
            <div class="profile-text">Your total monthly income</div>
            <v-text-field
              v-model="income"
              class="input-field"
              color="rgb(172, 193, 252)"
              label="Your total monthly income"
              required
              regular
            ></v-text-field>
            <div class="profile-text">Salary</div>
            <v-text-field
              v-model="expense"
              class="input-field"
              color="rgb(172, 193, 252)"
              label="Your total monthly expense"
              required
              regular
            ></v-text-field>

            <v-btn
              class="justify-center white--text"
              color="rgb(0, 0, 255)"
              min-width="300"
              min-height="50"
              x-large
              @click="calculateBudget"
            >
              CALCULATE
            </v-btn>
          </v-form>
        </v-card>
      </v-flex>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      budgetFormHidden: true,
      income: 0,
      expense: 0,
    };
  },
  methods: {
    calculateBudget() {
      console.log(this.recommendation);
      this.showResult = true;
    },
    currencyFormat(num) {
      return "$" + num.toFixed(0).replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,");
    },
  },
  computed: {
    calculateBudget() {
      var netCashFlow = this.income - this.expense;
      return currencyFormat(netCashFlow);
    },
  },
};
</script>

<style scoped>
.calculator-form {
  padding: 40px 40px 40px 40px;
}

.profile-text {
  padding: 10px;
  margin-top: 10px;
}
</style>
