export const state = () => ({
  levelsFilter : ['WARNING', 'ERROR', 'DEBUG', 'INFO'],
  filterText : '',
  filterTime : ['1970/2/1', '3000/12/30'],
  filterTimeInSeconds: [],
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
  },
  changeFilterTime(state, [index, value]) {
    state.filterTime[index] = value
  },
  replaceFilterTimeInSeconds(state, value) {
    state.filterTimeInSeconds = value
  }
}
