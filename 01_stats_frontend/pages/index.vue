<template>


  <div class="frame">

    <div class="top-row">
      <div class="columns is-variable is-8">

        <div class="column is-3">
          <classes-pie :ds="dataSet" :colors="colors"/>
        </div>

        <div class="column is-3">
          <table class="table simple-data is-hoverable is-striped">
            <tr v-for="(idx, i) in dataSet.global" :key="idx">
              <td><b>{{ format(i) }}</b></td>
              <td> {{ dataSet.global[i] }}</td>
            </tr>
          </table>
        </div>

        <div class="column is-6">

        </div>
      </div>
    </div>

    <div class="bottom-row">
      <div class="columns is-variable is-4">
        <div class="column is-6">
          <classes-bar-line :ds="dataSet" :colors="colors"/>
        </div>
        <div class="column is-6">
          <classes-bar :ds="dataSet" :colors="colors"/>
        </div>
      </div>
    </div>
  </div>

</template>

<script>

  import axios from 'axios';
  import ClassesPie from '../components/Charts/ClassesPie';
  import ClassesBar from '../components/Charts/ClassesBarEff';
  import Header from '../components/Header';
  import ClassesBarLine from '../components/Charts/ClassesBarFreq';
  import { colorPicker } from '../assets/helpers';

  export default {
    components: {ClassesBarLine, Header, ClassesBar, ClassesPie},
    async asyncData() {
      // let {data} = await axios.get('http://localhost:8000/series/');
      let {data} = await axios.get('http://localhost:8000/classes/');
      return {dataSet: data[0].data};
    },
    data: () => ({

    }),
    computed: {
      colors() {
        return colorPicker(this.dataSet.plot.freq.ticks.length);
      }
    },

    methods: {
      format(str) {
        let clean = str.replace('_', ' ');
        return clean[0].toUpperCase() + clean.slice(1);
      },
    },
    mounted() {
      console.log(this.dataSet)
    },
  };
</script>

<style lang="scss">
  .top-row {
    padding: 60px 20px;
  }

  .bottom-row {
    padding: 20px;
    position: fixed;
    bottom: 0;
    width: 100%;
  }

</style>

