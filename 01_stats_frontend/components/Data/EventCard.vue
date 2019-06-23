<template>
  <div class="card">
<!--    <div class="card-header" :style="headerColor()">-->
<!--      <p class="card-header-title is-centered">{{ title }}</p>-->
<!--    </div>-->
    <div class="card-content">
      <div class="content">
        <table class="table is-narrow">
          <tr>
            <td>Caractère</td>
            <td>{{ element.car }}</td>
          </tr>
          <tr>
            <td>Effectif</td>
            <td>{{ element.eff }}</td>
          </tr>
          <tr>
            <td>Cumulé</td>
            <td>{{ element.cum }}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EventCard",
  props: {
    title: { type: String },
    element: { type: Object }
  },
  methods: {
    headerColor() {
      // return `background-color: ${this.title === 'Selected' ? '#329086' : '#42B5A8'}`
    }
  }
};
</script>

<style lang="scss" scoped>
.card {
  width: 150px;

  .card-header {
    .card-header-title {
      /*color: white;*/
    }
  }

  .card-content {
    padding: 0 5px 0 5px;
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
  }
}
</style>
