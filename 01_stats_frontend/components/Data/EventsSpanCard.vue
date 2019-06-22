<template>
    <div class="card">
      <div class="card-header is-info">
        <p class="card-header-title is-centered">🡐 Interval 🡒</p>
      </div>
      <div class="card-content">
        <div class="content">
          <p>
            {{ element.value }}
          </p>
          <p>
            <b>{{ element.percent }} %</b>
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
        text-align: center;
        padding: 0 auto 0 auto;
        margin: 0 auto 0 auto;
      }
    }
  }
</style>
