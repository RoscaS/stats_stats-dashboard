<template>
  <div class="card">
    <div class="card-content">
      <div class="content">
        <input class="percent-input" max="100" min="0" type="number" v-model="p_input"/>
        % des effectifs = <b>{{ nPercentEquals }}</b>
        <input class="n-input" type="number" v-model="n_input" />
        = <b>{{ nEqualsXPercent }}</b> % des effectifs
        <p></p>
        <p></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PercentCard",
  props: {
    total: { type: Number }
  },
  data: () => ({
    // percent: 0,
    // n: 0,

    n_input: 0,
    p_input: 0
  }),
  computed: {
    nPercentEquals() {
      return ((this.total * this.p_input) / 100).toFixed(3);
    },
    nEqualsXPercent() {
      return ((100 * this.n_input) / this.total).toFixed(3);
    }
  }
};
</script>

<style lang="scss" scoped>
.card {
  width: 280px;
  height: 70px;

  .card-header {
    background-color: #209cee;

    .card-header-title {
      color: white;
    }
  }

  .card-content {
    padding: 10px;

    input {
      border: none;
    }

    p {
      text-align: center;
      padding: 0 auto 0 auto;
      margin: 0 auto 0 auto;
    }

    .percent-input {
      width: 50px;
    }

    .n-input {
      width: 50px;
    }
  }
}
</style>
