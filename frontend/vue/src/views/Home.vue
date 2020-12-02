<template>
  <div>
    <h1 class="subtitle-1 grey--text text--darken-1">Welcome!</h1>
    <div class="">
      <v-card flat small class="pa-0 px-6 py-2 grey lighten-4 border-radius-lg">
        <v-layout class="pa-0">
          <v-row class="pa-0">
            <v-card-title class="subtitle-1 pa-0">Add Events</v-card-title>
            <v-spacer></v-spacer>

            <v-dialog v-model="dialog" width="59vw">
            <template v-slot:activator="{on, attrs}">
            <v-card-actions class="pa-0">
            
            <v-btn fab x-small dark depressed color="#24F900" class="pa-0">
              <v-icon class="white--text" v-bind="attrs" v-on="on">add</v-icon>
            </v-btn>
            </v-card-actions>
            </template>

            <v-card>
              <v-form>
                <v-container fluid>
                  <v-select :items="items" label="type" dense solo prepend-icon="event"></v-select>
                <v-text-field label="title"></v-text-field>
                <v-textarea rows="3" label="description"></v-textarea>
                  <v-btn small dark class="purple accent-3"><span>submit</span></v-btn>
                </v-container>
              </v-form>
            </v-card>

            </v-dialog>
          </v-row>
        </v-layout>
      </v-card>
      <br>
      <v-divider></v-divider>
      <br>
      <v-expansion-panels focusable >
        <v-expansion-panel >
          <v-expansion-panel-header class="cus-h text-capitalize font-weight-regular">
            go to the doctor
             <template v-slot:actions>
            <v-icon color="purple accent-3">
              $expand
            </v-icon>
             </template>
            </v-expansion-panel-header>
          <v-divider></v-divider>
        <v-expansion-panel-content>
          <v-column>
           <br>
          <p class="cus-p">i need to go to the doctor for my eye checkup</p>
          <br>
          <v-row>
            <v-btn small dark color="#24F900">
              <span class="cus-b">done</span>
            </v-btn>
         <v-spacer></v-spacer>
         <v-btn small dark color="#F9D500">
              <span class="cus-b">pause</span>
            </v-btn>
          <v-btn small class="error ml-3">
            <span class="cus-b">delete</span>
          </v-btn>
           </v-row>
          </v-column>
        </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel disabled class="pause">
          <v-expansion-panel-header class="cus-h text-capitalize font-weight-regular" disable-icon-rotate>
            <span class="pause-text" >go to the doctor</span>
             <template v-slot:actions>
            <v-icon color="#24F900">check</v-icon>
          </template>
            </v-expansion-panel-header>
          <v-divider></v-divider>
        <v-expansion-panel-content>
          <v-column>
           <br>
          <p class="cus-p">i need to go to the doctor for my eye checkup</p>
          <br>
          <v-row>
            <v-btn small dark color="#24F900">
              <span>complete</span>
            </v-btn>
         <v-spacer></v-spacer>
          <v-btn small class="error">
            <span>delete</span>
          </v-btn>
           </v-row>
          </v-column>
        </v-expansion-panel-content>
       
        </v-expansion-panel>
      </v-expansion-panels>
    
    </div>
  </div>
</template>

<script>
export default {
data(){
  return{
    dialog : false,
    items : ["project", "event", "todo"]
  }
}
}
</script>

<style lang="scss" scoped>
.cus{
  &-h{
    font-size: 1.1em;
  }
  &-p{
    font-size: 1em;
  }
  &-b{
    font-size: 0.8em;
  }
}
.pause{
  border-left:0.2em solid #F9D500;
  &-text{
    color: #F9D500;
  }
}
</style>