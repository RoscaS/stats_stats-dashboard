<template>
  <apexcharts type=pie width="100%" :options="options" :series="series"/>
</template>

<script>

  export default {
    props: {
      ds: {type: Object},
      colors: {type: Array},
    },
    computed: {
      options() {
        return {
          colors: this.colors,
          labels: this.ds.plot.freq.ticks,
        };
      },
      series() {
        return this.ds.plot.freq.eff;
      },
    },
  };
</script>
