function range(end, fill = null) {
  let array = [...Array(end).keys()];
  return array.map(i => fill != null ? fill : i);
}

function randint(max = 100) {
  return Math.floor(Math.random() * (max + 1));
}

function format(str) {
  let clean = str.replace('_', ' ');
  return clean[0].toUpperCase() + clean.slice(1);
}

function colorPicker(count, alpha = 0.8, random=false) {
  if (count > rgbColours.length-1 || random) {
    return coloursGenerator(count, alpha);
  }
  let picked = [];
  for (let i in range(count)) {
    picked.push(`rgba(${rgbColours[i]}, ${alpha})`);
  }
  return picked;
}

function coloursGenerator(count, alpha = 0.8) {
  let colours = [];
  for (let i in range(10)) {
    let num = Math.round(0xffffff * Math.random());
    let r = num >> 16;
    let g = num >> 8 & 255;
    let b = num & 255;
    colours.push(`rgba(${r}, ${g}, ${b}, ${alpha})`);
  }
  return colours;
}

const rgbColours = [
  '102,217,239',
  '166,226,46',
  '0, 166, 237',
  '253,151,31',
  '0, 226, 145',
  '246, 81, 29',
  '50, 144, 143',
  '249,38,114',
  '174,129,255',

  '135, 166, 252',
  '87, 157, 206',
  '13, 44, 84',
  '236, 125, 16',
  '255, 180, 0',
  '200, 255, 35',
  '130, 32, 74',
  '47, 6, 1',
  '251, 40, 174',
  '194, 0, 251',
  '217, 3, 104',
  '217, 42, 46',

  '183, 255, 102',
  '81, 237, 49',
  '85, 58, 65',
  '127, 184, 0',
  '0, 226, 145',

];

export { range, randint, format, colorPicker, coloursGenerator };
