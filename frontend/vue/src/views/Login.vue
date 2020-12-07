<template>
  <div>
    <v-card class="pa-6 pb-10 pt-10 ma-auto" width="30em">
      <v-subheader class="subtitle-1 ml-0 pl-0 font-weight-bold">
        Login To Your Account
      </v-subheader>

      <v-divider></v-divider>
      <!-- For Login Form -->
      <v-form class="mt-6">
        <v-text-field label="email" prepend-inner-icon="email" :rules=[rules.required] v-model="email"></v-text-field>
        <v-text-field label="first name" prepend-inner-icon="person"></v-text-field>
        <v-text-field label="password" prepend-inner-icon="lock" :rules="[rules.required, rules.maxlength]"></v-text-field>
        <!-- for the login button-->
        <v-row justify="center mt-2">
        <v-btn dark class="mt-2 purple accent-3 rounded-lg elevation-1" >
          <span>login</span>
        </v-btn>
        </v-row>
        <!-- for the other options -->
        <v-row class="mt-6" justify="center">
          <p>Dont Have An Account?</p>
          <v-btn small outlined depressed class="subtitle-2 ml-3 font-weight-regular rounded-lg text-lowercase">register</v-btn>
      </v-row>
      </v-form>
    </v-card>
  </div>
</template>

<script>
export default {
data(){
  return {
    rules:{
        required: value => !!value || "Required",
        maxLength: value => value < 6 || "Password must be more than 6 digits" 
      }
    }
  }
}
</script>

<style>

</style>