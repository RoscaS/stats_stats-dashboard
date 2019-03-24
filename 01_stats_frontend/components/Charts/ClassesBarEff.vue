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
              // barPercentage: 1.2,
              categoryPercentage: 1,
              barThickness: 'flex',
              // maxBarThickness: 8,
              // minBarLength: 2,

              gridLines: {
                // offsetGridLines: true,
              },
            },
          ],
        },
      };

      this.renderChart({
          labels: this.ds.plot.cum.ticks,
          datasets: [
            {
              label: 'Frequences cumulée',
              backgroundColor: this.colors,
              borderWidth: 2,
              data: this.ds.plot.cum.freq,
            },
            {
              label: 'Frequences cumulés',
              backgroundColor: 'rgba(217, 3, 104, 1)',
              borderColor: 'rgba(217, 3, 104, 1)',
              // borderWidth: 2,
              data: this.ds.plot.cum.freq,
              type: 'line',
              fill: false,
            },
          ],
        }, options,
      );

    },
  };
</script>
