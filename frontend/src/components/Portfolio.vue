<template>
  <div class="Quickstart">
    <v-card flat class="block-card">
      <!-- input -->
      <v-card-text class="text-center">
        <span class="text-blue"
          ><h1><b>Your Portfolio Overview</b></h1></span
        ><br />

        To insert chart of user here

        <div v-if="assets" style="text-align:left;">
          Assets
          <hr />
          <table>
            <tr>
              <td></td>
              <td>High</td>
              <td>Low</td>
              <td>Open</td>
              <td>Close</td>
            </tr>
            <div v-for="(assets, index) in listofassets" :key="assets">
              <tr>
                <td>Assets {{ index + 1 }}</td>
                <td v-for="value in assets" :key="value">
                  {{ value }}
                </td>
              </tr>
            </div>
          </table>
        </div>
      </v-card-text>

      <div>
        <div class="chart-wrap">
          <div id="chart">
            <apexchart
              type="donut"
              width="380"
              :options="chartOptions"
              :series="series"
            ></apexchart>
          </div>
        </div>

        <div class="actions">
          <button @click="appendData">
            + ADD
          </button>

          <button @click="removeData">
            - REMOVE
          </button>

          <button @click="randomize">
            RANDOMIZE
          </button>

          <button @click="reset">
            RESET
          </button>
        </div>
      </div>

      <!-- output -->
    </v-card>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
  data: () => ({
    assets: true,
    listofassets: [["high 1", "low 1", "open 1", "close 1"]],
    series: [44, 55, 13, 33],
    chartOptions: {
      chart: {
        width: 380,
        type: "donut",
      },
      dataLabels: {
        enabled: false,
      },
      responsive: [
        {
          breakpoint: 480,
          options: {
            chart: {
              width: 200,
            },
            legend: {
              show: false,
            },
          },
        },
      ],
      legend: {
        position: "right",
        offsetY: 0,
        height: 230,
      },
    },
  }),
  computed: {
    apexchart: VueApexCharts,
  },
  methods: {
    appendData: function() {
      var arr = this.series.slice();
      arr.push(Math.floor(Math.random() * (100 - 1 + 1)) + 1);
      this.series = arr;
    },

    removeData: function() {
      if (this.series.length === 1) return;
      var arr = this.series.slice();
      arr.pop();
      this.series = arr;
    },

    randomize: function() {
      this.series = this.series.map(function() {
        return Math.floor(Math.random() * (100 - 1 + 1)) + 1;
      });
    },

    reset: function() {
      this.series = [44, 55, 13, 33];
    },
  },
};
</script>

<style scoped lang="scss">
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
</style>
