<template>
  <div ref="root">
    <div class="navbar">
      <nuxt-link :to="adminActivated ? 'adminPanel' : '/'">
        <div class="admin-button" @click="activateAdmin">{{ admin }}</div>
      </nuxt-link>
      Log Manager
      <div class="menu-button" @click="sideBarActivated = !sideBarActivated"></div>
    </div>
    <div class="pt-[56px]">
      <nuxt/>
    </div>
    <div class="sidebar" v-show="sideBarActivated">
      <div class="text-[19px]">Filter</div>
      <div class="border-[#2f3136] border-y-[1px]">
        Levels
        <div class="grid grid-cols-2 px-4 justify-items-start my-1">
          <div class="level-checkbox">
            <input type="checkbox" v-model="filterLevels.warning"/>
            WARNING
          </div>
          <div class="level-checkbox">
            <input type="checkbox" v-model="filterLevels.info"/>
            INFO
          </div>
          <div class="level-checkbox">
            <input type="checkbox" v-model="filterLevels.debug"/>
            DEBUG
          </div>
          <div class="level-checkbox">
            <input type="checkbox" v-model="filterLevels.error"/>
            ERROR
          </div>
        </div>
      </div>
      <div class="border-[#2f3136] border-b-[1px]">
        Content
        <div class="my-1 mb-2">
          <input class="outline-none px-2 w-4/5 rounded-sm" placeholder="Police officer" v-model="filterText"/>
        </div>
      </div>
      <div class="border-[#2f3136] border-b-[1px]">
        Time
        <div class="mt-1 mb-2">
            <calendar/>
        </div>
      </div>
      <div class="px-3 py-1 bg-[#2f3136] cursor-pointer rounded-lg text-[#e5dfdf] mx-auto mt-3"
           style="width :fit-content" @click="filter">Apply
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "default",
  data() {
    return {
      date : null,
      sideBarActivated: false,
      filterLevels: {
        warning: false,
        error: false,
        info: false,
        debug: false
      },
      filterText: '',
      adminActivated : false,
      admin : 'Tables'
    }
  },
  mounted() {
    const currentTable = localStorage.getItem('currentTable')
    const savedLevels = localStorage.getItem('levelsFilter')
    const savedText = localStorage.getItem('textFilter')

    if (currentTable) {
      this.$store.commit('setCurrentTable', currentTable)
    }

    if (savedLevels) {
      for (let savedLevel of JSON.parse(savedLevels)) {
        this.filterLevels[savedLevel.toLowerCase()] = true
      }
    }
    if (savedText) {
      this.filterText = savedText
    }

    if (savedLevels || savedText) {
      this.filter()
    }
  },
  methods: {
    activateAdmin() {
        this.adminActivated = !this.adminActivated

        if (this.adminActivated) {
          this.admin = 'Logs'
        }
        else {
          this.admin = 'Tables'
        }
    },
    filter() {
      let time = this.$store.state.filterTime
      let levels = []
      let timeInSeconds = []

      for (let elem of time) {
        let seconds = 0
        let time_ = elem.split('/')

        let datetime = new Date(parseInt(time_[0]), parseInt(time_[1]) - 1, parseInt(time_[2]))
        seconds = datetime.getTime() / 1000

        timeInSeconds.push(seconds)
      }

      for (let elem in this.filterLevels) {
        if (this.filterLevels[elem]) {
          levels.push(elem.toUpperCase())
        }
      }

      localStorage.setItem('levelsFilter', JSON.stringify(levels))
      localStorage.setItem('textFilter', this.filterText)

      // filter levels
      this.$store.commit('changeFillFilter', levels)
      // filter text
      this.$store.commit('changeFilterText', this.filterText)
      // filter time
      this.$store.commit('replaceFilterTimeInSeconds', timeInSeconds)
      // update logs
      this.$store.commit('reFilter')
    },
  }
}
</script>

<style>

html::-webkit-scrollbar {
  width : 0 !important;
}

html {
  @apply bg-[#2f3136]
}

.navbar {
  /*color : #e5dfdf;*/
  @apply fixed bg-transparent/20 backdrop-filter backdrop-blur-lg w-screen pt-2 pb-3 text-center text-3xl text-[#c7bcbc]
}

.admin-button {
  @apply text-2xl h-[40px] px-2 border-2 border-[#c7bcbc] cursor-pointer absolute left-[30px] rounded-md
}

.menu-button {
  @apply absolute right-[30px] top-[14px] w-[30px] h-[30px] rounded-[100%] bg-transparent inline-block border-2 border-[#c7bcbc] cursor-pointer
}

.sidebar {
  font-family: 'Ubuntu Mono', monospace;
  height : calc(100% - 56px);
  @apply w-[300px] bg-white inline-block fixed right-0 top-[56px] bg-[#c7bcbc] text-center px-1 pt-2 overflow-y-auto
}


.level-checkbox {

}

</style>
