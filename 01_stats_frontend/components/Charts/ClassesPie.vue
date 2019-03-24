<script>
  import { Pie } from 'vue-chartjs';

  export default {
    extends: Pie,
    props: {
      ds: {type: Object},
      colors: {type: Array},
    },

    mounted() {

      let labels = [];

      for (let i in this.ds.plot.freq.eff_pc) {
        labels.push(`${this.ds.plot.freq.eff[i]} (${this.ds.plot.freq.eff_pc[i]}%)`)
      }

      let options = {
        responsive: true,
        maintainAspectRatio: false,
        tooltips: {
          bodyFontSize: 16
        },
        legend: {display: false},
        // title: {display: true, text: "Fréquences"}

      };

      this.renderChart({
          labels: labels,
          datasets: [
            {
              backgroundColor: this.colors,
              borderWidth: 2,
              data: this.ds.plot.freq.eff,
            },
          ],
        }, options,
      );

    },
  };
</script>
