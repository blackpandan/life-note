<template>
 <v-app>
   <NavBar />

   <v-main>
     <v-container fluid class="pa-5">
       <router-view></router-view>
     </v-container>
   </v-main>
 </v-app>
</template>

<script>
import NavBar from './components/nav.vue'

export default {
  name: 'App',

  components: {
    NavBar
  },

  data: () => ({
    //
  }),
};
</script>
