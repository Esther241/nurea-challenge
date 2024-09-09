<template>
  <v-container fluid>
    <v-row no-gutters>
      <!-- Patient Details Card -->
      <v-col
        v-if="patientData"
        cols="12"
        md="3"
        class="d-flex flex-column align-start pa-3"
      >
        <v-card class="pa-4" elevation="2" height="100%">
          <v-card-title>Patient Details</v-card-title>
          <v-card-text>
            <p>
              <span class="text"> Medical Number: </span>
              {{ patientData.medicalRecordNumber }}
            </p>
            <p>
              <span class="text">First Name: </span> {{ patientData.firstName }}
            </p>
            <p>
              <span class="text"> Last Name: </span>{{ patientData.lastName }}
            </p>
            <p><span class="text">Age: </span>{{ patientData.age }}</p>
          </v-card-text>
        </v-card>
      </v-col>
      <!-- Graphs -->
      <v-col>
        <v-row>
          <v-col md="6" class="pa-2">
            <v-card flat v-if="heartRate.length > 0">
              <v-card-title>Heart Rate</v-card-title>
              <line-chart
                :labels="labels"
                :data="heartRate"
                label="Heart Rate"
                borderColor="rgba(75, 192, 192, 1)"
                backgroundColor="rgba(75, 192, 192, 0.2)"
              ></line-chart>
            </v-card>
          </v-col>
          <v-col cols="12" md="6" class="pa-2">
            <v-card flat v-if="temperature.length > 0">
              <v-card-title>Temperature</v-card-title>
              <line-chart
                :labels="labels"
                :data="temperature"
                label="Temperature"
                borderColor="rgba(255, 99, 132, 1)"
                backgroundColor="rgba(255, 99, 132, 0.2)"
              ></line-chart>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="6" class="pa-2">
            <v-card flat v-if="bloodPressureSystolic.length > 0">
              <v-card-title>Blood Pressure Systolic</v-card-title>
              <line-chart
                :labels="labels"
                :data="bloodPressureSystolic"
                label="Blood Pressure Systolic"
                borderColor="rgba(153, 102, 255, 1)"
                backgroundColor="rgba(153, 102, 255, 0.2)"
              ></line-chart>
            </v-card>
          </v-col>
          <v-col cols="12" md="6" class="pa-2">
            <v-card flat v-if="bloodPressureDiastolic.length > 0">
              <v-card-title>Blood Pressure Diastolic</v-card-title>
              <line-chart
                :labels="labels"
                :data="bloodPressureDiastolic"
                label="Blood Pressure Diastolic"
                borderColor="rgba(255, 159, 64, 1)"
                backgroundColor="rgba(255, 159, 64, 0.2)"
              ></line-chart>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <error-modal v-model="showErrorModal" />
  </v-container>
</template>

<script>
import axios from "axios";
import LineChart from "./LineChart.vue";
import ErrorModal from "./ErrorModal.vue";

export default {
  name: "PatientDetails",
  components: {
    LineChart,
    ErrorModal,
  },
  data() {
    return {
      labels: [],
      patientData: null,
      heartRate: [],
      temperature: [],
      bloodPressureSystolic: [],
      bloodPressureDiastolic: [],
      showErrorModal: false,
    };
  },
  async mounted() {
    await this.getPatientDetails();
  },
  methods: {
    async getPatientDetails() {
      const patientId = this.$route.params.id;

      try {
        const { data: patient } = await axios.get(
          `http://localhost:8000/patients/${patientId}`
        );
        if (patient && patient.vitals) {
          this.patientData = patient;
          const { heartRate, temperature, bloodPressure } = patient.vitals;

          this.heartRate = heartRate;
          this.temperature = temperature;
          this.bloodPressureSystolic = bloodPressure.map((e) => e.systolic);
          this.bloodPressureDiastolic = bloodPressure.map((e) => e.diastolic);

          const maxDataLength = Math.max(
            heartRate.length,
            temperature.length,
            this.bloodPressureSystolic.length,
            this.bloodPressureDiastolic.length
          );

          this.labels = this.generateLabels(maxDataLength);
        }
      } catch (error) {
        this.showErrorModal = true;
      }
    },
    generateLabels(count) {
      // Generate labels for the last 24 hours
      const now = new Date();
      const maxCount = Math.min(count, 24);
      const labels = [];

      const interval = 24 / maxCount;

      for (let i = 0; i < maxCount; i++) {
        const date = new Date(now.getTime() - i * interval * 3600 * 1000);
        labels.push(
          `${String(date.getHours()).padStart(2, "0")}:${String(
            date.getMinutes()
          ).padStart(2, "0")}`
        );
      }
      return labels.reverse();
    },
  },
};
</script>

<style scoped>
.graph-card {
  height: 300px;
  width: 100%;
}
.text {
  font-weight: bold;
}
</style>
