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
        :id="log.id"
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
      monitor: NaN,
      lastId: 0,
      limit: 5
    }
  },
  async mounted() {
    this.monitor = setInterval(async () => {
      // monitor log updates
      await this.filter()
    }, 1000)

    if (!this.$store.state.filtered) {
      this.applyFiltered()
      await this.reRender()
    }

  },
  methods: {
    turnLogState(field) {
      // show or hide log time/level/content
      this.$store.commit('turnLogState', field)
    },
    async getLastId() {
      let table_ = this.filterTable_()

      return await this.$axios.$post(this.API() + 'last', {
        tablename: table_
      })
    },
    API() {
      return this.$store.state.api
    },
    async reRender() {
      this.lastId = await this.getLastId()
      this.logs = []

      let levels_ = this.filterLevels_()
      let text_ = this.filterText_()
      let time_ = this.filterTime_()
      let table_ = this.filterTable_()

      for (let i = 0; i < 100; i++) {
        let newPack = await this.$axios.$post(this.API() + 'logs', {
          limit: this.limit,
          offset: i * this.limit,
          from_id: this.lastId,
          table: table_,
          time: time_,
          text: text_,
          levels: levels_
        })

        for (let elem of newPack) {
          this.logs.push(elem)
        }
      }
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
      let levels_ = this.filterLevels_()
      let text_ = this.filterText_()
      let time_ = this.filterTime_()
      let table_ = this.filterTable_()

      let last = await this.getLastId()

      if (last > this.lastId) {
        // add logs til last
        const limit = last - this.lastId

        let newLogs = await this.$axios.$post(this.API() + 'logs', {
          tablename: table_,
          limit: limit,
          from_id: last,
          levels: levels_,
          text: text_,
          time: time_
        })

        for (let elem of newLogs.reverse()) {
          this.logs.unshift(elem)
        }
      }
      if (last < this.lastId) {
        // remove all logs til last
      }

      this.lastId = last;
    }
  },
  destroyed() {
    clearInterval(this.monitor)
  },
  watch: {
    async '$store.state.filtered'(val) {
      if (!val) {
          this.applyFiltered()
          await this.reRender()
      }
    },
  }
}
</script>
