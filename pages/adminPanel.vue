<template>
  <div ref="root">
    <div class="w-1/2 mx-auto">
      <span class='title'>List of tables</span>
      <div class="tables">
        <data-table
          v-for="table in tables"
          :title="table"
          :selected="true"
          :key="table"
        />
      </div>
    </div>

    <div class="w-1/2">

    </div>
  </div>
</template>

<script>
export default {
  name: "adminPanel",
  data() {
    return {
      tables: [],
      // api: 'http://127.0.0.1:5000/tables'
      // api : 'https://shg.radolyn.com/tables'
    }
  },
  async mounted() {
    await this.get_tables()
  },
  methods: {
    async get_tables() {
      const api = this.$store.state.api + 'tables'
      this.tables = await this.$axios.$get(api)
    }
  }
}
</script>

<style scoped>

.title {
  @apply text-[#c7bcbc] text-2xl;
  font-family: 'Ubuntu Mono', monospace;
}

.tables {
  @apply border-2 border-[#c7bcbc] rounded-sm
}

</style>
