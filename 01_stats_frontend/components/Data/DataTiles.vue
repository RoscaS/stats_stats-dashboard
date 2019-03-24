<template>
  <div class="tile is-ancestor">

    <div class="tile is-parent is-vertical">
      <article class="tile is-child">
        <data-cell title="General" :data="data.general"/>
      </article>
      <article class="tile is-child">
        <data-cell title="Forme" :data="data.forme"/>
      </article>
    </div>

    <div class="tile is-vertical is-8">
      <div class="tile">

        <div class="tile is-parent is-vertical">
          <article class="tile is-child">
            <data-cell title="Centre" :data="data.centre"/>
          </article>
          <article class="tile is-child">
            <data-cell title="Dispersion" :data="data.dispersion"/>
          </article>
        </div>

        <div class="tile is-parent is-vertical">
          <article class="tile is-child">
            <data-cell title="Quantiles" :data="data.quantiles"/>
          </article>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
  import DataCell from './Tile';

  export default {
    components: {DataCell},
    props: {
      data: {type: Object},
    },
    mounted() {
    },
  };
</script>

<style lang="scss" scoped>

</style>
