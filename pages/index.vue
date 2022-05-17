<template>
  <div ref="root">
    <log
      v-for="log in logs"
      :level=log.level
      :text=log.text
      :time=log.time
      :key="log.id"
    />
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data() {
    return {
      logs: [],
      api: 'http://127.0.0.1:5000/logs',
      monitor: NaN
    }
  },
  async mounted() {
    if (!localStorage.getItem('levelsFilter') && !localStorage.getItem('textFilter')) {
      this.logs = await this.$axios.$get(this.api)
    }

    this.monitor = setInterval(async () => {
      // monitor log updates
      await this.filter()
    }, 1000)

  },
  methods: {
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
      let levels_ = this.filterLevels_()
      let text_ = this.filterText_()
      let time_ = this.filterTime_()
      let table_ = this.filterTable_()

      const currentLogs = await this.$axios.$post(this.api, {
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
