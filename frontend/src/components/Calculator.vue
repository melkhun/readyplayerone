<template>
  <div class="Calculator">
    <v-container flex colour="transparent">
      <v-row flex class="justify-center">
        <v-col cols="12" sm="4">
          <v-btn
            class="pa-5"
            min-height="100px"
            rounded
            @click="handleBudgetClick()"
          >
            <span class="text-blue"><b>Budget Calculator</b></span>

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
            @click="handleAssetClick()"
          >
            <span class="text-blue"><b>Asset Calculator</b></span>

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
          <v-form class="text-blue">
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
            
            <div class='button-style'>
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
            </div>
            <div class="output-style">{{ calculateBudget }}</div>
          </v-form>
        </v-card>
      </v-flex>
    </div>

    <div v-show="assetFormHidden">
      <v-flex xs12 sm6 offset-sm3>
        <v-card class="calculator-form" color="white">
          <v-form class="text-blue">
            <div class="d-flex"></div>

            <v-expansion-panels v-model="panel" multiple>
              <v-expansion-panel>
                <v-expansion-panel-header class="text-blue"
                  ><b>ASSETS</b></v-expansion-panel-header
                >
                <v-expansion-panel-content>
                  <div class="profile-text">Your total cash</div>
                  <v-text-field
                    v-model="cash"
                    class="input-field"
                    color="rgb(172, 193, 252)"
                    required
                    regular
                  ></v-text-field>
                  <div class="profile-text">Your total CPF savings</div>
                  <v-text-field
                    v-model="cpf"
                    class="input-field"
                    color="rgb(172, 193, 252)"
                    required
                    regular
                  ></v-text-field>
                  <div class="profile-text">Your total life insurance coverage</div>
                  <v-text-field
                    v-model="lifeinsurance"
                    class="input-field"
                    color="rgb(172, 193, 252)"
                    required
                    regular
                  ></v-text-field>
                  <div class="profile-text">Your total invested assets</div>
                  <v-text-field
                    v-model="investments"
                    class="input-field"
                    color="rgb(172, 193, 252)"
                    required
                    regular
                  ></v-text-field>
                </v-expansion-panel-content>
              </v-expansion-panel>

              <v-expansion-panel>
                <v-expansion-panel-header class="text-blue"
                  ><b>LIABILITIES</b></v-expansion-panel-header
                >
                <v-expansion-panel-content>
                  <div class="profile-text">Your total debt balance</div>
                  <v-text-field
                    v-model="debt"
                    class="input-field"
                    color="rgb(172, 193, 252)"
                    required
                    regular
                  ></v-text-field>
                  <div class="profile-text">Your outstanding bills</div>
                  <v-text-field
                    v-model="bills"
                    class="input-field"
                    color="rgb(172, 193, 252)"
                    required
                    regular
                  ></v-text-field>
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>

            <div class='button-style'>
            <v-btn
              class="justify-center white--text button"
              color="rgb(0, 0, 255)"
              min-width="300"
              min-height="50"
              x-large
              @click="calculateAssets"
            >
              CALCULATE
            </v-btn>
            </div>

            <div class="output-style">{{ calculateAssets }}</div>
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
      budgetFormHidden: false,
      assetFormHidden: false,
      income: 0,
      expense: 0,
      netCashFlow: "",
      cash: 0,
      cpf: 0,
      lifeinsurance: 0,
      investments: 0,
      debt: 0,
      bills: 0,
    };
  },
  methods: {
    handleAssetClick() {
      this.assetFormHidden = !this.assetFormHidden;
      this.budgetFormHidden = false;
    },
    handleBudgetClick() {
      this.budgetFormHidden = !this.budgetFormHidden;
      this.assetFormHidden = false;
    },
    currencyFormat(num) {
      return "$" + num.toFixed(0).replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,");
    },
  },
  computed: {
    calculateBudget() {
      var netCashFlow = this.income - this.expense;
      return this.currencyFormat(netCashFlow);
    },
    calculateAssets() {
      var netAssets = this.cash + this.cpf + this.lifeinsurance + this.investments - this.debt - this.bills;
      return this.currencyFormat(netAssets)
    },
  },
};
</script>

<style scoped>
.button-style {
  padding: 40px 40px 20px 40px;
}

.output-style {
  font-size: 3em;
}

.calculator-form {
  padding: 40px 40px 50px 40px;
}

.v-expansion-panel-content >>> profile-text {
  padding: 10px;
  margin-top: 10px;
  color: indigo darken-4;
}
</style>
