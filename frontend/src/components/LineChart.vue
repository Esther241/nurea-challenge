<template>
  <div>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import {
  Chart,
  LineElement,
  Title,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  LineController,
  PointElement,
  Filler,
} from "chart.js";

Chart.register(
  LineElement,
  Title,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  LineController,
  PointElement,
  Filler
);

export default {
  name: "LineChart",
  props: {
    labels: {
      type: Array,
      required: true,
    },
    data: {
      type: Array,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
    borderColor: {
      type: String,
      default: "rgba(75, 192, 192, 1)",
    },
    backgroundColor: {
      type: String,
      default: "rgba(75, 192, 192, 0.2)",
    },
  },
  mounted() {
    this.renderChart();
  },
  updated() {
    this.renderChart();
  },
  methods: {
    renderChart() {
      new Chart(this.$refs.chartCanvas, {
        type: "line",
        data: {
          labels: this.labels,
          datasets: [
            {
              label: this.label,
              data: this.data,
              borderColor: this.borderColor,
              backgroundColor: this.backgroundColor,
              fill: true,
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
          },
        },
      });
    },
  },
};
</script>

<style scoped>
canvas {
  height: 100%;
  width: 100%;
}
</style>
