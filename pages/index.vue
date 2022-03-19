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
    if (!localStorage.getItem('levelsFilter') && !localStorage.getItem('textFilter')) {
      this.logs = await this.$axios.$get(this.api)
    }
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
    }
  },
  watch: {
    async '$store.state.filtered' (val)  {
      if (!val) {
        let levels_ = this.filterLevels_()
        let text_ = this.filterText_()

        this.logs = await this.$axios.$post(this.api, {
          levels : levels_,
          text : text_
        })

        this.applyFiltered()
      }
    }
  }
}
</script>
