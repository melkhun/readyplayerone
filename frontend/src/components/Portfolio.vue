<template>
  <div class="Portfolio ">
    <v-card flat class="block-card">
      <!-- input -->
      <v-card-text class="text-center">
        <span class="text-blue"
          ><h1><b>Your Followed Portfolio Overview</b></h1></span
        ><br />
        
  <div>
    <h1>Chart Demo</h1>

    <div class="grid">
      <ChartDoughnut :countEtf="countEtf" :countBond="countBond" :countFuture="countFuture" :countOption="countOption" :countEquity="countEquity" />

    </div>
  </div>

  <div class="header-style">
          Here's a breakdown of your followed portfolio
        </div>

        <div>
          <h1>Chart Demo</h1>
      </div>
        <div>
          <div v-if="assets" style="text-align:left;">
            <h2><b>Assets</b></h2>
            <hr />
          </div>

          <div>
            <v-card flat>
              {{ errorMsg }}
            </v-card>

            <v-data-table
              v-model="selected"
              :headers="headers"
              :items="tableContent"
              item-key="symbol"
              show-select
              class="elevation-1"
            >
            </v-data-table>
            <v-btn @click="deleteSelected">Delete</v-btn>
          </div>
        </div>
      </v-card-text>

      <!-- output -->
    </v-card>
  </div>
</template>

<script>
import ChartDoughnut from "@/components/chart-doughnut";
import { getPortfolio, deletePortfolioAsset } from '../api';
import { Auth } from 'aws-amplify';
import { getCompanyData } from '../api'

export default {
  data: () => ({
    headers: [
      { text: "Symbol", value: "symbol" },
      { text: "Name", value: "name" },
      { text: "Asset Type", value: "type" },
      { text: "50 Day Moving Average", value: "50DayMovingAverage" },
      { text: "52 Week High", value: "52WeekHigh" },
      { text: "52 Week Low", value: "52WeekLow" },
      { text: "Dividend Per Share", value: "DividendPerShare" },
      { text: "Profit Margin", value: "ProfitMargin" },
      { text: "Market Cap", value: "cap" },
      { text: "PE Ratio (TTM)", value: "ratio" },
    ],
    tableContent: [],
    items: [],
    tableItems: {},
    selected: [],
    selectedData: [],
    errorMsg: null,
    username: null,
    countEtf: 0,
    countBond: 0,
    countFuture: 0,
    countOption: 0,
    countEquity: 0,
    countTotal:0
  }),
  components: {
    ChartDoughnut,
  },
mounted() {
    this.getUser();
    // this.getItems();
    // for (var i = 0; i < this.items.length; i++) {
    //   this.getCompanyData(this.items[i]);
    // }
  },

  methods: {
    async getUser() {
      let user = await Auth.currentAuthenticatedUser();
      this.username = user['username'];
      const data = {
        username: this.username,
      }
      let userData = await getPortfolio(data);
      this.tableItems = userData['portfolio'];

      let lengthItems = Object.keys(this.tableItems).length;

      // cap at 5 due to api limit restrictions
      for (var i = 0; i < Math.min(lengthItems, 5); i++) {
        this.getCompanyData(Object.keys(this.tableItems)[i]);
      }
    },

    getItems() {
      this.items = ["IBM", "GOOGL"];
      // call some api
    },
    async getCompanyData(symbol) {
      try {
        // var resp = {
        //   Symbol: "IBM",
        //   AssetType: "Common Stock",
        //   Name: "International Business Machines Corporation",
        //   Description:
        //     "International Business Machines Corporation operates as an integrated solutions and services company worldwide. Its Cloud & Cognitive Software segment offers software for vertical and domain-specific solutions in health, financial services, and Internet of Things (IoT), weather, and security software and services application areas; and customer information control system and storage, and analytics and integration software solutions to support client mission critical on-premise workloads in banking, airline, and retail industries. It also offers middleware and data platform software, including Red Hat, which enables the operation of clients' hybrid multi-cloud environments; and Cloud Paks, WebSphere distributed, and analytics platform software, such as DB2 distributed, information integration, and enterprise content management, as well as IoT, Blockchain and AI/Watson platforms. The company's Global Business Services segment offers business consulting services; system integration, application management, maintenance, and support services for packaged software; finance, procurement, talent and engagement, and industry-specific business process outsourcing services; and IT infrastructure and platform services. Its Global Technology Services segment provides project, managed, outsourcing, and cloud-delivered services for enterprise IT infrastructure environments; and IT infrastructure support services. The company's Systems segment offers servers for businesses, cloud service providers, and scientific computing organizations; data storage products and solutions; and z/OS, an enterprise operating system, as well as Linux. Its Global Financing segment provides lease, installment payment, loan financing, short-term working capital financing, and remanufacturing and remarketing services. The company was formerly known as Computing-Tabulating-Recording Co. and changed its name to International Business Machines Corporation in 1924. The company was founded in 1911 and is headquartered in Armonk, New York.",
        //   Exchange: "NYSE",
        //   Currency: "USD",
        //   Country: "USA",
        //   Sector: "Technology",
        //   Industry: "Information Technology Services",
        //   Address: "One New Orchard Road, Armonk, NY, United States, 10504",
        //   FullTimeEmployees: "352600",
        //   FiscalYearEnd: "December",
        //   LatestQuarter: "2020-06-30",
        //   MarketCapitalization: "108917817344",
        //   EBITDA: "15576999936",
        //   PERatio: "14.5329",
        //   PEGRatio: "8.1011",
        //   BookValue: "23.076",
        //   DividendPerShare: "6.52",
        //   DividendYield: "0.0509",
        //   EPS: "8.811",
        //   RevenuePerShareTTM: "85.058",
        //   ProfitMargin: "0.1043",
        //   OperatingMarginTTM: "0.1185",
        //   ReturnOnAssetsTTM: "0.0362",
        //   ReturnOnEquityTTM: "0.4097",
        //   RevenueTTM: "75499003904",
        //   GrossProfitTTM: "36489000000",
        //   DilutedEPSTTM: "8.811",
        //   QuarterlyEarningsGrowthYOY: "-0.458",
        //   QuarterlyRevenueGrowthYOY: "-0.054",
        //   AnalystTargetPrice: "135.19",
        //   TrailingPE: "14.5329",
        //   ForwardPE: "10.4493",
        //   PriceToSalesRatioTTM: "1.518",
        //   PriceToBookRatio: "5.5547",
        //   EVToRevenue: "2.2493",
        //   EVToEBITDA: "11.2431",
        //   Beta: "1.17",
        //   "52WeekHigh": "158.75",
        //   "52WeekLow": "90.56",
        //   "50DayMovingAverage": "125.1934",
        //   "200DayMovingAverage": "122.3291",
        //   SharesOutstanding: "890579008",
        //   SharesFloat: "889189445",
        //   SharesShort: "21600483",
        //   SharesShortPriorMonth: "23242369",
        //   ShortRatio: "4.51",
        //   ShortPercentOutstanding: "0.02",
        //   ShortPercentFloat: "0.0243",
        //   PercentInsiders: "0.108",
        //   PercentInstitutions: "58.555",
        //   ForwardAnnualDividendRate: "6.52",
        //   ForwardAnnualDividendYield: "0.0509",
        //   PayoutRatio: "0.7358",
        //   DividendDate: "2020-09-10",
        //   ExDividendDate: "2020-08-07",
        //   LastSplitFactor: "2:1",
        //   LastSplitDate: "1999-05-27",
        // };

        var resp = await getCompanyData(symbol);

        // console.log(resp);

        if (Object.keys(resp).length === 0 || ("Note" in resp)) {
          if (this.errorMsg == null) {
            this.errorMsg = "Note: Due to the free tier API limitation, some stocks may not show values.";
          }
        } else {
            if (resp["AssetType"] == "ETF") this.countEtf += 1
            if (resp["AssetType"] == "Options") this.countOption += 1
            if (resp["AssetType"] == "Futures") this.countFuture += 1
            if (resp["AssetType"] == "Common Stock") this.countEquity += 1
            if (resp["AssetType"] == "Bond") this.countBond += 1
            this.countTotal += 1
            
            console.log(symbol);

            this.tableContent.push({
              symbol: resp["Symbol"],
              name: resp["Name"],
              type: resp["AssetType"],
              "50DayMovingAverage": resp["50DayMovingAverage"],
              "52WeekHigh": resp["52WeekHigh"],
              "52WeekLow": resp["52WeekLow"],
              DividendPerShare: resp["DividendPerShare"],
              ProfitMargin: resp["ProfitMargin"],
              cap: resp["MarketCapitalization"],
              ratio: resp["PERatio"],
            });
        }        
      } catch (e) {
        console.error(e);
      }
    },

    deleteSelected() {
      for (let id in this.selected) {
        console.log(this.tableContent.indexOf(this.selected[0]));

        let tableID = this.tableContent.indexOf(this.selected[0]);
        let currSymbol = this.selected[id]["symbol"];

        const data = {
          username: this.username,
          category: this.tableItems[currSymbol],
          symbol: currSymbol,
        };
        console.log(data);
        this.deletePortfolio(data);
        this.tableContent.splice(tableID, 1);

      }
      
    },

    async deletePortfolio(data) {
      try {
        var resp = await deletePortfolioAsset(data);
        console.log(resp)
      } catch(e) {
        console.log(e)
      }
    },

  },
};
</script>

<style scoped lang="scss">
.header-style {
  padding: 150 40 150 40;
  font-size: 2em;
  color:blue;
}

.button-style {
  padding: 80px 50px 20px 50px;
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

.grid {
  display: grid;
  row-gap: 2rem;
}
</style>
