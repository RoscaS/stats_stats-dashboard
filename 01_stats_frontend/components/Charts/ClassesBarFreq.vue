<script>
  import { Bar } from 'vue-chartjs';

  export default {
    extends: Bar,
    props: {
      ds: {type: Object},
      colors: {type: Array},
    },
    data: () => ({}),

    mounted() {

      let options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [
            {
              categoryPercentage: 1,
              barThickness: 'flex',
              gridLines: {
              },
              ticks: {
                  beginAtZero: false
              },
            },
          ],
        },
      };

      this.renderChart({
          labels: this.ds.plot.freq.ticks,
          datasets: [
            {
              label: 'Effectifs',
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
