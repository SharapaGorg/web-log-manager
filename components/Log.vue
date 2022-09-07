<template>
  <div ref="root" class="log">
    [
    <div
      class="time"
      v-show="logsStates.time">{{ time }}
    </div>
    ]
    [
    <div
      class="level"
      :style="{ color : levelColor}"
      v-show="logsStates.level">{{ level }}
    </div>
    ]
    <div
      class="log-text"
      v-show="!slice && logsStates.content">{{ text }}
    </div>
    <div
      class="log-text"
      v-show="slice && logsStates.content">
      <span>{{ beforeSlice }}
        <span class="bg-blue-500">{{ slice }}</span>
        {{ afterSlice }}
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "Log",
  props: {
    level: String,
    text: String,
    time: String,
    seconds: Number,
    id : Number
  },
  data() {
    return {
      levelColor: '',
      beforeSlice: '',
      afterSlice: '',
      slice: '',
      logsStates: {
        time: true,
        level: true,
        content: true
      }
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

    this.detectRange_()

  },
  methods: {
    detectRange_() {
      const selectedWord = this.$store.state.filterText

      if (selectedWord) {
        let start = this.text.indexOf(selectedWord)
        let finish = start + selectedWord.length

        this.underlineSlice(start, finish);
      } else {
        this.beforeSlice = this.afterSlice = this.slice = ''
      }
    },
    underlineSlice(start, finish) {
      this.beforeSlice = this.text.slice(0, start)
      this.afterSlice = this.text.slice(finish, this.text.length - 1)
      this.slice = this.text.slice(start, finish)
    }
  },
  watch: {
    '$store.state.filtered'(val) {
      this.detectRange_()
    },
    '$store.state.logStates.time'(val) {
      this.logsStates.time = val
    },
    '$store.state.logStates.level' (val) {
      this.logsStates.level = val
    },
    '$store.state.logStates.content' (val) {
      this.logsStates.content = val
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
  /*transform : translateY(8px);*/
  @apply inline-block
}

.log {
  @apply h-[24px]
}

</style>
