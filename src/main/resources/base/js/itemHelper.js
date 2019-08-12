function getItemKeys(item) {
  if (item) {
    return Object.keys(item).map(k => item[k]);
  } else return [];
}
