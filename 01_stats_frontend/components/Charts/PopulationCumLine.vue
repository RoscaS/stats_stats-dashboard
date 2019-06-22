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
            palette: 'palette7',
          },
          grid: {
            position: 'front',
            borderColor: '#5f5f5f',
          },
          markers: {
            size: [4, 6],
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
                text: 'Effectifs cumulées',
              },
            },
            {
              opposite: true,
              title: {
                text: 'Effectif',
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
          {name: 'Effectifs cumulées', type: 'line', data: this.ds.plot.cum.eff},
          {name: 'Effectif', type: 'bar', data: this.ds.plot.freq.eff},
        ];
      },
    },
  };
</script>
