export const state = () => ({
  levelsFilter : ['WARNING', 'ERROR', 'DEBUG', 'INFO'],
  filterText : '',
  filtered : true
})

export const mutations = {
  reFilter(state) {
    state.filtered = !state.filtered
  },
  changeFillFilter(state, value) {
    state.levelsFilter = value
  },
  changeFilterText(state, value) {
    state.filterText = value
  }
}
