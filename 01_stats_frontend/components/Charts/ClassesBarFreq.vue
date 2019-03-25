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
          // colors: this.colors,
          grid: {
            position: 'front',
            borderColor: '#5f5f5f',
          },
          markers: {
            size: [4, 6],
          },
          chart: {
            id: 'Frequence',
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
              // tickAmount: 10,
            },
            {
              opposite: true,
              title: {
                text: 'Éffectifs cumulés',
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
          {name: 'Frequence', type: 'bar', data: this.ds.plot.cum.eff},
          {name: 'Effectifs', type: 'line', data: this.ds.plot.cum.freq},
        ];
      },
    },
  };
</script>
