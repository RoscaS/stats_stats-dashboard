<template>
  <apexcharts height="430" type="bar" :options="options" :series="series"/>
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
          colors: this.colors,
          legend: {
            show: true,
            showForSingleSeries: true,
          },
          chart: {
            id: 'Effectifs',
            toolbar: {show: false},
          },
          xaxis: {
            type: 'category',
            categories: this.ds.plot.freq.ticks,

          },
          plotOptions: {
            bar: {
              distributed: true,
              columnWidth: '100%',
            },
          },
        };
      },
      series() {
        return [
          {name: 'Effectifs', data: this.ds.plot.freq.eff},
        ];
      },
    },
  };
</script>

<style lang="scss">


</style>
