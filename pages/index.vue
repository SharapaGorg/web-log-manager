<template>
  <div ref="root">
    <log
      v-for="log in logs"
      :level = log.level
      :text = log.text
      :time = log.time
    />
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data() {
    return {
      logs : []
    }
  },
  async mounted() {
    this.logs = await this.$axios.$get('/api/logs')
  }
}
</script>
