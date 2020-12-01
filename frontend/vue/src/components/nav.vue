<template>
<nav>
  <v-app-bar app dark color="purple accent-3" elevate-on-scroll>
     <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
     <v-toolbar-title class="title"><span class="">Life</span><span class="grey--text text--lighten-4 font-weight-light">Note</span></v-toolbar-title>
     <v-spacer></v-spacer>
     <v-toolbar-items>
       <v-btn dark color="purple accent-3" depressed>
         <v-icon left>person</v-icon>
         <span class="font-weight-normal">login</span>
       </v-btn>
     </v-toolbar-items>
   </v-app-bar>
   <v-navigation-drawer v-model="drawer" app temporary color="grey lighten-4">
       <v-list rounded>
           <v-list-item-group>
             <v-list-item>
               <v-list-item-icon>
                 <v-icon>shopping_cart</v-icon>
               </v-list-item-icon>
               <v-list-item-content>
                 <v-list-item-title>cart</v-list-item-title>
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

<style>

</style>