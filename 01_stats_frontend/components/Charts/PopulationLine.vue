<template>
  <apexcharts height="430" type="line" :options="options" :series="series"/>
</template>

<script>
  export default {
    props: {
      ds: {type: Object},
      colors: {type: Array},
      type: {type: String, default: 'category'},

    },
    data: () => ({}),

    computed: {
      options() {
        return {
          markers: {
            size: [6, 8],
          },
          chart: {
            id: 'Frequence',
            toolbar: {show: false},
          },
          xaxis: {
            type: this.type,
            categories: this.ds.plot.freq.ticks,
            tickAmount: 'dataPoints',

          },
          yaxis: [
            {
              title: {
                text: 'Effectifs',
              },
              tickAmount: 10,
            }
          ],

          plotOptions: {
            line: {
              // color: th
            },
          },
        };

      },
      series() {
        return [
          {name: 'Effectifs', type: 'line', data: this.ds.plot.cum.eff},
        ];
      },
    },
  };
</script>
