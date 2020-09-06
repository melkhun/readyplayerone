<template>
  <v-app>
    <v-app-bar app color="#828deb" flat>
      
          <v-list-item-avatar tile>
            <img src="../assets/team_logov2.png" />
          </v-list-item-avatar>
          <v-list-item-content style="text-align:left;">
            <v-list-item-title float-left>READY PLAYER 1</v-list-item-title>
            <v-list-item-subtitle>Financially Ready in 3, 2, 1</v-list-item-subtitle>
          </v-list-item-content>
   


    </v-app-bar>

    <v-main>
    
      <v-card>
        <v-tabs background-color="white" color="deep-purple accent-4" right class="fixed-tabs-bar">
          <v-tab>Home</v-tab>
          <v-tab>Calculator</v-tab>
          <v-tab>Quick Start</v-tab>
          <v-tab>My Portfolio</v-tab>
          <v-tab @click="logout">Logout</v-tab>
          <v-tab-item>
            <v-container fluid>
              <Home></Home>
            </v-container>
          </v-tab-item>
          <v-tab-item>
            <v-container fluid>
              <Calculator></Calculator>
            </v-container>
          </v-tab-item>
          <v-tab-item>
            <v-container fluid>
              <QuickStart></QuickStart>
            </v-container>
          </v-tab-item>
          <v-tab-item>
            <v-container fluid>
              <Portfolio></Portfolio>
            </v-container>
          </v-tab-item>
          <v-tab-item>
            <v-container fluid>
              <Login></Login>
            </v-container>
          </v-tab-item>
          <v-tab-item>
            <v-container fluid>
              <SignUp></SignUp>
            </v-container>
          </v-tab-item>
        </v-tabs>
      </v-card>
    </v-main>
    <v-footer color="secondary" app>
      <span class="white--text">&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js"></script>
<script src="https://unpkg.com/vue-chartjs/dist/vue-chartjs.min.js"></script>
<script>
import Home from "../components/Home";
import Calculator from "../components/Calculator";
import QuickStart from "../components/QuickStart";
import Portfolio from "../components/Portfolio";

export default {
  components: {
    Portfolio,
    Calculator,
    QuickStart,
    Home,
  },
  props: {
    source: String,
  },
  data: () => ({
    drawer: null,
  }),
  methods: {
    logout: function() {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/login");
      });
    },
  },
};
</script>

<style>

.fixed-tabs-bar .v-tabs-bar {
    position: -webkit-sticky;
    position: sticky;
    top: 4rem;
    z-index: 2;
}

#app {
  text-align: center;
}

.container {
  padding: 2rem 0 2rem 0;
  background-color: #828deb;
}

.circle {
  position: absolute;
  border-radius: 100%;
}

.circle.circle-purple {
  border: 10px solid #f2eafa;
  opacity: 0.1;
  width: 4vw;
  height: 4vw;
  left: 10%;
  top: 25%;
}

.circle.circle-purple1 {
  border: 15px solid #f2eafa;
  opacity: 0.1;
  width: 8vw;
  height: 8vw;
  right: -2%;
  bottom: 17%;
}
.circle.circle-purple2 {
  background-color: #f2eafa;
  opacity: 0.1;
  width: 5vw;
  height: 5vw;
  left: 20%;
  bottom: 17%;
}

.circle.circle-purple3 {
  border: 15px solid #f2eafa;
  opacity: 0.3;
  width: 3vw;
  height: 3vw;
  top: 80%;
  left: 60%;
}

.text-blue {
  color: rgb(0, 102, 255);
  font-size: 300;
  justify-content: center;
}
</style>
