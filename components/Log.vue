<template>
  <div ref="root">
      [<div class="time">{{ time }}</div>]
      [<div class="level" :style="{ color : levelColor}">{{ level }}</div>]
      <div class="log-text">{{ text }}</div>
  </div>
</template>

<script>
export default {
  name: "Log",
  props: {
    level : String,
    text : String,
    time : String,
    seconds : Number
  },
  data() {
    return {
      levelColor : '',
    }
  },
  async mounted() {
    switch (this.level) {
      case 'WARNING':
        this.levelColor = '#a7e801'
        break
      case 'ERROR':
        this.levelColor = '#ad0000'
        break
      case 'DEBUG':
        this.levelColor = '#0404ee'
        break
      case 'INFO':
        this.levelColor = '#269a26'
        break
    }

    this.logs = await this.$axios.$get('/api/logs')
    console.log(this.logs)
  }
}
</script>

<style scoped>

* {
  font-family: 'Ubuntu Mono', monospace;
  @apply text-[#c7bcbc]
}

.time {
  @apply inline-block w-[152px] text-center
}

.level {
  /*color : #269a26;*/
  @apply inline-block w-[60px] text-center
}

.log-text {
  @apply inline-block
}

</style>
