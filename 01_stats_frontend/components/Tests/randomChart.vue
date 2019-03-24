<template>
  <div class="small">
    <BarChart :chart-data="datacollection"></BarChart>
    <button @click="fillData()">Randomize</button>
  </div>
</template>

<script>
  import BarChart from './BarChart';

  export default {
    components: {BarChart},
    props: {
      dataSet: {type: Object },
    },
    data() {
      return {
        datacollection: null,
      };
    },
    computed: {
      counts() {
        return this.dataSet.counts;
      }
    },

    methods: {
      buildClasses() {
        let span = this.dataSet.span;
      },
      fillData() {
        this.datacollection = {
          labels: [this.getRandomInt(), this.getRandomInt()],
          datasets: [
            {
              label: 'Data One',
              backgroundColor: 'rgba(54, 162, 235, 0.6)',
              data: [this.getRandomInt(), this.getRandomInt()],
            }, {
              label: 'Data Two',
              backgroundColor: 'rgba(255, 99, 132, 0.6)',
              data: [this.getRandomInt(), this.getRandomInt()],
            },
          ],
        };
      },
      getRandomInt() {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
      },
    },
    mounted() {
      this.buildClasses();
      this.fillData();
    },
  };
</script>

<style>
  .small {
    max-width: 600px;
    margin: 150px auto;
  }
</style>
