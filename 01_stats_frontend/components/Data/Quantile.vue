<template>
  <nav class="line">
    <div class="line-title">
      {{ format(title) }}:
    </div>
    <div v-for="(k, v) in data" :key="k" class="line-content">
      <QuantileTag :Q="v" :value="k"/>
    </div>
    <hr>
  </nav>
</template>

<script>
  import QuantileTag from './QuantileTag';
  import { format } from '../../assets/helpers';

  export default {
    components: {QuantileTag},
    props: {
      title: {type: String},
      data: {type: Object},
    },
    methods: {
      format(str) { return format(str); },
    },
  };
</script>

<style lang="scss" scoped>

  .line {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: flex-start;

    .line-title {
      margin-top: 10px;
      /*margin-right: auto;*/
    }

    .line-content {
      margin-top: 10px;
      /*margin-left: auto;*/
    }
  }

</style>
