<template>
  <div>
    <h1 class="subtitle-1 grey--text text--darken-1">Welcome!</h1>

    <!-- Action Panel -->
    <div>
      <v-card flat small class="pa-0 px-6 py-2 grey lighten-4 border-radius-lg">
        <v-row class="pa-0">
          <v-card-title class="addEvents__text pa-0 font-weight-regular">Add Events</v-card-title>
          <v-spacer></v-spacer>

          <!-- Dialog For Adding New Event, Project or Reminder -->
          <v-dialog v-model="dialog" width="59vw">
            <template v-slot:activator="{on, attrs}">
              <v-card-actions class="pa-0">
                <v-btn
                  fab
                  x-small
                  dark
                  depressed
                  color="#24F900"
                  class="pa-0"
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-icon class="white--text" color="white">add</v-icon>
                </v-btn>
              </v-card-actions>
            </template>
            
            <!-- Dialog form -->
            <v-card>
              <v-form>
                <v-container fluid>
                  <v-select :items="items" label="type" dense solo prepend-icon="event" flat></v-select>
                  <v-text-field label="title"></v-text-field>
                  <v-textarea rows="3" label="description"></v-textarea>
                  <v-btn small dark class="purple accent-3">
                    <span>submit</span>
                  </v-btn>
                </v-container>
              </v-form>
            </v-card>
          </v-dialog>
        </v-row>
      </v-card>

      <!-- Activity Area-->
      <v-expansion-panels focusable class="mt-9">
        <!--Model For Ongoing Activity-->
        <v-expansion-panel>
          
          <v-expansion-panel-header class="expansionPanel__header text-capitalize topExpansionPanel font-weight-light">
            go to the doctor
            <template v-slot:actions>
              <v-icon color="purple accent-3">$expand</v-icon>
            </template>
          </v-expansion-panel-header>
          
          <v-divider></v-divider>
          
          <v-expansion-panel-content>
            
            <v-column>
              <br />
              <p class="expansionPanel__text">i need to go to the doctor for my eye checkup</p>
              <br />
              <v-row>
                <v-btn small dark color="#24F900">
                  <span class="expansionPanel__button-text">done</span>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn small dark color="#F9D500">
                  <span class="expansionPanel__button-text">pause</span>
                </v-btn>
                <v-btn small class="error ml-3">
                  <span class="expansionPanel__button-text">delete</span>
                </v-btn>
              </v-row>
            </v-column>
          
          </v-expansion-panel-content>
        </v-expansion-panel>
        
        <!-- Model For Paused Activity -->
        <v-expansion-panel class="pause">
          <v-expansion-panel-header
            class="expansionPanel__header text-capitalize font-weight-regular"
            disable-icon-rotate
          >
            <span class="pause-text">go to the doctor</span>
            <template v-slot:actions>
              <v-icon color="#F9D500">pause</v-icon>
            </template>
          </v-expansion-panel-header>
          <v-divider></v-divider>
          <v-expansion-panel-content>
            <v-column>
              <br />
              <p class="expansionPanel__text">i need to go to the doctor for my eye checkup</p>
              <br />
              <v-row>
                <v-btn small dark color="#F9D500">
                  <span class="expansionPanel__button-text">cotinue</span>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn small class="error">
                  <span class="expansionPanel__button-text">delete</span>
                </v-btn>
              </v-row>
            </v-column>
          </v-expansion-panel-content>
        </v-expansion-panel>
        
        <!-- Model For Finished Activity -->
        <v-expansion-panel class="complete">
          
          <v-expansion-panel-header
            class="expansionPanel__header text-capitalize font-weight-regular"
            disable-icon-rotate
          >
            <span class="complete-text">go to the doctor</span>
            <template v-slot:actions>
              <v-icon color="#24F900">check</v-icon>
            </template>
          </v-expansion-panel-header>
          
          <v-divider></v-divider>
          
          <v-expansion-panel-content>
            <v-column>
              <br />
              <p class="expansionPanel__text">i need to go to the doctor for my eye checkup</p>
              <br />
              <v-row>
                <v-btn small dark color="#24F900" depressed>
                  <span class="expansionPanel__button-text">complete</span>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn small class="error">
                  <span class="expansionPanel__button-text">delete</span>
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
  data() {
    return {
      // controller for dialog visibility
      dialog: false,
      //items for dialog form, type chooser
      items: ["project", "event", "todo"],
    };
  },
};
</script>

<style lang="scss" scoped>
$green: #24f900;
.topExpansionPanel{
  border-top: 2px solid #d500f9;
}
  .expansionPanel {
    &__header{
    font-size: 1.1em;
  }
  
  &__text {
    font-size: 1em;
  }
  &__button {
    &-text{
    font-size: 0.8em;
    }
  }
  }
.addEvents {
    &__text{
    font-size: 1em;
    }
  }
.pause {
  border-left: 0.2em solid #f9d500;
  &-text {
    color: #f9d500;
  }
}

.complete {
  border-left: 0.2em solid $green;
  // background-color: black;
  &-text {
    color: $green;
  }
}
</style>