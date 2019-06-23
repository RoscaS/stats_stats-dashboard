<template>
    <div class="card">
<!--      <div class="card-header is-info">-->
<!--        <p class="card-header-title is-centered">🡐 Interval 🡒</p>-->
<!--      </div>-->
      <div class="card-content">
        <div class="content">
          <p>
            de <b>x<sub>{{element.start.cum}}</sub></b> à <b>x<sub>{{element.end.cum}}</sub></b>
            = <b>{{ element.interval.value }}</b>
          </p>
          <p>
            <b>{{ element.interval.percent }} %</b> des effectifs
          </p>
        </div>
      </div>
    </div>
  </template>

<script>
  export default {
    name: 'EventsSpanCard',
    props: {
      title: { type: String },
      element: { type: Object }
    },
  };
</script>

<style lang="scss" scoped>
  .card {
    width: 200px;

    .card-header {
      background-color: #209CEE;

      .card-header-title {
        color: white;
      }
    }

    .card-content {
      padding: 10px;
      p {
        padding: 0 auto 0 auto;
        margin: 0 auto 0 auto;
        :last-child {
          text-align: center;
        }
      }
    }
  }
</style>
