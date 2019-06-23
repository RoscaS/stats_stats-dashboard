<template>
  <div>
    <div class="events-row">
      <transition name="fade">
        <div class="events" v-if="showRange">
          <event-card class="event" title="Selected" :element="selected"></event-card>
          <events-span-card class="event" :element="interval"></events-span-card>
          <event-card class="event" title="Hovered" :element="hovered"></event-card>
          <percent-card class="percent-card" :total="total"></percent-card>
        </div>
      </transition>
    </div>
    <apexcharts height="430" type="line" :options="options" :series="series"/>
  </div>
</template>

<script>
  import EventCard from '../Data/EventCard';
  import EventsSpanCard from '../Data/EventsSpanCard';
  import PercentCard from '../Data/PercentCard';

  export default {
    components: {PercentCard, EventsSpanCard, EventCard},
    props: {
      ds: {type: Object},
      colors: {type: Array},
      showRange: {type: Boolean},
    },
    data: () => ({
      selected: {car: null, eff: null, cum: null},
      hovered: {car: null, eff: null, cum: null},
    }),

    methods: {
      setValues(attr, idx) {
        attr.car = this.ds.plot.freq.ticks[idx];
        attr.eff = this.ds.plot.freq.eff[idx];
        attr.cum = this.ds.plot.cum.eff[idx];
      },
    },

    computed: {
      total() {
        return this.ds.plot.cum.eff[this.ds.plot.cum.eff.length - 1];
      },
      interval() {
        let interval = {value: null, percent: null};
        if (!(this.selected.car === null || this.hovered.car === null)) {
          let max = this.total;
          let v = this.hovered.cum < this.selected.cum ? this.hovered.eff : this.selected.eff;
          interval.value = Math.abs(this.selected.cum - this.hovered.cum) + v;
          interval.percent = ((interval.value * 100) / max).toFixed(3);
        }
        return {start: this.selected, interval: interval, end: this.hovered};
      },

      options() {
        return {
          theme: {
            palette: 'palette7',
          },
          grid: {
            position: 'front',
            borderColor: '#5f5f5f',
          },
          markers: {
            size: [4, 6],
          },
          chart: {
            id: 'Frequences cumulées',
            toolbar: {show: false},
            events: {
              dataPointSelection: (e, chart, opts) => {
                this.setValues(this.selected, opts.dataPointIndex);
              },
              dataPointMouseEnter: (e, chart, opts) => {
                this.setValues(this.hovered, opts.dataPointIndex);
              },
            },
          },
          xaxis: {
            type: 'category',
            categories: this.ds.plot.freq.ticks,
          },
          yaxis: [
            {
              title: {
                text: 'Effectifs cumulées',
              },
            },
            {
              opposite: true,
              title: {
                text: 'Effectif',
              },
            },
          ],

          plotOptions: {
            bar: {
              // distributed: true,
              columnWidth: '100%',
            },
            line: {
              // color: th
            },
          },
        };
      },
      series() {
        return [
          {
            name: 'Effectifs cumulées',
            type: 'line',
            data: this.ds.plot.cum.eff,
          },
          {name: 'Effectif', type: 'bar', data: this.ds.plot.freq.eff},
        ];
      },
    },
  };
</script>

<style lang="scss">
  .fade-enter-active {
    transition: opacity 3.5s;
  }

  .fade-leave-active {
    transition: opacity .5s;
  }

  .fade-enter, .fade-leave-to {
    opacity: 0;
  }

  .events-row {
    height: 85px;
    margin-top: -20px;
    margin-bottom: -5px;
  }

  .events {
    display: flex;

    .event {
      margin-right: 20px;
    }

    .percent-card {
      margin-left: 78px;
      margin-right: 50px;
    }
  }
</style>
