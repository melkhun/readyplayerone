<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      color="primary"
      dark
      app
    >
      <v-list dense>
        <v-list-item two-line>
          <v-list-item-avatar tile >
            <img src="./assets/team_logov2.png">
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

    <v-app-bar
      app
      color="white"
      flat
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-main>
      <v-card>
    <v-tabs
      background-color="white"
      color="deep-purple accent-4"
      right
    >
      <v-tab>Calculator</v-tab>
      <v-tab>Quick Start</v-tab>
      <v-tab>My Portfolio</v-tab>
      <v-tab>Login</v-tab>
      <v-tab>Sign Up</v-tab>
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
    <v-footer
      color="secondary"
      app
    >
      <span class="white--text">&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import Calculator from './components/Calculator'
import QuickStart from './components/QuickStart'
import Login from './components/Login'
import SignUp from './components/SignUp'

export default {
  components: {
    Calculator,
    QuickStart,
    Login,
    SignUp
  },
  props: {
    source: String,
  },
  data: () => ({
    drawer: null,
  }),
  methods: {
  }
}
</script>