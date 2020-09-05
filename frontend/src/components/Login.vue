<template>
 <v-app>
   <form class="login" @submit.prevent="login">
     <h1>Sign in</h1>
     <label>Username</label>
     <input required v-model="username" type="text" placeholder="Username"/>
     <label>Password</label>
     <input required v-model="password" type="password" placeholder="Password"/>
     <hr/>
     <button type="submit">Login</button>
   </form>
 </v-app>
</template>

<script>
  export default {
    data(){
      return {
        email : "",
        password : ""
      }
    },
    methods: {
      login: function () {
        let username = this.username 
        let password = this.password
        this.$store.dispatch('login', { username, password })
       .then(() => this.$router.push('/'))
       .catch(err => console.log(err))
      }
    }
  }
</script>