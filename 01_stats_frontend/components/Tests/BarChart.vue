<script>
  import { Bar, mixins } from 'vue-chartjs';
  const { reactiveProp } = mixins;

  export default {
    extends: Bar,
    mixins: [reactiveProp],
    name: 'BarChart',
    props: {
      data: {type: Object},
      options: {type: Object},
    },
    mounted() {
      this.renderChart(this.data, this.options);
    },
  };
</script>

