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
            {
              label: 'Effectifs cumulés',
              backgroundColor: 'rgba(217, 3, 104, 1)',
              borderColor: 'rgba(217, 3, 104, 1)',
              // borderWidth: 2,
              data: this.ds.plot.cum.eff,
              type: 'line',
              fill: false,

            },
          ],
        }, options,
      );

    },
  };
</script>
