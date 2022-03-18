<template>
  <div ref="root">
    <div class="navbar">
      Log Manager
      <div class="menu-button" @click="sideBarActivated = !sideBarActivated"></div>
    </div>
    <div class="px-3 pt-[56px]">
      <nuxt/>
    </div>
    <div class="sidebar" v-show="sideBarActivated">
      <div class="text-[19px]">Filter</div>
      <div class="border-[#2f3136] border-y-[1px]">
        Log Levels
        <div class="grid grid-cols-2 px-4 justify-items-start">
          <div class="level-checkbox">
            <input type="checkbox"/>
            WARNING
          </div>
          <div class="level-checkbox">
            <input type="checkbox"/>
            INFO
          </div>
          <div class="level-checkbox">
            <input type="checkbox"/>
            DEBUG
          </div>
          <div class="level-checkbox">
            <input type="checkbox"/>
            ERROR
          </div>
        </div>
      </div>
      <div class="px-3 py-1 bg-[#2f3136] cursor-pointer rounded-lg text-[#e5dfdf] mx-auto mt-3" style="width :fit-content">Accept</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "default",
  data() {
    return {
      sideBarActivated : false
    }
  }
}
</script>

<style>

html {
  @apply bg-[#2f3136]
}

.navbar {
  /*color : #e5dfdf;*/
  @apply fixed bg-transparent/20 backdrop-filter backdrop-blur-lg w-screen pt-2 pb-3 text-center text-3xl text-[#c7bcbc]
}

.menu-button {
  @apply absolute right-[30px] top-[14px] w-[30px] h-[30px] rounded-[100%] bg-transparent inline-block border-2 border-[#c7bcbc] cursor-pointer
}

.sidebar {
  font-family: 'Ubuntu Mono', monospace;
  @apply w-[300px] h-full bg-white inline-block fixed right-0 top-[56px] bg-[#c7bcbc] text-center px-1 pt-2
}

.level-checkbox {

}

</style>
