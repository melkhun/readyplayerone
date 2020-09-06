<template>
  <div class="Portfolio ">

    <v-card flat class="block-card">

    <!-- input -->
      <v-card-text class="text-center">

        <span class="text-blue"><h1><b>Your Portfolio Overview</b></h1></span><br>
        
        To insert chart of user here

      <div v-if="assets" style="text-align:left;">
        <h2><b>Assets</b></h2>
        <hr>

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
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in desserts" :key="item.name">
                  <td>Asset {{index + 1}}</td>
                  <td>{{ item.high }}</td>
                  <td>{{ item.low }}</td>
                  <td>{{ item.open }}</td>
                  <td>{{ item.close }}</td>
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

  export default {
    data: () => ({
      dense: false,
    fixedHeader: false,
    height: 300,
    desserts: [
      {
        high: 'Frozen Yogurt',
        low: 159,
        open: 'Frozen Yogurt',
        close: 159,
      },
    ],
    assets: true,
    
    }),
    computed: {
    },
    methods: {
      
    },
    mounted () {
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
  text-align:center;
  justify-content: center;
}

.input-field {
  width: 100px;
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