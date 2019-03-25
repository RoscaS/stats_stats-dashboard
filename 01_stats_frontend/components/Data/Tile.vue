<template>
  <div class="card">

    <header class="card-header">
      <p class="card-header-title">
        {{ format(title) }}
      </p>
    </header>

    <div class="card-content">
      <div class="content">
        <table v-if="title !== 'Quantiles'" class="table">
          <tr v-for="(idx, i) in data" :key="i">
            <td class="data-label">{{ format(i) }}:</td>
            <td v-if="coefficients.includes(i)" :title="data[i].info"> {{ data[i].data }}</td>
            <td v-else> {{ data[i] }}</td>
          </tr>
        </table>

        <div v-else>
          <Quantile v-for="(idx, i) in data" :key="i" :data="data[i]" :title="i"/>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
  import { format } from '../../assets/helpers';
  import Quantile from './Quantile';

  export default {
    components: {Quantile},
    data: () => ({
      coefficients: ['coefficient_de_variation', 'coefficient_asymetrie', 'coefficient_applatissement']
    }),
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

  .card {
    /*border-radius: 5px;*/

    .card-header {
      background-color: hsl(204, 86%, 53%);
      .card-header-title {
        padding: 4px 10px;
        color: white;
      }
    }
  }

  .card-content {
    padding: 10px;

    td {
      padding: 0 !important;
      border: none !important;
    }

    .data-label {
      user-select: none;
    }
  }
</style>
