export const state = () => ({
  levelsFilter : ['WARNING', 'ERROR', 'DEBUG', 'INFO'],
  filtered : true
})

export const mutations = {
  reFilter(state) {
    state.filtered = !state.filtered
  },
  changeFillFilter(state, value) {
    state.levelsFilter = value
  }
}
