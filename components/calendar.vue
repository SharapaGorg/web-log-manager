<template>
  <div ref="root">
    <div>
      <span class="outline-none px-2 w-2/5 rounded-sm">{{ time1 }}</span>
      <span class="outline-none px-2 w-2/5 rounded-sm">{{ time2 }}</span>
    </div>
    <div class="calendar disable-select">

      <div>
        <div class="grid grid-cols-3 justify-items-center">
          <div @click="decrementYear(1)" class="crement">-</div>
          <input v-model="selectedYear1" class="outline-none w-[32px] bg-transparent text-center"/>
          <div @click="incrementYear(1)" class="crement">+</div>
        </div>

        <div class="grid grid-cols-3 justify-items-center">
          <div @click="changeMonth(1, 0)" class="crement"><-</div>
          <span>{{ selectedMonth1 }}</span>
          <div @click="changeMonth(1, 1)" class="crement">-></div>
        </div>

        <div class="grid grid-cols-3 justify-items-center">
          <div @click="decrementDay(1)" class="crement">-</div>
          <input v-model="selectedDay1" class="outline-none w-[32px] bg-transparent text-center"/>
          <div @click="incrementDay(1)" class="crement">+</div>
        </div>
      </div>

      <div class="h-[1px] w-4/5 bg-black mx-auto my-1.5"></div>

      <div>
        <div class="grid grid-cols-3 justify-items-center">
          <div @click="decrementYear(2)" class="crement">-</div>
          <input v-model="selectedYear2" class="outline-none w-[32px] bg-transparent text-center"/>
          <div @click="incrementYear(2)" class="crement">+</div>
        </div>

        <div class="grid grid-cols-3 justify-items-center">
          <div @click="changeMonth(2, 0)" class="crement"><-</div>
          <span>{{ selectedMonth2 }}</span>
          <div @click="changeMonth(2, 1)" class="crement">-></div>
        </div>

        <div class="grid grid-cols-3 justify-items-center">
          <div @click="decrementDay(2)" class="crement">-</div>
          <input v-model="selectedDay2" class="outline-none w-[32px] bg-transparent text-center"/>
          <div @click="incrementDay(2)" class="crement">+</div>
        </div>
      </div>

    </div>

  </div>
</template>

<script>

export default {
  name: 'Calendar',
  data() {
    return {
      time1: '1970/2/1',
      time2: '3000/12/30',
      selectedYear1: 1970,
      selectedYear2: 3000,
      selectedMonth1: 'February',
      selectedMonth2: 'December',
      selectedDay1: 1,
      selectedDay2: 30,
      months: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    }
  },
  mounted() {
    this.time1 = this.selectedYear1 + '/' + (this.months.indexOf(this.selectedMonth1) + 1) + '/' + this.selectedDay1
    this.time2 = this.selectedYear2 + '/' + (this.months.indexOf(this.selectedMonth2) + 1) + '/' + this.selectedDay2
  },
  methods: {
    setDate_(index, key, value) {
      let currentDate = this['time' + index].split('/')
      currentDate[key] = value

      this['time' + index] = currentDate.join('/')
    },
    setYear(index) {
      this.setDate_(index, 0, this['selectedYear' + index])
    },
    setDay(index) {
      this.setDate_(index, 2, this['selectedDay' + index])
    },
    setMonth(index) {
      let month = this.months.indexOf(this['selectedMonth' + index]) + 1
      this.setDate_(index, 1, month)
    },
    decrementYear(index) {
      if (this['selectedYear' + index] > 0) {
        this['selectedYear' + index]--
      }
    },
    decrementDay(index) {
      if (this['selectedDay' + index] > 1) {
        this['selectedDay' + index]--
      }
    },
    incrementYear(index) {
      this['selectedYear' + index]++
    },
    incrementDay(index) {
      this['selectedDay' + index]++
    },
    changeMonth(index, action) {
      let currentIndex = this.months.indexOf(this['selectedMonth' + index])

      action ? currentIndex++ : currentIndex--

      if (this.months[currentIndex]) {
        this['selectedMonth' + index] = this.months[currentIndex]
        return
      }

      this['selectedMonth' + index] = this.months[0]
    }
  },
  watch: {
    time1() {
      this.$store.commit('changeFilterTime', [
        0, this.time1
      ])
    },
    time2() {
      this.$store.commit('changeFilterTime', [
        1, this.time2
      ])
    },
    selectedYear1() {
      this.setYear(1)
    },
    selectedYear2() {
      this.setYear(2)
    },
    selectedDay1() {
      this.setDay(1)
    },
    selectedDay2() {
      this.setDay(2)
    },
    selectedMonth1() {
      this.setMonth(1)
    },
    selectedMonth2() {
      this.setMonth(2)
    }
  }
}

</script>

<style scoped>

.disable-select {
  user-select: none; /* supported by Chrome and Opera */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
}

.crement {
  transform: translateY(-4px);
  @apply inline-block cursor-pointer text-xl
}

.calendar {
  @apply w-[250px] mx-auto bg-transparent rounded-md mt-2 border-[1px] border-black py-2
}

</style>
