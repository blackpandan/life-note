<template>
<nav>
  <v-app-bar app dark color="purple accent-3" elevate-on-scroll>
     <v-app-bar-nav-icon @click="drawer = !drawer" class="pa-0"></v-app-bar-nav-icon>
     <v-toolbar-title class="title font-weight-regular"><span class="life">Life</span><span class="life grey--text text--lighten-3 font-weight-normal">Book</span></v-toolbar-title>
     <v-spacer></v-spacer>
     <v-toolbar-items class="d-none d-sm-flex">
       <v-btn dark color="purple accent-3" depressed to="/">
       <v-icon left>home</v-icon>
       <span class="font-weight-regular life-l">home</span>
       </v-btn>
       <v-btn dark color="purple accent-3" depressed to="/login">
         <v-icon left>person</v-icon>
         <span class="font-weight-regular life-l">login</span>
       </v-btn>
       
     </v-toolbar-items>
     <v-toolbar-items class="d-flex d-sm-none"> 
        <v-btn icon to="/">
         <v-icon>home</v-icon>
       </v-btn>
       <v-btn icon to="/login">
         <v-icon>person</v-icon>
       </v-btn>
      
     </v-toolbar-items>
   </v-app-bar>
   <v-navigation-drawer v-model="drawer" app temporary color="grey lighten-4">
     <v-container fluid>
       <v-avatar size="96"><v-img src="../assets/head.png" alt="hey"></v-img></v-avatar>
       <v-card flat class="grey lighten-4">
         <v-card-title class="ma-0 pa-2 ">anonymous</v-card-title>
         <v-card-subtitle class="pa-0 pa-2">login@gmail.com</v-card-subtitle>
       </v-card>
       <v-divider color="font-size-5 purple accent-3"></v-divider>
     </v-container>
       <v-list rounded>
           <v-list-item-group>
             <v-list-item to="/">
               <v-list-item-icon>
                 <v-icon>home</v-icon>
               </v-list-item-icon>
               <v-list-item-content>
                 <v-list-item-title>
                 Home
                 </v-list-item-title>
               </v-list-item-content>
             </v-list-item>

             <v-list-item to="/tasks">
               <v-list-item-icon>
                 <v-icon>event</v-icon>
               </v-list-item-icon>
               <v-list-item-content>
                 <v-list-item-title>Tasks</v-list-item-title>
               </v-list-item-content>
             </v-list-item>

             <v-list-item to="/projects">
               <v-list-item-icon>
                 <v-icon>assignment</v-icon>
               </v-list-item-icon>
               <v-list-item-content>
                 <v-list-item-title>
                   Projects
                 </v-list-item-title>
               </v-list-item-content>
             </v-list-item>

             <v-list-item to="/login">
               <v-list-item-icon>
                 <v-icon>login</v-icon>
               </v-list-item-icon>
               <v-list-item-content>
                 <v-list-item-title>
                   login
                 </v-list-item-title>
               </v-list-item-content>
             </v-list-item>
           </v-list-item-group>
       </v-list>
   </v-navigation-drawer>
</nav>
</template>

<script>
export default {
data(){
    return{
        drawer: true
    }
}
}
</script>

<style lang="scss" scoped>
.life{
  font-size: 1em;
  &-l{
    font-size: 0.95em;
  }
}
</style>