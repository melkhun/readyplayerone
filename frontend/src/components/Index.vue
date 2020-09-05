<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" color="primary" dark app>
      <v-list dense>
        <v-list-item two-line>
          <v-list-item-avatar tile>
            <img src="../assets/team_logov2.png" />
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title>READYPLAYER1</v-list-item-title>
            <v-list-item-subtitle>Subtext</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app color="white" flat>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-main>
      <v-card>
        <v-tabs background-color="white" color="deep-purple accent-4" right>
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
              <Calculator></Calculator>
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

<script>
import Home from "../components/Home";
import Calculator from "../components/Calculator";
import QuickStart from "../components/QuickStart";

export default {
  components: {
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
#app {
  text-align: center;
}

.container {
  padding: 5rem 0;
  background-color: #7749bd;
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
