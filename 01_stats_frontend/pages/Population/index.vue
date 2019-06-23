<template>

  <div class="frame">

    <div class="top-row" @click="toggleRange()">
      <div class="columns">
        <div class="column is-9">
          <data-tiles :data="dataSet.study"></data-tiles>
        </div>
      </div>
    </div>

    <div class="bottom-row">
      <div class="columns is-variable is-4">
        <div class="column is-12">
          <population-cum-line :ds="dataSet" :colors="colors" :show-range="showRange"/>
        </div>
      </div>
    </div>
  </div>

</template>

<script>


  import axios from 'axios';
  import Header from '../../components/Header';
  import ClassesPie from '../../components/Charts/ClassesPie';
  import ClassesBarFreq from '../../components/Charts/ClassesBarFreq';
  import ClassesBarEff from '../../components/Charts/ClassesBarEff';
  import DataTiles from '../../components/Data/DataTiles';
  import { colorPicker } from '../../assets/helpers';
  import PopulationLine from '../../components/Charts/PopulationLine';
  import PopulationCumLine from '../../components/Charts/PopulationCumLine';

  export default {
    components: {
      PopulationCumLine,
      PopulationLine, Header, DataTiles, ClassesBarEff, ClassesBarFreq, ClassesPie},
    async asyncData() {
      let {data} = await axios.get('http://localhost:8000/series/');
      // let {data} = await axios.get('http://localhost:8000/classes/');
      return {
        dataSet: data[0].data
      };
    },
    data: () => ({
      showRange: false,
      images: {mode: false, }
    }),

    computed: {
      colors() {
        return colorPicker(this.dataSet.plot.freq.ticks.length);
      },
    },
    methods: {
      toggleRange() {
        this.showRange = !this.showRange;
      }
    },
  };
</script>

<style lang="scss">
  .top-row {
    padding: 50px 20px 50px 20px;
  }

  .bottom-row {
    padding: 20px;
    width: 100%;
  }

</style>

