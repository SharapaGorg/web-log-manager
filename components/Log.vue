<template>
  <div ref="root">
    [
    <div class="time">{{ time }}</div>
    ]
    [
    <div class="level" :style="{ color : levelColor}">{{ level }}</div>
    ]
    <div class="log-text">{{ text }}</div>
  </div>
</template>

<script>
export default {
  name: "Log",
  props: {
    level: String,
    text: String,
    time: String,
    seconds: Number
  },
  data() {
    return {
      levelColor: '',
    }
  },
  async mounted() {
    switch (this.level) {
      case 'WARNING':
        this.levelColor = '#a7e801'
        break
      case 'ERROR':
        this.levelColor = '#e50808'
        break
      case 'DEBUG':
        this.levelColor = '#0606fc'
        break
      case 'INFO':
        this.levelColor = '#269a26'
        break
    }

    const selectedWord = this.$store.state.filterText

    if (selectedWord) {
      let start = this.text.indexOf(selectedWord)
      let finish = start + selectedWord.length

      this.underlineSlice(start, finish);
    }

  },
  methods: {
    underlineSlice (start, finish) {
      //
    }
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
  @apply inline-block w-[60px] text-center font-bold
}

.log-text {
  @apply inline-block
}

</style>
