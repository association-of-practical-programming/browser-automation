const addMarquee = (ele) => {
  ele.innerHTML = `<marquee>${ele.innerHTML}</marquee>`
}

const allChildren = (ele) => {
  const children = Array.from(ele.children);
  if (children.length === 0) {
    return false;
  }
  for (const child of children) {
    allChildren(child);
    addMarquee(child);
  }
}