<template>
  <v-dialog :v-model="showModal" max-width="500px">
    <v-card>
      <v-card-title class="headline">Error</v-card-title>
      <v-card-text>
        <p>We encountered an issue while processing your request.</p>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "ErrorModal",
  props: {
    showModal: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style scoped>
.v-dialog {
  z-index: 2000;
}
.headline {
  font-size: 1.25rem;
}
</style>
