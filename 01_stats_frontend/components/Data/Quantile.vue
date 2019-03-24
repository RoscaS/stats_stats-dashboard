<template>
  <nav class="level">
    <div class="level-left">
      <div class="level-item">
        {{ format(title) }}:
      </div>
    </div>
    <div class="level-left">
      <div v-for="(k, v) in data" :key="k" class="level-item">
        <QuantileTag :Q="v" :value="k"/>
      </div>
    </div>
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

</style>
