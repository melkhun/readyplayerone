<template>
  <div class="Quickstart">
    <v-card flat class="block-card">
      <!-- input -->
      <v-card-text v-if="!showResult" class="text-center">
        <span class="text-blue"
          ><h1><b>Investment Quick Start</b></h1></span
        ><br />
        <p>
          Want to invest but don’t know what or how?<br />Fill up your profile
          and we will recommend you something that is just right for you!
        </p>

        <v-flex xs12 sm6 offset-sm3>
          <v-form>
            <div class="profile">
              <v-card color="transparent" elevation="0">
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
              <v-card-title class="justify-center"
                ><span class="text-blue">Risk Appetite</span></v-card-title
              >
            </v-row>
            <v-row>
              <v-select
                class="input-field justify-center"
                :items="riskLevels"
                v-model="risk"
                placeholder="Select a risk level"
              ></v-select>
            </v-row>

            <v-card-title class="justify-center"
              ><span class="text-blue">Time Horizon (Years)</span></v-card-title
            >
            <v-slider
              v-model="time"
              color="rgb(172, 193, 252)"
              thumb-label="always"
              max="10"
              min="1"
            ></v-slider>

            <v-card-title class="justify-center"
              ><span class="text-blue"
                >How much are you ready to invest?</span
              ></v-card-title
            >
            <v-text-field
              v-model="amount"
              label="Enter an amount"
              required
              regular
            ></v-text-field>

            <div class="justify-center">
              <div class="button-style">
                <v-btn
                  class="justify-center white--text"
                  color="#651FFF"
                  min-width="300"
                  min-height="50"
                  x-large
                  @click="handleSubmit"
                >
                  SHOW MY RESULTS
                </v-btn>
              </div>
            </div>
          </v-form>
        </v-flex>
      </v-card-text>

      <!-- output -->
      <v-card-text v-else>
        <h1>
          <b
            >Based on your profile, we recommend the following investments
            classes.</b
          >
        </h1>
        <br />
        <v-card flat>
          <v-tabs color="deep-purple accent-4" centered>
            <v-tab v-for="rec of recommendation" :key="rec" @click='updateTable(tabs[rec].id)'>
              {{ tabs[rec].name }}
            </v-tab>
            <!-- <v-tab-item v-for="rec of recommendation" :key="rec">
              <v-card flat>
                <v-card-text>{{ tabs[rec].desc }}</v-card-text>
              </v-card>
            </v-tab-item> -->
          </v-tabs>

          <!--samantha code here-->

          <v-data-table
            v-model="selected"
            :headers="headers"
            :items="tableContent"
            :single-select="singleSelect"
            item-key="name"
            show-select
            class="elevation-1"
          >
            <template v-slot:top>
              <v-switch
                v-model="singleSelect"
                label="Single select"
                class="pa-3"
              ></v-switch>
            </template>

          </v-data-table>
          <div class="button-style">
            <v-btn 
              @click="addSelected"
              class="justify-center white--text"
              color="#651FFF"
              min-width="300"
              min-height="50"
              x-large
            >Add to Portfolio</v-btn>
          </div>
          <div class="button-style">
            <v-btn
              class="justify-center white--text"
              color="blue-grey lighten-2"
              min-width="300"
              min-height="50"
              x-large
              @click="goBack"
            >
              START OVER
            </v-btn>
          </div>
        </v-card>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import { getTopGains, getCompanyData, getFutures, getBonds, getTopETFs, getOptions, addToPortfolio } from '../api'
import { Auth } from 'aws-amplify';

export default {
  data: () => ({
    username: null,
    name: null,
    age: null,
    risk: null,
    time: null,
    amount: null,
    showResult: false,
    riskLevels: ["Low", "Medium", "High"],
    topGains: {
      "Symbol": {"0": "TLVLF", "1": "BNKXF", "2": "CRYYF", "3": "PTKFF", "4": "CAIXY", "5": "BNDSY", "6": "CHWRF", "7": "CYDY", "8": "BIGC", "9": "WKHS"},
      "Name": {"0": "Minds + Machines Group Limited", "1": "Bankia, S.A."}
    },
    currentTab: null,
    tabs: [
      {
        id: 0,
        name: "No recommendations found",
        desc: "Sorry, we don't have anything suitable for you yet.",
      },
      // {
      //   id: 1,
      //   name: "FOREX",
      //   desc:
      //     "Mr Worldwide, buy and sell currencies of your choice. Take a long position to buy when you expect the prices to go up, short sell when you expect prices to go down.",
      // },
      // {
      //   id: 2,
      //   name: "CFD",
      //   desc:
      //     "CFD in short for Contract For Difference. You don’t actually own the stock but you borrow it from a 3rd party to take that position. Pay only a percentage of the full cost of the underlying share, but get the same exposure.",
      // },
      // {
      //   id: 3,
      //   name: "COMMODITIES",
      //   desc:
      //     "Our bread and butter. Commodities are things like grains, gold, beef, oil, and natural gas. There are many ways to get into commodities, through and ETF, mutual fund, futures or buying the commodities itself.  As prices of commodities tend to move in opposition to stocks, it is a good “resistive” instrument to consider.",
      // },
      {
        id: 4,
        name: "STOCK",
        desc:
          "When a company offers equities, it's selling partial ownership in the company. The share you purchased go up or down with the value of the company. Receive dividends from the company when it is performing well for holding on to the shares.",
      },
      {
        id: 5,
        name: "FUTURES",
        desc:
          "By purchasing a futures contract, you enter in an legal agreement to buy or sell something at a predetermined price at a specified time in the future. There’s no going back.",
      },
      {
        id: 6,
        name: "OPTIONS",
        desc:
          "The future is too unpredictable? Options give you the power to buy or sell at a predetermined price in the future. You don’t have to execute it if you don’t want to, but what you paid for the option is sunk cost, sadly.",
      },
      {
        id: 7,
        name: "ETFs",
        desc:
          "You can do almost everything with ETFs - Exchange Traded Funds. Invest in commodities, stocks, currencies, get them all. By investing in one ETF, you instantly diversification  as an ETF contains a basket of other instruments like how an index does.",
      },
      {
        id: 8,
        name: "BONDS",
        desc:
          "Bonds can be issued by companies or governments and generally pay a stated interest rate. The interest rate is the discount you get when purchasing the bond, for a 10% interest bond, you buy at $900 and get $1000 when it matures. How simple?",
      },
      // {
      //   id: 9,
      //   name: "MUTUAL FUNDS",
      //   desc:
      //     "It’s more fun with company. Pool your investments with other investors to invest in a pool of assets with mutual funds. Like ETFs, you can have exposure to various asset classes with mutual funds. Mutual funds unlike ETFs are offered by fund companies and are priced daily.",
      // },
      // {
      //   id: 10,
      //   name: "REITS",
      //   desc:
      //     "A REIT is a corporation, trust, or association that invests directly in income-producing real estate and is traded like a stock.",
      // },
    ],
    singleSelect: false,
    selected: [],
    selectedCat: [],
    headers: [],
    tableContent: [],
  }),
  computed: {
    highCapital() {
      return this.amount > 10000;
    },
    longHorizon() {
      return this.time > 3;
    },
    recommendation() {
      let results = [1]
      // if (!this.highCapital && !this.longHorizon && this.risk == "High")
      //   return [1, 2, 3]; //forex, CFD, commodities
      if (!this.longHorizon && this.risk == "Medium") results = [1]; //equities
      if (this.longHorizon && this.risk == "High") results = [2]; //futures
      if (!this.highCapital && this.longHorizon && this.risk == "Medium") results = [3]; //options
      if (!this.highCapital && !this.longHorizon && this.risk == "Low") results = [4]; //ETFs
      if (this.longHorizon && this.risk == "Low") results = [5]; //bonds
      // if (!this.highCapital && this.longHorizon && this.risk == "Medium")
      //   return [9]; //mutual funds
      // if (!this.highCapital && this.longHorizon && this.risk == "Low")
      //   return [10]; //REITS
      // return [1];
      return results;
    },
  },
  mounted() {
    this.getUser()
  },
  methods: {
    async getUser() {
      let user = await Auth.currentAuthenticatedUser();
      this.username = user['username'];
    },
    
    async addToPortfolio(data) {
      try {
        var resp = await addToPortfolio(data);
        console.log(resp)
        alert('Successfully added to portfolio!')
      } catch(e) {
        console.log(e)
        alert('Unable to add to portfolio, please rememeber to log in.')
      }
    },

    addSelected() {
      console.log(this.selectedCat);
      for (let id in this.selected) {
        const data = {
          category: this.selectedCat,
          symbol: this.selected[id]["symbol"],
          username: this.username,
        }
        console.log(data)
        this.addToPortfolio(data)
      }
    },

    handleSubmit() {
      if (this.amount === '' || this.amount === null || this.amount.value === 0 || 
      this.time === '' || this.time === null || this.time.value === 0 || 
      this.risk === '' || this.risk === null || this.risk.value === 0){
            alert('Please fill in all your details.');
      } else {
        this.showResult = true;
      }
      if (this.recommendation[0] == 1) {
        this.getTopGains();
        this.selectedCat = "STOCK";
      }
      if (this.recommendation[0] == 2) {
        this.getFutures()
        this.selectedCat = "FUTURES";
      }
      if (this.recommendation[0] == 3) {
        this.getOptions()
        this.selectedCat = "OPTIONS";
      }
      if (this.recommendation[0] == 4) {
        this.getTopETFs()
        this.selectedCat = "ETFs";
      }
      if (this.recommendation[0] == 5) {
        this.getBonds()
        this.selectedCat = "BONDS";
      }


    },
    goBack() {
      this.showResult = false;
      this.amount = null;
      this.risk = null;
      this.time = null;
    },

    async getFutures() {
      try {
        var resp = await getFutures()
        var len = Object.keys(resp.Symbol).length
        var tmp = []
        for (var i=0; i<len; i++) {
          tmp.push({
            symbol: resp["Symbol"][i],
            name: resp["Name"][i],
            price: resp["Last price"][i],
            mkttime: resp["Market time"][i],
            change: resp["Change"][i],
            pChange: resp["% change"][i],
            volume: resp["Volume"][i],
            openInt: resp["Open Interest"][i],
          })
        }
        this.tableContent = tmp
        this.headers = [
          { text: "Symbol", value: "symbol" },
          { text: "Name", value: "name" },
          { text: "Last price", value: "price" },
          { text: "Market time", value: "mkttime" },
          { text: "Change", value: "change" },
          { text: "% change", value: "pChange" },
          { text: "Volume", value: "volume" },
          { text: "Open Interest", value: "openInt" },
        ]
      } catch(e) {
        console.error(e)
      }
    },

    async getBonds() {
      try {
        var resp = await getBonds()
        var len = Object.keys(resp.Symbol).length
        var tmp = []
        for (var i=0; i<len; i++) {
          tmp.push({
            symbol: resp["Symbol"][i],
            name: resp["Name"][i],
            price: resp["Last price"][i],
            change: resp["Change"][i],
            pChange: resp["% change"][i],
          })
        }
        this.tableContent = tmp
        this.headers = [
          { text: "Symbol", value: "symbol" },
          { text: "Name", value: "name" },
          { text: "Last price", value: "price" },
          { text: "Change", value: "change" },
          { text: "% change", value: "pChange" },
        ]
      } catch(e) {
        console.error(e)
      }
    },

    async getTopETFs() {
      try {
        var resp = await getTopETFs()
        var len = Object.keys(resp.Symbol).length
        var tmp = []
        for (var i=0; i<len; i++) {
          tmp.push({
            symbol: resp["Symbol"][i],
            name: resp["Name"][i],
            price: resp["Price (intraday)"][i],
            change: resp["Change"][i],
            pChange: resp["% change"][i],
            volume: resp["Volume"][i],
            fiftyday: resp["50-day average"][i],
            twohdday: resp["200-day average"][i],
          })
        }
        this.tableContent = tmp
        this.headers = [
          { text: "Symbol", value: "symbol" },
          { text: "Name", value: "name" },
          { text: "Price (intraday)", value: "price" },
          { text: "Change", value: "change" },
          { text: "% change", value: "pChange" },
          { text: "Volume", value: "volume" },
          { text: "50-day average", value: "fiftyday" },
          { text: "200-day average", value: "twohdday" },
        ]
      } catch(e) {
        console.error(e)
      }
    },

    async getOptions() {
      try {
        var resp = await getOptions()
        var len = Object.keys(resp.Symbol).length
        var tmp = []
        for (var i=0; i<len; i++) {
          tmp.push({
            symbol: resp["Underlying Symbol"][i],
            name: resp["Name"][i],
            strike: resp["Strike"][i],
            expDate: resp["Expiration Date"][i],
            price: resp["Price (Intraday)"][i],
            change: resp["Change"][i],
            pChange: resp["% Change"][i],
            bid: resp["Bid"][i],
            ask: resp["Ask"][i],
            volume: resp["Volume"][i],
            openInt: resp["Open Interest"][i],
          })
        }
        this.tableContent = tmp
        this.headers = [
          { text: "Underlying Symbol", value: "symbol" },
          { text: "Name", value: "name" },
          { text: "Strike", value: "strike" },
          { text: "Expiration Date", value: "expDate" },
          { text: "Price (intraday)", value: "price" },
          { text: "Change", value: "change" },
          { text: "% change", value: "pChange" },
          { text: "Bid", value: "bid" },
          { text: "Ask", value: "ask" },
          { text: "Volume", value: "volume" },
          { text: "Open Interest", value: "openInt" },
        ]
      } catch(e) {
        console.error(e)
      }
    },

    async getTopGains() {
      try {
        var resp = await getTopGains()
        var len = Object.keys(resp.Symbol).length
        var tmp = []
        for (var i=0; i<len; i++) {
          tmp.push({
            symbol: resp["Symbol"][i],
            name: resp["Name"][i],
            price: resp["Price (Intraday)"][i],
            change: resp["Change"][i],
            pChange: resp["% Change"][i],
            volume: resp["Volume"][i],
            aVolume: resp["Avg Vol (3 month)"][i],
            cap: resp["Market Cap"][i],
            ratio: resp["PE Ratio (TTM)"][i],
          })
        }
        this.tableContent = tmp
        this.headers = [
          { text: "Symbol", value: "symbol" },
          { text: "Name", value: "name" },
          { text: "Price (Intraday)", value: "price" },
          { text: "Change", value: "change" },
          { text: "% Change", value: "pChange" },
          { text: "Volume", value: "volume" },
          { text: "Avg Vol (3 month)", value: "aVolume" },
          { text: "Market Cap", value: "cap" },
          { text: "PE Ratio (TTM)", value: "ratio" },
        ]
      } catch(e) {
        console.error(e)
      }
    },
    async getCompanyData() {
      try {
        var resp = await getCompanyData()
        console.log(resp)
      } catch(e) {
        console.error(e)
      }
    },
    updateTable(id) {
      this.currentTab = id
      if (this.currentTab == 4) {
        this.getTopGains()
      } else {
        this.tableContent = []
      }
    }
  },
};
</script>

<style scoped lang="scss">
.button-style {
  padding: 30px 50px 0px 50px;
}

.block-card {
  padding: 50px 40px 40px 40px;
}
.center-element >>> input {
  text-align: center;
  justify-content: center;
}

.input-field {
  width: 100px;
  color: rgb(172, 193, 252);
}

.profile-text {
  padding: 10px;
  margin-top: 10px;
}

.transparent {
  background-color: transparent !important;
  border-color: transparent !important;
}
</style>
