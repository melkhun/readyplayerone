<template>
  <div class="Portfolio ">
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

        <!--Donut-->
        
  <div>
    <h1>Chart Demo</h1>

    <div class="grid">
      <ChartBar />
      <ChartDoughnut />
      <ChartLine />
    </div>
  </div>

        <div>
          <h1>Chart Demo</h1>
          <div v-if="assets" style="text-align:left;">
          <h2><b>Assets</b></h2>
          <hr>
        </div>

        <div>
          <v-simple-table
                  :dense="dense"
                  :fixed-header="fixedHeader"
                  :height="height"
                >
            <template v-slot:default>
              <thead>
                <tr>
                  <th></th>
                  <th class="text-left">High</th>
                  <th class="text-left">Low</th>
                  <th class="text-left">Open</th>
                  <th class="text-left">Close</th>
                  <th class="text-left">Remove</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in desserts" :key="item.name">
                  <td>Asset {{index + 1}}</td>
                  <td>{{ item.high }}</td>
                  <td>{{ item.low }}</td>
                  <td>{{ item.open }}</td>
                  <td>{{ item.close }}</td>
                  <td><v-btn color="primary" @click="deleteItem">remove</v-btn></td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </div>


      </div>
      </v-card-text>


      <!-- output -->
    </v-card>
  </div>
</template>

<script>

import ChartDoughnut from "@/components/chart-doughnut";


export default {
  components: {
    ChartDoughnut,
  }
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

.grid {
  display: grid;
  row-gap: 2rem;
}
</style>
