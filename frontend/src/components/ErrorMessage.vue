<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" md="6" class="d-flex justify-center">
        <v-card elevation="2">
          <v-card-title class="text-center error-title">
            Error! Something went wrong!
          </v-card-title>
          <v-card-text>Go back to the previous page</v-card-text>
          <v-card-actions class="justify-center">
            <v-btn @click="goBack" color="primary" class="error-btn"
              >Go Back</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "ErrorMessage",
  methods: {
    goBack() {
      this.$router.go(-1);
    },
  },
};
</script>

<style scoped>
.error-title {
  font-size: 1.5rem;
}

.v-card-text {
  margin-bottom: 1rem;
}
</style>
