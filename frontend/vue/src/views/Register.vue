<template>
  <div >
    <v-card class="pa-6 pb-10 pt-10 ma-auto mt-5" width="30em" elevation="4">
      <v-subheader class="subtitle-1 ml-0 pl-0 font-weight-bold">
         Register Your Account
      </v-subheader>

      <v-divider></v-divider>
      <!-- For Login Form -->
      <v-form class="mt-6" ref="form" v-model="formValidity">
        <v-text-field label="email" prepend-inner-icon="email" type="email" :rules="emailRules" v-model="email" outlined class="subtitle-2 tre" dense></v-text-field>
        <v-text-field label="first name" prepend-inner-icon="person" class="mt-5 tre" outlined dense></v-text-field>
        <v-text-field label="password" prepend-inner-icon="lock" :append-icon="passwordVisibility ? 'visibility' : 'visibility_off'" @click:append="passwordVisibility = !passwordVisibility" counter :rules="passwordRules" :type="passwordVisibility ? 'password' : 'text' " v-model="password" class="mt-5" outlined dense></v-text-field>
        <!-- for the login button-->
        <v-row justify="center" class="mt-2">
        <v-btn dark class="mt-2 purple accent-3 rounded-lg elevation-1" v-on:click="submitForm">
          <span>sign up</span>
        </v-btn>
        </v-row>
        <!-- for the other options -->
        <v-row class="mt-6" justify="center">
          <p>Already Have An Account?</p>
          <v-btn small outlined depressed class="subtitle-2 ml-3 font-weight-regular rounded-lg text-lowercase" to="/login">login</v-btn>
      </v-row>
      </v-form>
    </v-card>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>