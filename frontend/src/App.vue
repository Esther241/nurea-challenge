<template>
  <div>
    <header class="header">
      <img
        src="@/assets/logo-nurea.svg"
        alt="Logo"
        class="logo"
        @click="goToPatientsList"
      />
    </header>
    <div>
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  methods: {
    goToPatientsList() {
      this.$router.push({ name: "PatientsList" });
    },
  },
};
</script>

<style scoped>
.header {
  width: 100%;
  height: 80px;
  display: flex;
  align-items: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 0 1rem;
  background-color: #2662be;
}
.logo {
  height: 80px;
  margin-right: 1rem;
  cursor: pointer;
}

@media (min-width: 1024px) {
  .logo {
    margin: 0 2rem 0 0;
    cursor: pointer;
  }
  header .wrapper {
    display: flex;
    flex-wrap: wrap;
  }
}
</style>
