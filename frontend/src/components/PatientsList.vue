<template>
  <v-container class="mt-16">
    <v-card flat>
      <v-card-title
        class="d-flex justify-space-between align-center border-thin"
      >
        <h2>Patients</h2>
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="searchPatient"
        item-value="id"
        hide-default-footer
      >
        <template v-slot:item="patient">
          <tr @click="goToPatientDetails(patient.item.id)" class="row">
            <td>{{ patient.item.medicalRecordNumber }}</td>
            <td>{{ patient.item.firstName }}</td>
            <td>{{ patient.item.lastName }}</td>
            <td>{{ patient.item.age }}</td>
            <td>{{ getHeartRate(patient.item) }}</td>
            <td>{{ getTemperature(patient.item) }}</td>
            <td>{{ getBloodPressure(patient.item) }}</td>
          </tr>
        </template>
      </v-data-table>
    </v-card>
    <error-modal v-model="showErrorModal" />
  </v-container>
</template>

<script>
import axios from "axios";
import ErrorModal from "./ErrorModal.vue";

export default {
  name: "PatientsList",
  components: { ErrorModal },
  data() {
    return {
      patients: [],
      search: "",
      showErrorModal: false,
      currentIndex: 0,
      indices: {},
      interval: null,
      headers: [
        {
          text: "Medical Number",
          value: "medicalRecordNumber",
          title: "Medical Number",
        },
        {
          text: "FirstName",
          value: "firstName",
          title: "First name",
        },
        {
          text: "LastName",
          value: "lastName",
          title: "Last name",
        },
        {
          text: "Age",
          value: "age",
          title: "Age",
        },
        {
          text: "vitals",
          value: "vitals.heartRate",
          title: "Heart Rate",
        },
        {
          text: "vitals",
          value: "vitals.temperature",
          title: "Temperature",
        },
        {
          text: "vitals",
          value: "vitals.bloodPressure",
          title: "Blood Pressure",
        },
      ],
    };
  },
  computed: {
    searchPatient() {
      const searchPatient = this.search.toLowerCase();

      return this.patients.filter((patient) => {
        const fullName =
          `${patient.firstName} ${patient.lastName}`.toLowerCase();
        const medicalNumber = patient.medicalRecordNumber.toLowerCase();
        return (
          fullName.includes(searchPatient) ||
          medicalNumber.includes(searchPatient)
        );
      });
    },
  },
  mounted() {
    this.getPatients();
    this.interval = setInterval(() => {
      this.updateCurrentIndex();
      this.getPatients();
    }, 60000); // Set regular intervals every 60 seconds
  },
  beforeUnmount() {
    if (this.interval) {
      clearInterval(this.interval);
    }
  },
  methods: {
    async getPatients() {
      try {
        const { data } = await axios.get("http://localhost:8000/patients");
        this.patients = data;
        this.patients.forEach((patient) => {
          if (!this.indices[patient.id]) {
            this.indices[patient.id] = {
              heartRate: 0,
              temperature: 0,
              bloodPressure: 0,
            };
          }
        });
      } catch (error) {
        this.showErrorModal = true;
      }
    },
    updateCurrentIndex() {
      this.patients.forEach((patient) => {
        const currentIndices = this.indices[patient.id];

        if (currentIndices) {
          currentIndices.heartRate = Math.min(
            currentIndices.heartRate + 1,
            patient.vitals.heartRate.length - 1
          );
          currentIndices.temperature = Math.min(
            currentIndices.temperature + 1,
            patient.vitals.temperature.length - 1
          );
          currentIndices.bloodPressure = Math.min(
            currentIndices.bloodPressure + 1,
            patient.vitals.bloodPressure.length - 1
          );
        }
      });
    },
    getHeartRate(patient) {
      const index = this.indices[patient.id]?.heartRate || 0;
      return patient.vitals.heartRate[index] || "NA";
    },
    getTemperature(patient) {
      const index = this.indices[patient.id]?.temperature || 0;
      return patient.vitals.temperature[index] || "NA";
    },
    getBloodPressure(patient) {
      const index = this.indices[patient.id]?.bloodPressure || 0;
      const bp = patient.vitals.bloodPressure[index];
      return bp ? `${bp.systolic}/${bp.diastolic}` : "NA";
    },
    goToPatientDetails(patientId) {
      this.$router.push({ name: "PatientDetails", params: { id: patientId } });
    },
  },
};
</script>

<style>
.table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #dddbdb;
}

th {
  background-color: #b8ddf9;
}

.row {
  cursor: pointer;
}
</style>
