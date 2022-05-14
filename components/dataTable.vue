<template>
  <div ref="root" class="table-container">
    <span class="table-name">{{ title }}</span>
    <span
      v-show="selected"
      class="float-right relative right-[5px] text-[#a7e801] font-bold"
    >SELECTED</span>

    <div
      @click="selectTable"
      v-show="!selected"
      class="select-button"
    >SELECT</div>

  </div>
</template>

<script>
export default {
  name: "dataTable",
  props: {
    title : String,
  },
  computed: {
    selected() {
      return this.$store.state.currentTable === this.title
    }
  },
  methods: {
    selectTable() {
      this.$store.commit('setCurrentTable', this.title)
      localStorage.setItem('currentTable', this.title)
    }
  }
}
</script>

<style scoped>

.select-button {
  @apply float-right relative right-[5px] font-bold;
  @apply rounded-sm
}

.select-button:hover {
  @apply underline
}

.table-container {
  @apply cursor-pointer inline-block w-full;
  @apply text-[#c7bcbc]
}

.table-name {
  font-family: 'Ubuntu Mono', monospace;
  @apply px-2 py-1
}

.table-container:hover {
  background : #c7bcbc;
  color : #2f3136
}

</style>
