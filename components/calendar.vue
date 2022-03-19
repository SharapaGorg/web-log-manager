<template>
  <div ref="root">
    <div>
      <input class="outline-none px-2 w-4/5 rounded-sm" placeholder="2022/3/18 - 2022/3/18"/>
    </div>
    <div class="calendar disable-select">

      <div>
        <div class="grid grid-cols-3 justify-items-center">
          <div @click="decrementYear(1)" class="crement">-</div>
          <input v-model="selectedYear1" class="outline-none w-[32px] bg-transparent"/>
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
          <input v-model="selectedYear2" class="outline-none w-[32px] bg-transparent"/>
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
      selectedYear1: 2022,
      selectedYear2: 2022,
      selectedMonth1: 'April',
      selectedMonth2: 'February',
      selectedDay1: 1,
      selectedDay2: 1,
      months: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    }
  },
  methods: {
    decrementYear(index) {
      if (this['selectedYear' + index] > 0) {
        this['selectedYear' + index]--
      }
    },
    incrementYear(index) {
      this['selectedYear' + index]++
    },
    incrementDay(index) {
      this['selectedDay' + index]++
    },
    decrementDay(index) {
      if (this['selectedDay' + index] > 0) {
        this['selectedDay' + index]--
      }
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
  @apply inline-block cursor-pointer text-xl font-bold
}

.calendar {
  @apply w-[250px] mx-auto bg-transparent rounded-md mt-2 border-[1px] border-black py-2
}

</style>
