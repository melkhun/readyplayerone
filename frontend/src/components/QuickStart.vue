<template>
<div class="Quickstart">
  
<v-card flat>

<!-- input -->
  <v-card-text v-if="!showResult" class="text-center">

    <span class="text-blue"><h1><b>Investment Quick Start</b></h1></span>
    <p>Want to invest but don’t know what or how?<br>Fill up your profile and we will recommend you something that is just right for you!</p>
    <v-form>
      <div class="profile">
        <v-card
          color="transparent"
          elevation=0
        >
          <v-row>
            <div class="profile-text">My name is</div>
            <v-text-field
              class="input-field"
              v-model="name"
              color="rgb(172, 193, 252)"
              label="Input your name"
              required
              regular
            ></v-text-field>
            <div class="profile-text">and I am</div>
            <v-text-field
              class="input-field"
              v-model="age"
              color="rgb(172, 193, 252)"
              label="Input your age"
              required
              regular
            ></v-text-field>
            <div class="profile-text">years old.</div>
          </v-row>
        </v-card>
      </div>

      <v-row class="justify-center">
        <v-card-title class="justify-center"><span class="text-blue">Risk Appetite</span></v-card-title>
      </v-row>
      <v-row>
        <v-select class="input-field justify-center" :items="riskLevels" v-model="risk"></v-select>
      </v-row>

      <v-card-title class="justify-center"><span class="text-blue">Time Horizon (Years)</span></v-card-title>
      <v-slider
          v-model="time"
          color="rgb(172, 193, 252)"
          thumb-label="always"
          max="10"
          min="1"
      ></v-slider>

      <v-card-title class="justify-center"><span class="text-blue">How much are you ready to invest?</span></v-card-title>
      <v-text-field
        v-model="amount"
        label="Enter an amount"
        required
        regular
      ></v-text-field>

      <div class="justify-center">
      <v-btn
        class="justify-center white--text"
        color="rgb(0, 0, 255)"
        min-width=300
        min-height=50
        x-large
        @click="handleSubmit"
      >
      SHOW MY RESULTS
      </v-btn>
      </div>

    </v-form>
  </v-card-text>

<!-- output --> 
  <v-card-text v-else>
    <h1><b>Based on your profile, we recommend the following investments classes.</b></h1>
    <br>
    <v-card flat>
      <v-tabs color="deep-purple accent-4" centered>
        <v-tab v-for="rec of recommendation" :key="rec">
          {{tabs[rec].name}}
        </v-tab>
        <v-tab-item
          v-for="rec of recommendation"
          :key="rec"
        >
          <v-card flat>
            <v-card-text>{{ tabs[rec].desc }}</v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
      
    </v-card>
  </v-card-text>

</v-card>

</div>
</template>

<script>
  export default {
    data: () => ({
      name: null,
      age: null,
      risk: null,
      time: null,
      amount: null,
      showResult: false,
      riskLevels: ["Low", "Medium", "High"],
      tabs: [
        {
          id: 0,
          name: "No recommendations found",
          desc: "idk we cant help"
        },
        {
          id: 1, 
          name: 'FOREX',
          desc: "Mr Worldwide, buy and sell currencies of your choice. Take a long position to buy when you expect the prices to go up, short sell when you expect prices to go down."
        },
        { 
          id: 2, 
          name: 'CFD',
          desc: "CFD in short for Contract For Difference. You don’t actually own the stock but you borrow it from a 3rd party to take that position. Pay only a percentage of the full cost of the underlying share, but get the same exposure."
        },
        { 
          id: 3, 
          name: 'COMMODITIES',
          desc: "Our bread and butter. Commodities are things like grains, gold, beef, oil, and natural gas. There are many ways to get into commodities, through and ETF, mutual fund, futures or buying the commodities itself.  As prices of commodities tend to move in opposition to stocks, it is a good “resistive” instrument to consider."
        },
        { 
          id: 4, 
          name: 'EQUITIES',
          desc: "When a company offers equities, it's selling partial ownership in the company. The share you purchased go up or down with the value of the company. Receive dividends from the company when it is performing well for holding on to the shares."
        },
        { 
          id: 5, 
          name: 'FUTURES',
          desc: "By purchasing a futures contract, you enter in an legal agreement to buy or sell something at a predetermined price at a specified time in the future. There’s no going back."
        },
        {
          id: 6, 
          name: 'OPTIONS',
          desc: "The future is too unpredictable? Options give you the power to buy or sell at a predetermined price in the future. You don’t have to execute it if you don’t want to, but what you paid for the option is sunk cost, sadly."
        },
        {
          id: 7, 
          name: 'ETFs',
          desc: "You can do almost everything with ETFs - Exchange Traded Funds. Invest in commodities, stocks, currencies, get them all. By investing in one ETF, you instantly diversification  as an ETF contains a basket of other instruments like how an index does."
        },
        {
          id: 8, 
          name: 'BONDS',
          desc: "Bonds can be issued by companies or governments and generally pay a stated interest rate. The interest rate is the discount you get when purchasing the bond, for a 10% interest bond, you buy at $900 and get $1000 when it matures. How simple?"
        },
        {
          id: 9,
          name: 'MUTUAL FUNDS',
          desc: "It’s more fun with company. Pool your investments with other investors to invest in a pool of assets with mutual funds. Like ETFs, you can have exposure to various asset classes with mutual funds. Mutual funds unlike ETFs are offered by fund companies and are priced daily."
        },
        { 
          id: 10, 
          name: 'REITS',
          desc: "A REIT is a corporation, trust, or association that invests directly in income-producing real estate and is traded like a stock."
        },
      ],
    }),
    computed: {
      highCapital() {
        return this.amount > 10000
      },
      longHorizon() {
        return this.time > 3
      },
      recommendation() {
        if (!this.highCapital && !this.longHorizon && this.risk=="High") return [1,2,3]
        if (this.highCapital && !this.longHorizon && this.risk=="Medium") return [4]
        if (!this.highCapital && this.longHorizon && this.risk=="High") return [5]
        if (!this.highCapital && this.longHorizon && this.risk=="Medium") return [6]
        if (!this.highCapital && !this.longHorizon && this.risk=="Low") return [7]
        if (this.highCapital && this.longHorizon && this.risk=="Low") return [8]
        if (!this.highCapital && this.longHorizon && this.risk=="Medium") return [9]
        if (!this.highCapital && this.longHorizon && this.risk=="Low") return [10]
        return [0]
      }
    },
    methods: {
      handleSubmit() {
        console.log(this.recommendation)
        this.showResult = true
      },
    },
  };
</script>

<style scoped lang="scss">
  .center-element >>> input {
    text-align:center;
    justify-content: center;
  }

  .text-blue {
    color:rgb(0, 102, 255);
    font-size: 300;
    justify-content: center;
  }
  
  .input-field {
    width: 200px;
    color: rgb(172, 193, 252);
  }

  .profile-text {
    padding:10px;
    margin-top:10px;
  }

  .transparent {
     background-color: transparent!important;
     border-color: transparent!important;
   }
</style>