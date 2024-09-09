import { createRouter, createWebHistory } from "vue-router";
import PatientsList from "./components/PatientsList.vue";
import PatientDetails from "./components/PatientDetails.vue";
import ErrorMessage from "./components/ErrorMessage.vue";

const routes = [
  { path: "/", name: "PatientsList", component: PatientsList },
  {
    path: "/patient/:id",
    name: "PatientDetails",
    component: PatientDetails,
    props: true,
  },
  { path: "/:pathMatch(.*)*", name: "ErrorMessage", component: ErrorMessage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
