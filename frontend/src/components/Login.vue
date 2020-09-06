<template>
 <v-app>
   
   <!-- <form class="login" @submit.prevent="login">
     <h1>Sign in</h1>
     <label>Username</label>
     <input required v-model="username" type="text" placeholder="Username"/>
     <label>Password</label>
     <input required v-model="password" type="password" placeholder="Password"/>
     <hr/>
     <button type="submit">Login</button>
   </form> -->

   <!-- <v-flex xs12 sm8 md4>
     <v-card class="elevation-12">
       <v-toolbar dark color="primary">
        <v-toolbar-title>Log in </v-toolbar-title>
      </v-toolbar>

      <v-card-text>
        <v-form>
          <v-text-field prepend-icon="person" name="username" label="username" type="text"></v-text-field>
          <v-text-field prepend-icon="email" name="email" label="email" type="text"></v-text-field>
          <v-text-field
            id="password"
            preprend-icon="lock"
            name="password"
            label="password"
            type="password">
          </v-text-field>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-space></v-space>
        <v-btn color="primary">sign up</v-btn>
        <v-btn color="primary"> to="/">cancel</v-btn>
      </v-card-actions>
     </v-card>
     </v-flex> -->

        
      

   <amplify-authenticator v-bind:authConfig="authConfig"></amplify-authenticator>
   <amplify-sign-out v-if='signedIn' button-text="Custom Text"></amplify-sign-out>

 </v-app>
</template>

<script>
import { Auth } from "aws-amplify";
import { AmplifyEventBus } from 'aws-amplify-vue';


  export default {
    // data(){
    //   return {
    //     email : "",
    //     password : ""
    //   }
    // },

    data() {
      return {
        signedIn: false
      }
    },
    created() {
      this.isUserSignedIn();
      AmplifyEventBus.$on('authState', info => {
        if(info === 'signedIn') {
          this.isUserSignedIn();
        } else {
          this.signedIn = false;
        }
      });


    },

    // methods: {
    //   login: function () {
    //     let username = this.username 
    //     let password = this.password
    //     this.$store.dispatch('login', { username, password })
    //    .then(() => this.$router.push('/'))
    //    .catch(err => console.log(err))
    //   }
    // }

    methods: {
      async isUserSignedIn() {
        try{
          const userObj = await Auth.currentAuthenticatedUser();
          this.signedIn = true;
          console.log(userObj)
          this.$router.push({path:'/'})
        } catch(err) {
          this.signedIn = false;
          console.log(err)
        }
        
      }     
    }
  };
</script>