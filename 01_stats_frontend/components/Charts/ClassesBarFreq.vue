<template>
  <apexcharts height="430" type="line" :options="options" :series="series"/>
</template>

<script>
  export default {
    props: {
      ds: {type: Object},
      colors: {type: Array},
    },
    data: () => ({}),

    computed: {
      options() {
        return {
          theme: {
            palette: 'palette3',
          },
          grid: {
            position: 'front',
            borderColor: '#5f5f5f',
          },
          markers: {
            size: [4, 6],
          },
          dataLabels: {
            enabled: true,
            style: {
                fontSize: '16px',
                fontFamily: 'Helvetica, Arial, sans-serif',
                colors: undefined
            },
          },
          chart: {
            id: 'Frequences cumulées',
            toolbar: {show: false},
          },
          xaxis: {
            type: 'category',
            categories: this.ds.plot.freq.ticks,
          },
          yaxis: [
            {
              title: {
                text: 'Frequences cumulées',
              },
            },
            {
              opposite: true,
              title: {
                text: 'Éffectifs cumulése',
              },
            },
          ],

          plotOptions: {
            bar: {
              // distributed: true,
              columnWidth: '100%',
            },
            line: {
              // color: th
            },
          },
        };

      },
      series() {
        return [
          {name: 'Frequences cumulées', type: 'line', data: this.ds.plot.cum.freq},
          {name: 'Effectifs cumulés', type: 'bar', data: this.ds.plot.cum.eff},
        ];
      },
    },
  };
</script>
