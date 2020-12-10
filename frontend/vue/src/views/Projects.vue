<template>
  <v-container fluid>
    <v-expansion-panels>
      <v-expansion-panel v-for="(project, i) in projects" :key="i">
        <v-expansion-panel-header v-on:click="project.done = true" class="subtitle-2">{{ project.title }}-{{ i+1 }}</v-expansion-panel-header>
        <v-divider></v-divider>
        <v-expansion-panel-content>
          <p class="mt-6">
            {{ project.body }}
          </p>
          <p class="grey--text mt-6">time: {{ project.time }}</p>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-container>
</template>

<script>
export default {
data(){
  return {
    projects: [
      {
        title: "Portfolio",
        body: "Create a portfolio for yourself it should contain all your works and updates itself",
        time: "30 dec 2020",
        done: false
      },
       {
        title: "Portfolio",
        body: "Create a portfolio for yourself it should contain all your works and updates itself",
        time: "30 dec 2020",
        done: false
      },
       {
        title: "Portfolio",
        body: "Create a portfolio for yourself it should contain all your works and updates itself",
        time: "30 dec 2020",
        done: false
      }
    ]
  }
}
}
</script>

<style lang="scss" scoped>

</style>