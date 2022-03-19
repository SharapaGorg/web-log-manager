<template>
  <div ref="root">
    <log
      v-for="log in logs"
      :level = log.level
      :text = log.text
      :time = log.time
      :key="log.id"
    />
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data() {
    return {
      logs : [],
      api : 'https://shg.radolyn.com/logs'
    }
  },
  async mounted() {
    this.logs = await this.$axios.$get(this.api)
  },
  methods: {
    applyFiltered() {
      this.$store.commit('reFilter')
    },
    filterLevels_() {
      return this.$store.state.levelsFilter
    }
  },
  watch: {
    async '$store.state.filtered' (val)  {
      if (!val) {
        let levels_ = this.filterLevels_()

        this.logs = await this.$axios.$post(this.api, {
          levels : levels_
        })

        this.applyFiltered()
      }
    }
  }
}
</script>
