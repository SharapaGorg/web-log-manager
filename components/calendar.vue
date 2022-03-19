<template>
  <div ref="root">
    <div>
      <input class="outline-none px-2 w-4/5 rounded-sm" placeholder="2022/3/18 - 2022/3/18"/>
    </div>
    <div class="calendar">
      <div class="grid grid-cols-2 justify-items-center">
        <span>From</span>
        <span>To</span>
      </div>

      <div class="disable-select text-left grid grid-cols-2 justify-items-center px-2">
        <div>
          <div @click="decrementYear(1)" class="crement">-</div>
          <input v-model="selectedYear1" class="outline-none w-[32px] bg-transparent"/>
          <div @click="incrementYear(1)" class="crement">+</div>
        </div>

        <div>
          <div @click="decrementYear(2)" class="crement">-</div>
          <input v-model="selectedYear2" class="outline-none w-[32px] bg-transparent"/>
          <div @click="incrementYear(2)" class="crement">+</div>
        </div>
      </div>

      <div class="grid grid-cols-2 px-1 disable-select justify-items-center">

        <div>
          <span>{{ selectedMonth1 }}</span><br/>
          <div @click="changeMonth(1, 0)" class="crement"><-</div>
          <div @click="changeMonth(1, 1)" class="crement">-></div>
        </div>


        <div>
          <span>{{ selectedMonth2 }}</span><br/>
          <div @click="changeMonth(2, 0)" class="crement"><-</div>
          <div @click="changeMonth(2, 1)" class="crement">-></div>
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
      months: ['September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
    }
  },
  methods: {
    decrementYear(index) {
      this['selectedYear' + index]--
    },
    incrementYear(index) {
      this['selectedYear' + index]++
    },
    changeMonth(index, action) {
      let currentIndex= this.months.indexOf(this['selectedMonth' + index])

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
  @apply inline-block cursor-pointer
}

.calendar {
  @apply w-[250px] mx-auto h-[200px] bg-transparent rounded-md mt-2 border-[1px] border-black
}

</style>
