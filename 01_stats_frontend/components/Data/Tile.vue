<template>
<div>
  <div class="card">

    <header class="card-header">
      <p class="card-header-title">
        {{ format(title) }}
      </p>
    </header>

    <div class="card-content">
      <div class="content">
        <table v-if="title !== 'Quantiles'" class="table">
          <tr v-for="(idx, i) in data" :key="i" @click="showData(i)" @mouseout="hideData()">
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
  <div>
    <div class="images">
      <transition name="fade">
        <img v-if="modeImage" src="https://i.imgur.com/F5Hnpjl.png" alt="">
        <img v-if="modeQuantileImage" src="https://i.imgur.com/QGnKTUf.png" alt="">
        <img v-if="formulaImage" src="https://i.imgur.com/mF3bddd.png" alt="">
      </transition>
    </div>
    <div class="infos">
      <transition name="fade">
        <div v-if="caractereInfo" class="caractere">
          <span>Quantitatif</span>
          <ul>
            <li>Continu</li>
            <li>Discret</li>
          </ul>
          <span>Qualitatif</span>
          <ul>
            <li>Ordinal</li>
            <li>Nominal: pas ordinal (couleur yeux, état civil)</li>
          </ul>
        </div>
      </transition>
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
      coefficients: ['coefficient_de_variation', 'coefficient_asymetrie', 'coefficient_applatissement'],
      modeImage: false,
      modeQuantileImage: false,
      formulaImage: false,
      caractereInfo: false,
    }),
    props: {
      title: {type: String},
      data: {type: Object},
    },
    methods: {
      format(str) { return format(str); },
      showData(data) {
        if  (data === "effectifs") {
          this.caractereInfo = true;
        } else if (data === "classe_modale") {
          this.modeQuantileImage = true;
        } else if (data === "mode"){
          this.modeImage = true;
        } else if (data === "ecart_type"){
          this.formulaImage = true;
        }
      },
      hideData() {
        this.modeImage = false;
        this.modeQuantileImage = false;
        this.formulaImage = false;
        this.caractereInfo = false;
      }
    },
  };
</script>

<style lang="scss" scoped>
  .fade-enter-active {
    transition: opacity 3.5s;
  }
  .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }

  .images {
    position: absolute;
    bottom: 30px;
    left: 20px;
    opacity: .5;
    z-index: 5;
  }

  .infos {
    position: absolute;
    top: 270px;
    right: 500px;
    opacity: .1;
    z-index: 5;
  }

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
    }

    tr {
      &:last-child {
        td {
          border: none !important;
        }
      }
    }

    .data-label {
      user-select: none;
    }
  }
</style>
