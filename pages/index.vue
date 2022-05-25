<template>
  <div ref="root">
    <div class="top-bar">
      [
      <div
        class="log-time"
        @click="turnLogState('time')">Time
      </div>
      ]
      [
      <div
        class="log-level"
        @click="turnLogState('level')">Level
      </div>
      ]
      <div
        class="log-content"
        @click="turnLogState('content')">Content
      </div>
    </div>

    <div class="px-3">
      <log
        v-for="log in logs"
        :level=log.level
        :text=log.text
        :time=log.time
        :key="log.id"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data() {
    return {
      logs: [],
      monitor: NaN
    }
  },
  async mounted() {
    const API = this.$store.state.api + 'logs'

    if (!localStorage.getItem('levelsFilter') && !localStorage.getItem('textFilter')) {
      this.logs = await this.$axios.$get(API)
    }

    this.monitor = setInterval(async () => {
      // monitor log updates
      await this.filter()
    }, 1000)

  },
  methods: {
    turnLogState(field) {
      // show or hide log time/level/content
      this.$store.commit('turnLogState', field)
    },
    applyFiltered() {
      this.$store.commit('reFilter')
    },
    filterLevels_() {
      return this.$store.state.levelsFilter
    },
    filterText_() {
      return this.$store.state.filterText
    },
    filterTime_() {
      return this.$store.state.filterTimeInSeconds
    },
    filterTable_() {
      return this.$store.state.currentTable
    },
    async filter() {
      const API = this.$store.state.api + 'logs'

      let levels_ = this.filterLevels_()
      let text_ = this.filterText_()
      let time_ = this.filterTime_()
      let table_ = this.filterTable_()

      const currentLogs = await this.$axios.$post(API, {
        levels: levels_,
        text: text_,
        seconds: time_,
        tablename: table_
      })

      if (currentLogs !== this.logs) {
        this.logs = currentLogs
      }

      this.applyFiltered()
    }
  },
  destroyed() {
    clearInterval(this.monitor)
  },
  watch: {
    async '$store.state.filtered'(val) {
      if (!val) {
        await this.filter()
      }
    },
  }
}
</script>
