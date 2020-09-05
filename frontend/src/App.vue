<template>
  <div id="app">
    <div id="nav">
      <router-link v-if="currentRouteName!='login'">Logout</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
  export default {
    computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn},
      currentRouteName() {
        return this.$route.name.toLowerCase() || '';
      }
    },
    methods: {
      logout: function () {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
      }
    },
    created: function () {
      this.$http.interceptors.response.use(undefined, function (err) {
        return new Promise(function () {
          if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
            this.$store.dispatch(this.logout)
          }
          throw err;
        });
      });
    }
  }
</script>
